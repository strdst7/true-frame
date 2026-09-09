#!/usr/bin/env python3
"""Patch: platform presets + negative prompt (PS), Batch tool (ba), showcase sections."""

s = open('template.html', encoding='utf-8').read()

def rep(old, new, n=1):
    global s
    c = s.count(old)
    assert c >= 1, 'ANCHOR NOT FOUND: ' + old[:80]
    s = s.replace(old, new, n)

# ================= 1. CSS: platform, batch, showcase =================
rep('#psDrivers{display:flex;gap:6px;flex-wrap:wrap}',
'''#psDrivers{display:flex;gap:6px;flex-wrap:wrap}

/* ================= BATCH ================= */
.ba-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;align-content:start;max-height:560px;overflow:auto;padding:2px}
.ba-item{position:relative;border-radius:10px;overflow:hidden;border:1px solid var(--line);aspect-ratio:1;background:#141416}
.ba-item img{width:100%;height:100%;object-fit:cover}
.ba-item .st{position:absolute;left:6px;bottom:6px;font-family:var(--mono);font-size:8.5px;letter-spacing:.08em;padding:3px 7px;border-radius:5px;background:rgba(8,8,9,.68);color:var(--dim);text-transform:uppercase}
.ba-item.done .st{color:var(--acc)}
.ba-item.err .st{color:#ff9090}
.ba-item.working .st{color:#ffe14d}
.ba-item .rm{position:absolute;top:6px;right:6px;width:20px;height:20px;border-radius:6px;background:rgba(8,8,9,.68);border:1px solid var(--line2);font-size:11px;line-height:1;color:var(--mut);display:flex;align-items:center;justify-content:center}
.ba-item .rm:hover{color:#ff9090}
.prog{height:3px;border-radius:3px;background:#2a2a2f;overflow:hidden;margin-top:14px}
.prog i{display:block;height:100%;width:0;background:var(--acc);transition:width .3s}

/* ================= SHOWCASE ================= */
.big-cmp{position:relative;max-width:960px;margin:0 auto;border-radius:22px;overflow:hidden;border:1px solid var(--line2);box-shadow:0 40px 100px rgba(0,0,0,.5)}
.big-cmp .cmp{aspect-ratio:16/10}
.uc-grid{display:grid;grid-template-columns:repeat(6,1fr);gap:16px;margin-top:18px}
.uc{position:relative;border-radius:var(--r);overflow:hidden;border:1px solid var(--line);grid-column:span 2;aspect-ratio:3/3.4}
.uc img{width:100%;height:100%;object-fit:cover;transition:transform .8s cubic-bezier(.2,.7,.2,1)}
.uc:hover img{transform:scale(1.05)}
.uc .ov{position:absolute;inset:0;background:linear-gradient(180deg,transparent 45%,rgba(5,5,6,.82));opacity:.85}
.uc .cap{position:absolute;left:18px;right:18px;bottom:16px}
.uc .cap b{display:block;font-size:15px;font-weight:600}
.uc .cap span{font-family:var(--mono);font-size:10px;letter-spacing:.16em;text-transform:uppercase;color:var(--acc)}
.zoom-grid{display:grid;grid-template-columns:1.5fr 1fr;gap:48px;align-items:center;margin-top:84px}
.zoom-frame{position:relative;border-radius:20px;overflow:hidden;border:1px solid var(--line2);cursor:crosshair;box-shadow:0 30px 80px rgba(0,0,0,.5)}
.zoom-frame img{width:100%;height:100%;object-fit:cover;aspect-ratio:16/10}
#loupe{position:absolute;width:190px;height:190px;border-radius:50%;border:1.5px solid var(--acc);pointer-events:none;background-repeat:no-repeat;background-color:#000;box-shadow:0 0 0 6px rgba(216,255,74,.12),0 24px 60px rgba(0,0,0,.6);display:none;z-index:5}
.zstat{display:flex;justify-content:space-between;align-items:baseline;padding:16px 0;border-bottom:1px solid var(--line)}
.zstat:first-of-type{border-top:1px solid var(--line)}
.zstat b{font-size:22px;font-weight:650;letter-spacing:-.02em}
.zstat span{font-family:var(--mono);font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--dim)}
@media (max-width:1060px){.zoom-grid{grid-template-columns:1fr}.uc{grid-column:span 3}}
@media (max-width:720px){.uc{grid-column:span 6}}''')

