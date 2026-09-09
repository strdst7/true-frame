#!/usr/bin/env python3
"""Build script: inlines optimized images into template.html as base64 data URIs.
Usage: python3 build.py   (expects ./web/*.jpg and ./template.html)"""
import base64, os

KEYS = {
    'face':           'web/face.jpg',
    'face-plastic':   'web/face-plastic.jpg',
    'hero-real':      'web/hero-real.jpg',
    'hero-plastic':   'web/hero-plastic.jpg',
    'man-real':       'web/model-man-real.jpg',
    'man-plastic':    'web/model-man-plastic.jpg',
    'fashion-real':   'web/fashion-real.jpg',
    'fashion-plastic':'web/fashion-plastic.jpg',
    'eye':            'web/eye-macro.jpg',
    'senior':         'web/gallery-senior.jpg',
}

entries = []
for key, path in KEYS.items():
    with open(path, 'rb') as f:
        b64 = base64.b64encode(f.read()).decode()
    entries.append(f"'{key}': \"data:image/jpeg;base64,{b64}\",")

block = '\n'.join(entries)

with open('template.html', 'r', encoding='utf-8') as f:
    html = f.read()

assert '/*__IMAGES__*/' in html, 'placeholder missing'
html = html.replace('/*__IMAGES__*/', '\n' + block + '\n')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'index.html written: {os.path.getsize("index.html")/1024/1024:.2f} MB')
