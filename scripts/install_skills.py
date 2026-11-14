#!/usr/bin/env python3
"""Copy manifest-listed skills without deleting local evidence; dry-run by default."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import shutil
import stat
import sys
import uuid
from skill_common import (assert_storage, atomic_write, digest, load_repository,
                          no_symlinks, skill_path, write_json)


def target_for(root, entry):
    relative = skill_path(entry['path'])
    return no_symlinks(root, Path(*relative.parts[1:]))


def restore(journal_path, apply):
    document = json.loads(journal_path.read_text())
    target = Path(document['target']).resolve()
    assert_storage(target)
    operations = []
    for item in document['operations']:
        dest = target_for(target,item)
        current = digest(dest) if dest.is_file() else None
        if current == item['before_sha256']: continue
        if current != item['sha256']:
            raise ValueError('later edits prevent safe restore: '+str(dest))
        if item['before_sha256'] is not None:
            backup = journal_path.parent/'files'/item['path']
            if not backup.is_file() or digest(backup)!=item['before_sha256']:
                raise ValueError('backup checksum mismatch: '+str(backup))
        operations.append(item)
    if apply:
        for item in reversed(operations):
            dest = target_for(target,item)
            if item['before_sha256'] is None:
                dest.unlink()
            else:
                atomic_write(dest,(journal_path.parent/'files'/item['path']).read_bytes(),item['before_mode'])
        document['state']='restored'
        write_json(journal_path,document)
    return {'mode':'restore' if apply else 'restore-dry-run','files':len(operations),'journal':str(journal_path)}


def install(repo, target, names, apply, backup_root):
    catalog, files = load_repository(repo)
    available = {s['name']:s for s in catalog['skills']}
    selected = set(names) if names else set(available)
    unknown = selected-set(available)
    if unknown: raise ValueError('unknown skills: '+', '.join(sorted(unknown)))
    for name in list(selected):
        if available[name].get('alias_for'): selected.add(available[name]['alias_for'])
    if 'math-research' in available: selected.add('math-research')
    target = target.expanduser().resolve()
    assert_storage(target)
    operations=[]
    selected_files=[item for item in files if skill_path(item['path']).parts[1] in selected]
    for item in selected_files:
        dest=target_for(target,item)
        if dest.exists() and not dest.is_file(): raise ValueError('target is not a file: '+str(dest))
        current=digest(dest) if dest.is_file() else None
        if current==item['sha256']: continue
        operations.append({**item,'before_sha256':current,
                           'before_mode':stat.S_IMODE(dest.stat().st_mode) if dest.exists() else None})
    summary={'mode':'apply' if apply else 'dry-run','target':str(target),'skills':len(selected),
             'checked_files':len(selected_files),'changed_files':len(operations),
             'unchanged_files':len(selected_files)-len(operations),
             'bytes_to_write':sum(i['bytes'] for i in operations),'deletes':0}
    if not apply or not operations: return summary
    backup_root=(backup_root or repo/'.local/install-backups').expanduser().absolute()
    assert_storage(backup_root)
    backup_root.mkdir(parents=True,exist_ok=True)
    backup_root=backup_root.resolve()
    assert_storage(backup_root)
    journal_dir=backup_root/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid.uuid4().hex[:8])
    journal_dir.mkdir()
    for item in operations:
        dest=target_for(target,item)
        if item['before_sha256'] is not None:
            backup=journal_dir/'files'/item['path']
            backup.parent.mkdir(parents=True,exist_ok=True)
            shutil.copy2(dest,backup)
            if digest(backup)!=item['before_sha256']: raise ValueError('target changed while preparing backup: '+str(dest))
    journal={'schema_version':1,'state':'prepared','target':str(target),'operations':operations}
    journal_path=journal_dir/'journal.json'
    write_json(journal_path,journal)
    for item in operations:
        dest=target_for(target,item)
        current=digest(dest) if dest.is_file() else None
        if current!=item['before_sha256']: raise ValueError('target changed before write: '+str(dest))
        source=repo/item['path']
        if digest(source)!=item['sha256']: raise ValueError('source changed before write: '+str(source))
        atomic_write(dest,source.read_bytes(),item['before_mode'] if item['before_mode'] is not None else item['mode'])
        item['written']=True
        journal['state']='applying'
        write_json(journal_path,journal)
    for item in selected_files:
        dest=target_for(target,item)
        if not dest.is_file() or digest(dest)!=item['sha256']:
            raise ValueError('post-install verification failed: '+str(dest))
    journal['state']='verified'
    write_json(journal_path,journal)
    summary['journal']=str(journal_path)
    summary['verified_files']=len(selected_files)
    return summary


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[1])
    codex_root=Path(os.environ.get('CODEX_HOME',str(Path.home()/'.codex')))
    parser.add_argument('--target',type=Path,default=codex_root/'skills')
    parser.add_argument('--skill',action='append',default=[])
    parser.add_argument('--apply',action='store_true')
    parser.add_argument('--backup-root',type=Path)
    parser.add_argument('--restore',type=Path,metavar='JOURNAL')
    args=parser.parse_args(argv)
    try:
        result=restore(args.restore.expanduser().resolve(),args.apply) if args.restore else install(args.repo.resolve(),args.target,args.skill,args.apply,args.backup_root)
        print(json.dumps(result,ensure_ascii=False,indent=2))
        return 0
    except (OSError,ValueError,KeyError) as exc:
        print(json.dumps({'error':str(exc)},ensure_ascii=False),file=sys.stderr)
        return 2


if __name__=='__main__': raise SystemExit(main())