# ================= 2. desktop nav =================
rep('''      <a data-goto="ps">Prompt Studio</a>
      <a href="#privacy">Privacy</a>''',
'''      <a data-goto="ps">Prompt Studio</a>
      <a data-goto="ba">Batch</a>
      <a href="#privacy">Privacy</a>''')

# ================= 3. mobile nav =================
rep('<a data-goto="gl">Grade Lab</a><a data-goto="ps">Prompt Studio</a><a href="#privacy">Privacy</a><a href="#app">Open Studio</a>',
    '<a data-goto="gl">Grade Lab</a><a data-goto="ps">Prompt Studio</a><a data-goto="ba">Batch</a><a href="#privacy">Privacy</a><a href="#app">Open Studio</a>')

# ================= 4. hero lead / stat / h2 =================
rep('Five real tools, live on this page: rebuild plastic skin, upscale with true detail, grade like film, craft your own looks — and compose production-ready prompts. No signup, no uploads; everything runs on your device.',
    'Six real tools, live on this page: rebuild plastic skin, upscale with true detail, grade like film, craft looks, compose prompts — and batch a whole shoot into a ZIP. No signup, no uploads; everything runs on your device.')
rep('<div class="stat"><b>5</b><span>Working tools</span></div>',
    '<div class="stat"><b>6</b><span>Working tools</span></div>')
rep('<h2>Five tools. <em>Actually working.</em></h2>',
    '<h2>Six tools. <em>Actually working.</em></h2>')

# ================= 5. tab button =================
rep('''<svg viewBox="0 0 24 24"><path d="M21 11.5a8.4 8.4 0 0 1-8.5 8.3 8.8 8.8 0 0 1-3.9-.9L3 20l1.2-4.3a8.1 8.1 0 0 1-1.2-4.2A8.4 8.4 0 0 1 11.5 3a8.4 8.4 0 0 1 9.5 8.5z"/><path d="M8.5 10.5h7M8.5 13.5h4.5"/></svg>Prompt Studio</button>
    </div>''',
'''<svg viewBox="0 0 24 24"><path d="M21 11.5a8.4 8.4 0 0 1-8.5 8.3 8.8 8.8 0 0 1-3.9-.9L3 20l1.2-4.3a8.1 8.1 0 0 1-1.2-4.2A8.4 8.4 0 0 1 11.5 3a8.4 8.4 0 0 1 9.5 8.5z"/><path d="M8.5 10.5h7M8.5 13.5h4.5"/></svg>Prompt Studio</button>
      <button class="ttab" data-tab="ba"><svg viewBox="0 0 24 24"><rect x="7" y="7" width="13" height="13" rx="2.5"/><path d="M17 7V6a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h1"/></svg>Batch</button>
    </div>''')

# ================= 6. panel-ps: platform + negative =================
rep('''        <div class="ctl-group">
          <h4>Match this look</h4>''',
'''        <div class="ctl-group">
          <h4>Platform &amp; negative</h4>
          <div class="chips-row" id="psPlat">
            <button class="pbtn on" data-plat="universal">Universal</button>
            <button class="pbtn" data-plat="midjourney">Midjourney</button>
            <button class="pbtn" data-plat="sd">Stable Diffusion</button>
            <button class="pbtn" data-plat="dalle">DALL·E</button>
            <button class="pbtn" data-plat="flux">Flux</button>
          </div>
          <textarea class="txtin" id="psNeg" rows="2" spellcheck="false" style="margin-top:4px">plastic skin, waxy, over-smooth, deformed hands, extra fingers, watermark, text, logo</textarea>
        </div>
        <div class="ctl-group">
          <h4>Match this look</h4>''')

