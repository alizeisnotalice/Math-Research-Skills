"""Shared, standard-library-only manifest and file operations."""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import tempfile


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def assert_storage(path):
    path = path.absolute()
    if str(path) == '/Volumes/data' or str(path).startswith('/Volumes/data/'):
        if not Path('/Volumes/data').is_mount():
            raise ValueError('data is not mounted')
    old = Path('/Volumes/data/CodexProjects/T')
    if path == old or old in path.parents:
        raise ValueError('the old T project must remain read-only')


def skill_path(raw):
    path = PurePosixPath(raw)
    if path.is_absolute() or '..' in path.parts or '\\' in raw or len(path.parts) < 3 or path.parts[0] != 'skills':
        raise ValueError('unsafe manifest path: ' + raw)
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', path.parts[1]):
        raise ValueError('invalid skill name in path: ' + raw)
    return path


def no_symlinks(root, relative):
    candidate = root
    for part in Path(relative).parts:
        candidate = candidate / part
        if candidate.is_symlink():
            raise ValueError('refusing to replace a symlink: ' + str(candidate))
    return candidate


def load_repository(root):
    root = root.resolve()
    catalog = json.loads((root/'catalog/skills.json').read_text())
    entries = json.loads((root/'catalog/skill-files.json').read_text())['files']
    names = {item['name'] for item in catalog['skills']}
    seen = set()
    for item in entries:
        relative = skill_path(item['path'])
        if relative.parts[1] not in names or str(relative) in seen:
            raise ValueError('unknown or duplicate manifest entry: ' + str(relative))
        seen.add(str(relative))
        source = no_symlinks(root, str(relative))
        if not source.is_file() or digest(source) != item['sha256']:
            raise ValueError('source checksum mismatch: ' + str(relative))
    actual = {str(p.relative_to(root)) for p in (root/'skills').rglob('*') if p.is_file()}
    if seen != actual:
        raise ValueError('skill-files.json does not match the actual public files; rebuild the catalog')
    return catalog, entries


def atomic_write(path, data, mode=0o644):
    path.parent.mkdir(parents=True,exist_ok=True)
    descriptor, name = tempfile.mkstemp(prefix='.skill-write-',dir=path.parent)
    try:
        with os.fdopen(descriptor,'wb') as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.chmod(name,mode)
        os.replace(name,path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def write_json(path, value):
    atomic_write(path,(json.dumps(value,ensure_ascii=False,indent=2)+'\n').encode())
