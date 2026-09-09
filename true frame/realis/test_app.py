import asyncio, json
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        page = await browser.new_page(viewport={'width':1440,'height':960})
        errors = []
        page.on('console', lambda m: errors.append(f'console.{m.type}: {m.text}') if m.type in ('error','warning') else None)
        page.on('pageerror', lambda e: errors.append(f'pageerror: {e}'))

        await page.goto('file:///home/user/realis/index.html')
        await page.wait_for_timeout(800)

        # ---- 1. hero compare initial state ----
        clip = await page.evaluate("document.getElementById('heroLayer').style.clipPath")
        print('hero initial clip:', clip)

        # ---- 2. load fix sample ----
        await page.click('#heroSample')
        await page.wait_for_timeout(600)  # scroll + load sample
        await page.wait_for_selector('#cmp-fix:not([hidden])', timeout=8000)
        await page.wait_for_timeout(600)
        await page.wait_for_timeout(500)
        stats = await page.evaluate("""() => {
            const c=document.getElementById('fixCanvas');
            const d=c.getContext('2d').getImageData(0,0,c.width,c.height).data;
            let sum=0, nonEdge=0;
            for(let i=0;i<d.length;i+=4){sum+=d[i]+d[i+1]+d[i+2];nonEdge++;}
            return {w:c.width,h:c.height,avg:Math.round(sum/nonEdge/3)};
        }""")
        print('fix canvas after sample:', stats)

        # capture 'before' pixels, then crank sliders and verify change
        before_px = await page.evaluate("""() => {
            const c=document.getElementById('fixCanvas');
            return Array.from(c.getContext('2d').getImageData(c.width/2|0,c.height/2|0,1,1).data.slice(0,3));
        }""")
        await page.evaluate("""() => {
            const set=(id,v)=>{const el=document.getElementById(id);el.value=v;el.dispatchEvent(new Event('input'));};
            set('r-tex',90);set('r-matte',90);set('r-clar',80);set('r-warm',40);
        }""")
        await page.wait_for_timeout(400)
        after_px = await page.evaluate("""() => {
            const c=document.getElementById('fixCanvas');
            return Array.from(c.getContext('2d').getImageData(c.width/2|0,c.height/2|0,1,1).data.slice(0,3));
        }""")
        print('fix center px before:', before_px, '→ after sliders:', after_px, '| changed:', before_px != after_px)

        # ---- 3. compare slider drag on the fix viewport ----
        handle_before = await page.evaluate("document.querySelector('#cmp-fix .cmp-handle').style.left")
        box = await page.locator('#cmp-fix').bounding_box()
        cx, cy = box['x']+box['width']*0.3, box['y']+box['height']*0.5
        await page.mouse.move(box['x']+box['width']*0.5, cy)
        await page.mouse.down()
        await page.mouse.move(cx, cy, steps=5)
        await page.mouse.up()
        handle_after = await page.evaluate("document.querySelector('#cmp-fix .cmp-handle').style.left")
        print(f'compare drag: {handle_before} → {handle_after} (expect ~30%)')

        # ---- 4. upscaler tab ----
        await page.click('.ttab[data-tab="up"]')
        await page.wait_for_function("document.getElementById('upCanvas').height >= 1120", timeout=15000)
        await page.wait_for_timeout(300)
        await page.wait_for_timeout(400)
        up = await page.evaluate("""() => {
            const c=document.getElementById('upCanvas');
            return {w:c.width,h:c.height, info:document.getElementById('upInfo').textContent};
        }""")
        print('upscale preview (2x):', up)
        await page.click('#upFactorSeg button[data-f="4"]')
        await page.wait_for_timeout(900)
        up4 = await page.evaluate("() => document.getElementById('upCanvas').width")
        print('upscale preview (4x) width:', up4)

        # ---- 5. presets tab ----
        await page.click('.ttab[data-tab="pr"]')
        await page.wait_for_function("document.getElementById('prCanvas').width > 400", timeout=8000)
        await page.wait_for_timeout(400)
        await page.wait_for_timeout(400)
        pr_before = await page.evaluate("""() => {
            const c=document.getElementById('prCanvas');
            return Array.from(c.getContext('2d').getImageData(c.width/2|0,c.height/4|0,1,1).data.slice(0,3));
        }""")
        await page.click('[data-preset="noir"]')
        await page.wait_for_timeout(400)
        pr_after = await page.evaluate("""() => {
            const c=document.getElementById('prCanvas');
            return Array.from(c.getContext('2d').getImageData(c.width/2|0,c.height/4|0,1,1).data.slice(0,3));
        }""")
        print('presets px cinematic:', pr_before, '→ noir:', pr_after, '| changed:', pr_before != pr_after)

        # ---- 6. export path (intercept download) ----
        await page.click('.ttab[data-tab="fix"]')
        await page.wait_for_timeout(300)
        async with page.expect_download(timeout=20000) as dl:
            await page.click('#dl-fix')
            await page.wait_for_timeout(500)
        download = await dl.value
        path = await download.path()
        import os
        print('download triggered:', download.suggested_filename, os.path.getsize(path)//1024, 'KB')

        # ---- 6b. grade lab ----
        await page.click('.ttab[data-tab="gl"]')
        await page.wait_for_function("document.getElementById('glCanvas').width > 400", timeout=8000)
        await page.wait_for_timeout(500)
        glpx = "(c=>Array.from(c.getContext('2d').getImageData(c.width*0.12|0,c.height*0.92|0,1,1).data.slice(0,3)))(document.getElementById('glCanvas'))"
        gl0 = await page.evaluate(glpx)
        await page.click('[data-glseed="noir"]')
        await page.wait_for_timeout(500)
        gl1 = await page.evaluate(glpx)
        await page.evaluate("(()=>{const el=document.getElementById('r-shAmt');el.value=70;el.dispatchEvent(new Event('input'));})()")
        await page.wait_for_timeout(500)
        gl2 = await page.evaluate(glpx)
        print('grade lab shadow px:', gl0, '→ noir:', gl1, '→ +blue split:', gl2)
        # idempotence: same settings must re-render identically from pristine source
        await page.evaluate("(()=>{const el=document.getElementById('r-shAmt');el.value=0;el.dispatchEvent(new Event('input'));})()")
        await page.wait_for_timeout(400)
        gl3 = await page.evaluate(glpx)
        print('idempotence (split removed → noir again):', gl3, '| matches noir:', gl3 == gl1)
        await page.fill('#lookName','TestLook')
        await page.click('#saveLook')
        await page.wait_for_timeout(300)
        n1 = await page.evaluate("document.querySelectorAll('#lookList .look-item').length")
        await page.screenshot(path='/home/user/realis/shot-gradelab.png')
        async with page.expect_download(timeout=20000) as dl2:
            await page.click('#dl-gl')
            await page.wait_for_timeout(500)
        d2 = await dl2.value
        print('grade lab download:', d2.suggested_filename, os.path.getsize(await d2.path())//1024, 'KB')
        # persistence across reload
        await page.reload()
        await page.wait_for_timeout(900)
        n2 = await page.evaluate("document.querySelectorAll('#lookList .look-item').length")
        print('saved looks before/after reload:', n1, n2)
        # apply-on-empty guard (no image loaded after reload)
        await page.click('.ttab[data-tab="gl"]')
        await page.click('#lookList [data-la="0"]')
        await page.wait_for_timeout(400)
        print('apply-on-empty guard: no crash')


        # ---- 6d. prompt studio ----
        await page.click('.ttab[data-tab="ps"]')
        await page.wait_for_function("document.getElementById('psText').value.length > 50", timeout=8000)
        t0 = await page.input_value('#psText')
        t1 = t0
        for _ in range(3):
            await page.click('#psRandom')
            await page.wait_for_timeout(350)
            t1 = await page.input_value('#psText')
            if t1 != t0: break
        print('prompt len:', len(t0), '| surprise changed it:', t1 != t0)
        # load sample (source was reset by reload earlier)
        await page.click('#drop-ps [data-sample]')
        await page.wait_for_function("document.getElementById('psCanvas').width > 400", timeout=15000)
        await page.wait_for_timeout(500)
        pspx = "(c=>Array.from(c.getContext('2d').getImageData(c.width*0.12|0,c.height*0.92|0,1,1).data.slice(0,3)))(document.getElementById('psCanvas'))"
        psA = await page.evaluate(pspx)
        await page.click('#psrow-light button:nth-child(4)')  # Neon night
        await page.wait_for_timeout(800)
        psB = await page.evaluate(pspx)
        drv = await page.evaluate("document.querySelectorAll('#psDrivers .chip').length")
        print('prompt look px:', psA, '→ neon:', psB, '| changed:', psA != psB, '| drivers:', drv)
        await page.click('#psCopy')
        await page.wait_for_timeout(500)
        hist = await page.evaluate("document.querySelectorAll('#psHist .look-item').length")
        print('prompt history entries:', hist)
        await page.click('#psToLab')
        await page.wait_for_timeout(600)
        glon = await page.evaluate("document.querySelector('.ttab[data-tab=\"gl\"]').classList.contains('active')")
        print('to-grade-lab → gl tab active:', glon)
        await page.click('.ttab[data-tab="ps"]')
        await page.wait_for_timeout(600)
        await page.screenshot(path='/home/user/realis/shot-prompt.png')


        # ---- 6e. platform formats ----
        await page.click('.ttab[data-tab="ps"]')
        await page.wait_for_function("document.getElementById('psText').value.length > 50", timeout=8000)
        fmts = await page.evaluate("(() => { const out={}; ['universal','midjourney','sd','dalle','flux'].forEach(p=>{PSS.plat=p;out[p]=psFormat();}); PSS.plat='universal'; return out; })()")
        print('fmt midjourney has --ar:', '--ar' in fmts['midjourney'], '| sd has NEGATIVE:', 'NEGATIVE' in fmts['sd'], '| dalle has Avoid:', 'Avoid' in fmts['dalle'], '| flux has Do not include:', 'Do not include' in fmts['flux'])

        # ---- 6f. batch ----
        await page.click('.ttab[data-tab="ba"]')
        await page.set_input_files('#baInput', ['/tmp/batch1.jpg', '/tmp/batch2.jpg'])
        await page.wait_for_function("document.querySelectorAll('#baGrid .ba-item').length === 2", timeout=10000)
        await page.click('#baModeSeg button[data-m="preset"]')
        await page.click('[data-bapreset="noir"]')
        await page.click('#baRun')
        await page.wait_for_function("[...document.querySelectorAll('#baGrid .ba-item')].every(i => i.classList.contains('done'))", timeout=30000)
        await page.wait_for_timeout(400)
        zip_disabled = await page.evaluate("document.getElementById('baZip').disabled")
        print('batch done | zip enabled:', not zip_disabled)
        async with page.expect_download(timeout=30000) as dl3:
            await page.click('#baZip')
            await page.wait_for_timeout(500)
        d3 = await dl3.value
        zpath = await d3.path()
        import zipfile as zfmod
        z = zfmod.ZipFile(zpath)
        bad = z.testzip()
        names = z.namelist()
        print('ZIP file:', d3.suggested_filename, '| entries:', names, '| integrity bad file:', bad)
        sizes = [i.file_size for i in z.infolist()]
        print('ZIP entry sizes:', sizes, '| all > 10KB:', all(x > 10240 for x in sizes))

        # ---- 6g. showcase ----
        show_clip = await page.evaluate("(()=>{const l=document.getElementById('showLayer');return l? l.style.clipPath : 'MISSING';})()")
        print('showcase layer clip:', show_clip)
        loupe_ok = await page.evaluate("!!document.getElementById('loupe')")
        print('loupe present:', loupe_ok)
        await page.click('.ttab[data-tab="ba"]')
        await page.evaluate("document.getElementById('app').scrollIntoView()")
        await page.wait_for_timeout(900)
        await page.screenshot(path='/home/user/realis/shot-batch.png')

        # ---- 7. pricing removed / sections ----
        html = await page.content()
        print('pricing mentions in DOM:', html.lower().count('pricing'))

        # ---- screenshots ----
        await page.evaluate("window.scrollTo(0,0)")
        await page.wait_for_timeout(600)
        await page.screenshot(path='/home/user/realis/shot-hero.png')
        await page.evaluate("document.getElementById('app').scrollIntoView()")
        await page.wait_for_timeout(900)
        await page.screenshot(path='/home/user/realis/shot-app.png')
        await page.click('.ttab[data-tab="pr"]')
        await page.wait_for_timeout(600)
        await page.screenshot(path='/home/user/realis/shot-presets.png')

        # mobile
        mob = await browser.new_page(viewport={'width':390,'height':844})
        await mob.goto('file:///home/user/realis/index.html')
        await mob.wait_for_timeout(900)
        await mob.screenshot(path='/home/user/realis/shot-mobile.png')

        print('ERRORS:', json.dumps(errors[:10], indent=1) if errors else 'none')
        await browser.close()

asyncio.run(main())