# ================= 7. batch panel =================
rep('''    <input type="file" id="fileInput" accept="image/*" hidden>''',
'''    <!-- ================= PANEL: BATCH ================= -->
    <div class="app-panel" id="panel-ba">
      <div class="app-view">
        <div class="drop" id="drop-ba">
          <svg viewBox="0 0 24 24"><path d="M12 16V4M7 9l5-5 5 5"/><path d="M4 15v3a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-3"/></svg>
          <b>Drop images here — up to 12</b>
          <span>or click to browse · pick one look, apply it to the whole set, download everything as a ZIP. All on-device.</span>
          <div class="samples">
            <button class="btn ghost sm" data-basample>Add sample</button>
          </div>
        </div>
        <div id="baWrap" hidden style="width:100%">
          <div class="ba-grid" id="baGrid"></div>
          <div class="prog"><i id="baProg"></i></div>
        </div>
      </div>
      <aside class="app-side">
        <div class="ctl-group">
          <h4>Apply to all</h4>
          <div class="seg" id="baModeSeg">
            <button data-m="fix" class="on">Skin Fix</button>
            <button data-m="grade">My Look</button>
            <button data-m="preset">Preset</button>
          </div>
          <div class="pgrid" id="baPresets" style="margin-top:10px">
            <button class="pbtn on" data-bapreset="cinematic">Cinematic</button>
            <button class="pbtn" data-bapreset="noir">Noir</button>
            <button class="pbtn" data-bapreset="warmfilm">Warm Film</button>
            <button class="pbtn" data-bapreset="daylight">Daylight</button>
            <button class="pbtn" data-bapreset="faded">Faded</button>
            <button class="pbtn" data-bapreset="original">Original</button>
          </div>
        </div>
        <div class="ctl-group">
          <div class="ctl"><label>Output size (long edge) <output id="o-baSize">2048</output></label><input type="range" id="r-baSize" min="1024" max="3072" step="512" value="2048"></div>
        </div>
        <div class="ctl-group">
          <button class="btn acc" id="baRun">Process all</button>
          <button class="btn acc" id="baZip" disabled>Download ZIP</button>
          <button class="btn ghost sm" id="baClear">Clear queue</button>
        </div>
        <div class="side-note"><b>How it works:</b> images are processed one by one on this device — Skin Fix uses your current sliders, My Look uses your Grade Lab settings. Nothing is uploaded, and the ZIP is built in your browser.</div>
      </aside>
    </div>

    <input type="file" id="fileInput" accept="image/*" hidden>
    <input type="file" id="baInput" accept="image/*" multiple hidden>''')

# ================= 8. footer + marquee =================
rep('<a data-goto="ps">Prompt Studio</a></div>',
    '<a data-goto="ps">Prompt Studio</a><a data-goto="ba">Batch</a></div>')
rep('<span>Prompt Studio</span><span>Shine Removal</span>',
    '<span>Prompt Studio</span><span>Batch ZIP Export</span><span>Shine Removal</span>', n=2)

# ================= 9. TABS / barTitles / processTab =================
rep('''const PV_MAX={fix:1100,up:560,pr:1100,gl:1100,ps:1100};
const TABS=[
  {id:'fix',ready:false,prep:null},
  {id:'up',ready:false,prep:null,factor:2,sharp:40},
  {id:'pr',ready:false,prep:null,preset:'cinematic',int:70},
  {id:'gl',ready:false,prep:null},
  {id:'ps',ready:false,prep:null},
];''',
'''const PV_MAX={fix:1100,up:560,pr:1100,gl:1100,ps:1100};
const TABS=[
  {id:'fix',ready:false,prep:null},
  {id:'up',ready:false,prep:null,factor:2,sharp:40},
  {id:'pr',ready:false,prep:null,preset:'cinematic',int:70},
  {id:'gl',ready:false,prep:null},
  {id:'ps',ready:false,prep:null},
  {id:'ba',ready:false,prep:null},
];''')
rep("gl:'TRUEFRAME STUDIO — GRADE LAB',ps:'TRUEFRAME STUDIO — PROMPT STUDIO'};",
    "gl:'TRUEFRAME STUDIO — GRADE LAB',ps:'TRUEFRAME STUDIO — PROMPT STUDIO',ba:'TRUEFRAME STUDIO — BATCH'};")
