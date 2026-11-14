"""Archive a generated image without changing pixels; update project indexes."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
from PIL import Image


def read_json(path, default):
    return json.loads(path.read_text(encoding='utf-8-sig')) if path.exists() else default


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    temporary.replace(path)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', required=True, type=Path)
    parser.add_argument('--source', required=True, type=Path)
    parser.add_argument('--style', required=True)
    parser.add_argument('--name', required=True)
    parser.add_argument('--title', required=True)
    parser.add_argument('--generator', default='built-in image_gen')
    parser.add_argument('--prompt-file', required=True, type=Path)
    parser.add_argument('--reference-file', action='append', default=[], type=Path)
    args = parser.parse_args()
    for key, value in [('style', args.style), ('name', args.name)]:
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', value):
            parser.error(f'{key} must be a lowercase ASCII slug')
    source = args.source.resolve(strict=True)
    prompt = args.prompt_file.read_text(encoding='utf-8-sig')
    if not prompt.strip():
        parser.error('Prompt must not be empty')
    with Image.open(source) as im:
        image_format = im.format
        dimensions = list(im.size)
        im.verify()
    suffixes = {'PNG': '.png', 'JPEG': '.jpg', 'WEBP': '.webp'}
    if image_format not in suffixes:
        parser.error('Expected PNG, JPEG or WebP')
    references = [p.resolve(strict=True) for p in args.reference_file]
    for reference in references:
        with Image.open(reference) as im:
            if im.format not in suffixes:
                parser.error('Expected PNG, JPEG or WebP reference')
            im.verify()
    project = args.project.resolve()
    catalog_path = project / 'catalog.json'
    checks_path = project / 'image-verification.json'
    catalog = read_json(catalog_path, {'name': 'Visual Style Atlas', 'styles': [], 'items': []})
    checks = read_json(checks_path, [])
    if not isinstance(catalog, dict) or not isinstance(catalog.get('styles', []), list) or not isinstance(catalog.get('items', []), list) or not isinstance(checks, list):
        parser.error('Project indexes have an unsupported structure')
    image_folder = {'city-miniature-poster': 'city-miniature-posters'}.get(args.style, args.style)
    image_dir = project / 'images' / image_folder
    prompt_dir = project / 'prompts' / args.style
    image_dir.mkdir(parents=True, exist_ok=True)
    prompt_dir.mkdir(parents=True, exist_ok=True)
    stem = args.name
    version = 1
    while (image_dir / (stem + suffixes[image_format])).exists() or (prompt_dir / (stem + '.json')).exists():
        version += 1
        stem = f'{args.name}-v{version}'
    target = image_dir / (stem + suffixes[image_format])
    prompt_target = prompt_dir / (stem + '.json')
    shutil.copy2(source, target)
    image_digest = digest(source)
    if digest(target) != image_digest:
        raise RuntimeError('Image copy failed checksum verification')
    saved_refs = []
    for reference in references:
        ref_hash = digest(reference)
        with Image.open(reference) as im:
            ref_suffix = suffixes.get(im.format)
        if not ref_suffix:
            raise ValueError('Unsupported reference format')
        ref_target = project / 'styles/references' / f'{args.style}-{ref_hash[:16]}{ref_suffix}'
        ref_target.parent.mkdir(parents=True, exist_ok=True)
        if not ref_target.exists():
            shutil.copy2(reference, ref_target)
        if digest(ref_target) != ref_hash:
            raise RuntimeError('Reference checksum mismatch')
        saved_refs.append(ref_target.relative_to(project).as_posix())
    image_path = target.relative_to(project).as_posix()
    prompt_path = prompt_target.relative_to(project).as_posix()
    write_json(prompt_target, {'title': args.title, 'style': args.style, 'image': image_path, 'generator': args.generator, 'prompt': prompt, 'references': saved_refs})
    entry = {'title': args.title, 'style': args.style, 'image': image_path, 'prompt': prompt_path, 'dimensions': dimensions, 'sha256': image_digest}
    styles = catalog.setdefault('styles', [])
    style = next((item for item in styles if item.get('id') == args.style), None)
    if style is None:
        style = {'id': args.style, 'name': args.style, 'images': []}
        styles.append(style)
    style.setdefault('images', []).append(image_path)
    catalog.setdefault('items', []).append(entry)
    checks.append({'file': image_path, 'dimensions': dimensions, 'sha256': image_digest})
    write_json(catalog_path, catalog)
    write_json(checks_path, checks)
    print(json.dumps(entry, ensure_ascii=True))


if __name__ == '__main__':
    main()
