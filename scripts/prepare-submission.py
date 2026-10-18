"""Create a standalone, renamed submission without changing GitHub Pages paths.

Requires Python 3, Node.js and sharp for JPEG conversion. SHARP_MODULE may point
to an existing sharp installation; the website itself needs no dependencies.
"""
import argparse
import base64
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
from urllib.parse import unquote, urlsplit
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--team-number', default='16')
    parser.add_argument('--team-name', default='SMTOWN')
    parser.add_argument('--plan-pdf', type=Path, required=True)
    args = parser.parse_args()
    if not re.fullmatch(r'\d+', args.team_number):
        parser.error('team-number must contain digits only')
    if not re.fullmatch(r'[A-Za-z0-9_-]+', args.team_name):
        parser.error('team-name must be a filename-safe name')
    if not args.plan_pdf.is_file():
        parser.error('plan-pdf must be an existing PDF')

    name = f'{args.team_number}_{args.team_name}'
    parent = ROOT / 'output' / 'submission'
    # Use a fresh directory on every run; never recursively remove prior output.
    destination = parent / name
    number = 2
    while destination.exists():
        destination = parent / f'{name}_{number}'
        number += 1
    destination.mkdir(parents=True)
    pages = sorted(ROOT.glob('*.html'))
    mapping = {p.name: f'{name}_{p.name}' for p in pages}

    image_jobs = []
    for source in sorted((ROOT / 'images').rglob('*')):
        if source.suffix.lower() not in {'.svg', '.png', '.jpg', '.jpeg', '.webp'}:
            continue
        old = source.relative_to(ROOT).as_posix()
        new = (source.relative_to(ROOT).parent / f'{args.team_number}_{source.stem}.jpg').as_posix()
        if new in mapping.values():
            raise ValueError(f'Image filename collision: {new}')
        mapping[old] = new
        target = destination / new
        target.parent.mkdir(parents=True, exist_ok=True)
        image_jobs.append({'source': str(source), 'target': str(target)})

    convert = r'''
const fs = require('fs');
const sharp = require(process.env.SHARP_MODULE || 'sharp');
const jobs = JSON.parse(fs.readFileSync(0, 'utf8'));
(async () => {
  for (const job of jobs) {
    await sharp(job.source, {density: 144})
      .resize({width: 1800, height: 1800, fit: 'inside', withoutEnlargement: true})
      .flatten({background: '#f8f6f2'})
      .jpeg({quality: 94, chromaSubsampling: '4:4:4'})
      .toFile(job.target);
  }
})().catch(error => {console.error(error.message); process.exit(1);});
'''
    subprocess.run(['node', '-e', convert], input=json.dumps(image_jobs), text=True,
                   encoding='utf-8', check=True, env=os.environ.copy())

    # HTML paths in href/src and existing authentication scripts are both mapped.
    # A token matcher avoids replacing part of an unrelated longer filename.
    pattern = re.compile(r'(?<![\w/.-])(' + '|'.join(re.escape(k) for k in sorted(mapping, key=len, reverse=True)) + r')(?![\w.-])')
    for source in pages:
        text = pattern.sub(lambda match: mapping[match.group(1)], source.read_text(encoding='utf-8'))
        (destination / mapping[source.name]).write_text(text, encoding='utf-8', newline='\n')

    # Copy only referenced stylesheets. Embed the unchanged local font bytes in
    # CSS so the ZIP contains HTML, CSS, JPEGs and the PDF only.
    styles = set()
    for page in destination.glob('*.html'):
        styles.update(re.findall(r'href="(css/[^"?#]+\.css)"', page.read_text(encoding='utf-8')))
    for relative in styles:
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        css = (ROOT / relative).read_text(encoding='utf-8')
        if relative == 'css/common.css':
            font = base64.b64encode((ROOT / 'src' / 'fonts' / 'LeeSeoyun.woff').read_bytes()).decode('ascii')
            css = css.replace('../src/fonts/LeeSeoyun.woff', 'data:font/woff;base64,' + font)
            attribution = (ROOT / 'src' / 'fonts' / 'README.md').read_text(encoding='utf-8')
            css = '/*\n' + attribution.replace('*/', '* /') + '\n*/\n' + css
        target.write_text(css, encoding='utf-8', newline='\n')
    shutil.copy2(args.plan_pdf, destination / f'{name}_수행계획서.pdf')

    from html.parser import HTMLParser
    class References(HTMLParser):
        def __init__(self):
            super().__init__()
            self.ids = set()
            self.links = []
        def handle_starttag(self, tag, attrs):
            values = dict(attrs)
            if 'id' in values:
                if values['id'] in self.ids:
                    raise ValueError(f'Duplicate id: {values["id"]}')
                self.ids.add(values['id'])
            self.links.extend(values[k] for k in ['href', 'src'] if k in values)
    parsed = {}
    for page in destination.glob('*.html'):
        content = References()
        content.feed(page.read_text(encoding='utf-8'))
        parsed[page.name] = content
    for filename, content in parsed.items():
        for link in content.links:
            url = urlsplit(link)
            if url.scheme or url.netloc:
                continue
            relative = unquote(url.path) or filename
            if not (destination / relative).is_file():
                raise ValueError(f'Broken submission path in {filename}: {link}')
            if url.fragment and relative in parsed and unquote(url.fragment) not in parsed[relative].ids:
                raise ValueError(f'Broken submission anchor in {filename}: {link}')
    for css in destination.glob('css/*.css'):
        for path in re.findall(r'url\([\'"]?([^\)\'\"]+)', css.read_text(encoding='utf-8')):
            if not urlsplit(path).scheme and not (css.parent / path).is_file():
                raise ValueError(f'Broken CSS asset: {path}')
    archive = destination.with_suffix('.zip')
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as zipped:
        for source in sorted(destination.rglob('*')):
            if source.is_file():
                zipped.write(source, source.relative_to(destination.parent))
    print(json.dumps({'folder': str(destination), 'zip': str(archive),
                      'entry': mapping['index.html'], 'pages': len(pages),
                      'images': len(image_jobs)}, ensure_ascii=True))


if __name__ == '__main__':
    main()