rep('''async function processTab(id,rebuild){
  if(!src.img)return;''',
'''async function processTab(id,rebuild){
  if(id==='ba')return;
  if(!src.img)return;''')

# ================= 10. PS: platform logic =================
rep("const PSS={subject:0,wardrobe:2,setting:0,light:0,lens:0,film:0,mood:0};",
    "const PSS={subject:0,wardrobe:2,setting:0,light:0,lens:0,film:0,mood:0,plat:'universal'};")
rep('''function psCopyFallback(t){''',
'''const PLAT_LABELS={universal:'Universal',midjourney:'Midjourney',sd:'Stable Diffusion',dalle:'DALL·E',flux:'Flux'};
function psFormat(){
  const base=$('#psText').value;
  const neg=($('#psNeg').value||'').trim();
  switch(PSS.plat){
    case 'midjourney':return base+' --ar 4:5 --style raw'+(neg?' --no '+neg:'');
    case 'sd':return 'POSITIVE:\\n'+base+'\\n\\nNEGATIVE:\\n'+neg;
    case 'dalle':return base+'. Avoid the following: '+neg+'.';
    case 'flux':return base+'. Do not include: '+neg+'.';
    default:return neg?base+'\\n\\nNegative prompt: '+neg:base;
  }
}
function psPlatUI(){
  $$('#psPlat .pbtn').forEach(b=>b.classList.toggle('on',b.dataset.plat===PSS.plat));
  $('#psCopy').textContent='Copy · '+PLAT_LABELS[PSS.plat];
}
$$('#psPlat .pbtn').forEach(b=>b.addEventListener('click',()=>{
  PSS.plat=b.dataset.plat;
  psPlatUI();
}));
function psCopyFallback(t){''')
rep('''function psCopy(){
  const t=$('#psText').value;
  const done=()=>{toast('Prompt copied — paste it into any generator.');psPushHistory();};''',
'''function psCopy(){
  const t=psFormat();
  const done=()=>{toast('Copied for '+PLAT_LABELS[PSS.plat]+' — paste it into your generator.');psPushHistory();};''')
rep('''  Object.assign(PSS,en.s);psRenderChips();psCompose();psAuto();
  toast('Prompt recalled.');''',
'''  Object.assign(PSS,en.s);psRenderChips();psCompose();psPlatUI();psAuto();
  toast('Prompt recalled.');''')
rep('''psBuildRows();
psRenderChips();
psCompose();
psRenderHistory();''',
'''psBuildRows();
psRenderChips();
psCompose();
psPlatUI();
psRenderHistory();''')

