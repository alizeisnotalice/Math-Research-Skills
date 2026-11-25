#!/usr/bin/env python3
"""Validate the maintained public subset, not the mathematics in source packs."""
from __future__ import annotations
import ast
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote
import yaml
from rebuild_catalog import ALIASES, RUNTIME_SKILLS, frontmatter
from skill_common import load_repository

ROOT=Path(__file__).resolve().parents[1]


def visible_markdown(text):
    text=re.sub(r'```.*?```|~~~.*?~~~','',text,flags=re.S)
    text=re.sub(r'`[^`]*`','',text)
    return re.sub(r'\$\$.*?\$\$|(?<!\\)\$[^$\n]+\$|\\\[.*?\\\]|\\\(.*?\\\)','',text,flags=re.S)


def main():
    errors=[]
    try:
        catalog,files=load_repository(ROOT)
    except (OSError,ValueError,KeyError) as exc:
        print(str(exc),file=sys.stderr)
        return 1
    names={s['name'] for s in catalog['skills']}
    if len(names)!=len(catalog['skills']): errors.append('duplicate skill names')
    for skill in catalog['skills']:
        path=ROOT/skill['path']
        data,body=frontmatter(path)
        name=data.get('name')
        description=data.get('description')
        if name!=path.parent.name or not isinstance(name,str) or len(name)>64 or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',name):
            errors.append('invalid name: '+str(path.relative_to(ROOT)))
        if not isinstance(description,str) or not description.strip() or len(description)>1024 or '<' in description or '>' in description:
            errors.append('invalid description: '+str(path.relative_to(ROOT)))
        if set(data)-{'name','description','license','allowed-tools','metadata'}:
            errors.append('unsupported frontmatter: '+str(path.relative_to(ROOT)))
        if description!=skill['description'] and description.strip()!=skill['description']:
            errors.append('stale catalog description: '+name)
        if re.search(r'^\s*\[TODO:[^\n]*\]\s*$',body,re.M):
            errors.append('unfinished skill scaffold: '+name)
        dependencies = skill.get('requires', [])
        if dependencies != RUNTIME_SKILLS.get(name, []) or any(dep not in names for dep in dependencies):
            errors.append('stale or missing runtime dependency: '+name)
        config=path.parent/'agents/openai.yaml'
        if config.exists():
            metadata=yaml.safe_load(config.read_text())
            if not isinstance(metadata,dict): errors.append('invalid openai.yaml: '+name)
    for alias,target in ALIASES.items():
        if alias not in names or target not in names: errors.append('missing compatibility route: '+alias)
        elif f'../{target}/SKILL.md' not in (ROOT/'skills'/alias/'SKILL.md').read_text():
            errors.append('compatibility entry does not link its target: '+alias)
    local_links=0
    for path in sorted(ROOT.rglob('*')):
        relative=path.relative_to(ROOT)
        if relative.parts[0] in {'.git','.local'} or '__pycache__' in relative.parts or not path.is_file(): continue
        if path.is_symlink(): errors.append('public symlink: '+str(relative));continue
        if path.stat().st_size>10*1024*1024: errors.append('public file exceeds 10 MiB: '+str(relative))
        if path.suffix.lower() in {'.pdf','.zip','.gz','.tar','.tgz','.png','.jpg','.jpeg','.pcm','.swiftmodule','.pyc'}:
            errors.append('excluded asset entered public package: '+str(relative))
        if any(p in {'__pycache__','.swift-cache','swift-cache','.cache'} for p in relative.parts):
            errors.append('cache in public package: '+str(relative))
        try: text=path.read_text(encoding='utf-8')
        except UnicodeError:
            errors.append('unexpected binary/non-UTF8 public file: '+str(relative));continue
        if re.search(r'gh[pousr]_[A-Za-z0-9]{30,}|sk-(?:proj-)?[A-Za-z0-9_-]{32,}|-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----',text):
            errors.append('credential-like content: '+str(relative))
        if path.suffix=='.py':
            try: ast.parse(text,filename=str(relative))
            except SyntaxError as exc: errors.append(f'Python syntax error: {relative}: {exc}')
        if path.suffix!='.md': continue
        for raw in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)',visible_markdown(text)):
            raw=unquote(raw.split('#',1)[0].split(' "',1)[0].strip('<>'))
            if not raw or raw=='…' or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',raw) or raw.startswith(('/', '~','$')) or any(c in raw for c in ['<','>','*']): continue
            target=(path.parent/raw).resolve()
            if not target.exists() and '/' not in raw and not Path(raw).suffix: continue
            if ROOT not in target.parents and target!=ROOT:
                errors.append('undeclared external relative link: '+str(relative)+' -> '+raw)
            elif not target.exists(): errors.append('broken local link: '+str(relative)+' -> '+raw)
            else: local_links+=1
    legacy=json.loads((ROOT/'provenance/math-research-migration.json').read_text())
    if len(legacy['skills'])!=64: errors.append('legacy migration must include all 64 methods')
    for skill in legacy['skills']:
        if skill['skill'] not in names: errors.append('legacy skill missing: '+skill['skill'])
        for entry in skill['files']:
            if not entry['installed_source_sha256'] or not entry['public_path'] or not (ROOT/entry['public_path']).is_file():
                errors.append('legacy file not represented: '+skill['skill']+'/'+entry['path'])
    print(json.dumps({'skills':len(names),'managed_files':len(files),'local_links':local_links,
                      'mathematics_reverified':False,'errors':errors},ensure_ascii=False,indent=2))
    return 1 if errors else 0


if __name__=='__main__': raise SystemExit(main())