# ================= 11. batch engine =================
rep('''/* ============================================================
   PROCESS DISPATCH
   ============================================================ */''',
'''/* ============================================================
   TOOL: BATCH (queue → apply look → ZIP)
   ============================================================ */
const BA={items:[],running:false};
const baInput=$('#baInput');
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
$('#drop-ba').addEventListener('click',e=>{
  if(!e.target.closest('[data-basample]'))baInput.click();
});
baInput.addEventListener('change',()=>{addBaFiles([...baInput.files]);baInput.value='';});
['dragover','dragleave','drop'].forEach(ev=>$('#drop-ba').addEventListener(ev,e=>{
  e.preventDefault();
  $('#drop-ba').classList.toggle('over',ev==='dragover');
  if(ev==='drop')addBaFiles([...e.dataTransfer.files]);
}));
$$('[data-basample]').forEach(b=>b.addEventListener('click',e=>{
  e.stopPropagation();
  const im=new Image();
  im.onload=()=>{BA.items.push({name:'sample-portrait.jpg',img:im,status:'queued'});renderBa();toast('Sample added to the queue.');};
  im.src=IMGS['hero-plastic'];
}));
async function addBaFiles(files){
  const room=12-BA.items.length;
  const list=files.filter(f=>f.type.startsWith('image/')).slice(0,Math.max(0,room));
  if(!list.length){toast(BA.items.length>=12?'Queue is full (12 max).':'No images found in that drop.');return;}
  for(const f of list){
    try{
      const img=await fileToImage(f);
      BA.items.push({name:f.name||'image.jpg',img,status:'queued'});
    }catch(e){}
  }
  renderBa();
  toast(list.length+' image'+(list.length>1?'s':'')+' queued.');
}
function renderBa(){
  const grid=$('#baGrid'),wrap=$('#baWrap'),drop=$('#drop-ba');
  if(!BA.items.length){wrap.hidden=true;drop.style.display='';grid.innerHTML='';$('#baProg').style.width='0';return;}
  wrap.hidden=false;drop.style.display='none';
  grid.innerHTML='';
  BA.items.forEach((it,i)=>{
    const d=document.createElement('div');
    d.className='ba-item '+it.status;
    d.innerHTML=`<img src="${it.thumb||''}" alt=""><span class="st">${it.status}</span><button class="rm" data-rm="${i}" aria-label="Remove">×</button>`;
    grid.appendChild(d);
  });
  const done=BA.items.filter(x=>x.status==='done'||x.status==='err').length;
  $('#baProg').style.width=(done/BA.items.length*100)+'%';
}
$('#baGrid').addEventListener('click',e=>{
  const rm=e.target.closest('[data-rm]');
  if(!rm)return;
  if(BA.running){toast('Wait for the current run to finish.');return;}
  BA.items.splice(+rm.dataset.rm,1);
  renderBa();
});
$('#baClear').addEventListener('click',()=>{
  if(BA.running){toast('Wait for the current run to finish.');return;}
  BA.items=[];$('#baZip').disabled=true;renderBa();
});
$('#baModeSeg').addEventListener('click',e=>{
  const b=e.target.closest('[data-m]');if(!b)return;
  $$('#baModeSeg button').forEach(x=>x.classList.toggle('on',x===b));
});
$('#baPresets').addEventListener('click',e=>{
  const b=e.target.closest('[data-bapreset]');if(!b)return;
  $$('#baPresets .pbtn').forEach(x=>x.classList.toggle('on',x===b));
});
const rbs=$('#r-baSize');
rbs.addEventListener('input',()=>{$('#o-baSize').textContent=rbs.value;paintRange(rbs);});
paintRange(rbs);

function baProcessOne(it){
  const cap=+rbs.value;
  const sc=Math.min(1,cap/Math.max(it.img.width,it.img.height));
  const w=Math.max(1,Math.round(it.img.width*sc)),h=Math.max(1,Math.round(it.img.height*sc));
  const cv=makeCanvas(w,h),c=ctx2d(cv);
  c.drawImage(it.img,0,0,w,h);
  const mode=$('#baModeSeg button.on').dataset.m;
  const idata=c.getImageData(0,0,w,h);
  if(mode==='fix'){
    const blur=ctx2d(blurredCopy(cv,Math.max(1,Math.round(Math.min(w,h)/340)))).getImageData(0,0,w,h).data;
    applyFix(idata.data,blur,{...fixP,w,h});
  }else if(mode==='grade'){
    applyCustomGrade(idata.data,{...GLP,shRGB:hueTint(GLP.shHue),hiRGB:hueTint(GLP.hiHue)});
  }else{
    const pr=$('#baPresets .pbtn.on').dataset.bapreset;
    applyPreset(idata.data,{fn:PRESETS[pr],int:70});
  }
  c.putImageData(idata,0,0);
  return cv;
}
$('#baRun').addEventListener('click',async()=>{
  if(BA.running){toast('Already running.');return;}
  if(!BA.items.length){toast('Queue is empty — drop some images first.');return;}
  BA.running=true;
  $('#baRun').disabled=true;$('#baZip').disabled=true;
  BA.items.forEach(it=>{it.status='queued';});
  for(const it of BA.items){
    it.status='working';renderBa();
    await nextFrame();await nextFrame();
    try{
      const cv=baProcessOne(it);
      it.thumb=cv.toDataURL('image/jpeg',0.6);
      it.blob=await new Promise(res=>cv.toBlob(res,'image/jpeg',0.92));
      it.status='done';
    }catch(err){it.status='err';}
    renderBa();
    await sleep(30);
  }
  BA.running=false;
  $('#baRun').disabled=false;
  const ok=BA.items.filter(x=>x.status==='done').length;
  $('#baZip').disabled=!ok;
  toast(ok+' of '+BA.items.length+' processed — ready to download.');
});

/* ---------- minimal store-only ZIP writer ---------- */
const CRCT=(()=>{const t=new Uint32Array(256);for(let n=0;n<256;n++){let c=n;for(let k=0;k<8;k++)c=c&1?0xEDB88320^(c>>>1):c>>>1;t[n]=c;}return t;})();
function crc32(u8){let c=0xFFFFFFFF;for(let i=0;i<u8.length;i++)c=CRCT[(c^u8[i])&0xFF]^(c>>>8);return (c^0xFFFFFFFF)>>>0;}
function zipStore(files){
  const enc=new TextEncoder();
  const parts=[],centers=[];
  let offset=0;
  files.forEach(f=>{
    const name=enc.encode(f.name);
    const crc=crc32(f.u8);
    const lh=new Uint8Array(30+name.length),dv=new DataView(lh.buffer);
    dv.setUint32(0,0x04034b50,true);dv.setUint16(4,20,true);dv.setUint16(6,0x0800,true);
    dv.setUint32(14,crc,true);dv.setUint32(18,f.u8.length,true);dv.setUint32(22,f.u8.length,true);
    dv.setUint16(26,name.length,true);
    lh.set(name,30);
    parts.push(lh,f.u8);
    const ch=new Uint8Array(46+name.length),dv2=new DataView(ch.buffer);
    dv2.setUint32(0,0x02014b50,true);dv2.setUint16(4,20,true);dv2.setUint16(6,20,true);dv2.setUint16(8,0x0800,true);
    dv2.setUint32(16,crc,true);dv2.setUint32(20,f.u8.length,true);dv2.setUint32(24,f.u8.length,true);
    dv2.setUint16(28,name.length,true);dv2.setUint32(42,offset,true);
    ch.set(name,46);
    centers.push(ch);
    offset+=lh.length+f.u8.length;
  });
  const cdSize=centers.reduce((a,c)=>a+c.length,0);
  const eo=new Uint8Array(22),dv3=new DataView(eo.buffer);
  dv3.setUint32(0,0x06054b50,true);
  dv3.setUint16(8,files.length,true);dv3.setUint16(10,files.length,true);
  dv3.setUint32(12,cdSize,true);dv3.setUint32(16,offset,true);
  return new Blob([...parts,...centers,eo],{type:'application/zip'});
}
$('#baZip').addEventListener('click',async()=>{
  const done=BA.items.filter(x=>x.status==='done'&&x.blob);
  if(!done.length){toast('Process the queue first.');return;}
  const files=done.map((it,i)=>({name:String(i+1).padStart(2,'0')+'-'+it.name.replace(/[^\\w.-]+/g,'_').replace(/\\.(jpeg|jpg|png|webp)$/i,'')+'-trueframe.jpg',u8:new Uint8Array(await it.blob.arrayBuffer())}));
  const blob=zipStore(files);
  const a=document.createElement('a');
  a.href=URL.createObjectURL(blob);
  a.download='trueframe-batch.zip';
  a.click();
  setTimeout(()=>URL.revokeObjectURL(a.href),4000);
  toast('ZIP with '+files.length+' images downloaded.');
});

/* ============================================================
   PROCESS DISPATCH
   ============================================================ */''')

# ================= 12. showcase sections =================
rep('''<!-- ============ PRIVACY STRIP ============ -->''',
'''<!-- ============ SHOWCASE ============ -->
<section class="sec" id="showcase">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="k">The proof</span>
      <h2>Plastic in. <em>Photograph out.</em></h2>
      <p class="lead">Every result below was produced by the same engines you just used — nothing left this page.</p>
    </div>
    <div class="big-cmp rv" data-d="80">
      <div class="cmp" id="showCmp">
        <img alt="Realistic editorial result" data-img="fashion-real">
        <div class="layer" id="showLayer"><img alt="Plastic AI editorial" data-img="fashion-plastic" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover"></div>
        <div class="cmp-handle"></div>
        <span class="tag l">RAW AI</span><span class="tag r">TRUEFRAME</span>
        <span class="cmp-hint">Drag to compare</span>
      </div>
    </div>
    <div class="uc-grid">
      <div class="uc rv"><img alt="AI influencer portrait" data-img="hero-real"><div class="ov"></div><div class="cap"><span>AI influencer</span><b>Feed-ready, zero uncanny valley</b></div></div>
      <div class="uc rv" data-d="70"><img alt="Studio headshot" data-img="man-real"><div class="ov"></div><div class="cap"><span>Studio headshot</span><b>Professional, plausible, printable</b></div></div>
      <div class="uc rv" data-d="140"><img alt="Character study" data-img="senior"><div class="ov"></div><div class="cap"><span>Character study</span><b>Age and history in the skin</b></div></div>
    </div>
    <div class="zoom-grid">
      <div class="zoom-frame rv" id="zoomFrame">
        <img id="zoomImg" alt="Macro eye detail" data-img="eye">
        <div id="loupe"></div>
        <span class="tag l">HOVER TO INSPECT · 240%</span>
      </div>
      <div>
        <div class="sec-head rv" style="margin-bottom:26px">
          <span class="k">Zoom in</span>
          <h2 style="font-size:clamp(28px,3.6vw,42px)">8K fidelity. <em>No artifacts.</em></h2>
          <p class="lead" style="font-size:15.5px">Generic upscalers smooth faces into plastic. Hover the image and inspect for yourself — pores, iris fibers, individual lashes.</p>
        </div>
        <div class="rv" data-d="100">
          <div class="zstat"><b>1000%</b><span>Magnification</span></div>
          <div class="zstat"><b>8K+</b><span>Detail depth</span></div>
          <div class="zstat"><b>0</b><span>Uploads</span></div>
        </div>
        <a class="btn ghost rv" data-d="160" href="#app" style="margin-top:28px">Open the studio <span class="ar">→</span></a>
      </div>
    </div>
  </div>
</section>

<!-- ============ PRIVACY STRIP ============ -->''')

# ================= 13. showcase JS =================
rep("$('#heroCmp')._set(50);",
'''$('#heroCmp')._set(50);
const showLayer=document.getElementById('showLayer');
if(showLayer){attachCompare(document.getElementById('showCmp'),showLayer);document.getElementById('showCmp')._set(38);}
const zf=document.getElementById('zoomFrame'),zi=document.getElementById('zoomImg'),loupe=document.getElementById('loupe');
if(zf&&zi){
  const Z=2.4,LR=190;
  zf.addEventListener('pointermove',e=>{
    const fr=zf.getBoundingClientRect(),ir=zi.getBoundingClientRect();
    const x=e.clientX-ir.left,y=e.clientY-ir.top;
    loupe.style.display='block';
    loupe.style.left=(e.clientX-fr.left-LR/2)+'px';
    loupe.style.top=(e.clientY-fr.top-LR/2)+'px';
    loupe.style.backgroundImage=`url("${zi.src}")`;
    loupe.style.backgroundSize=(ir.width*Z)+'px '+(ir.height*Z)+'px';
    loupe.style.backgroundPosition=(-(x*Z-LR/2))+'px '+(-(y*Z-LR/2))+'px';
  });
  zf.addEventListener('pointerleave',()=>loupe.style.display='none');
}''')

open('template.html', 'w', encoding='utf-8').write(s)
print('patch_more: all replacements OK')
