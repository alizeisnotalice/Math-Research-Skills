import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
INSTALL=ROOT/'scripts/install_skills.py'


class InstallationTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='math-skill-install-')
        self.addCleanup(self.temp.cleanup)
        self.base=Path(self.temp.name)
        self.repo=self.base/'repo'
        self.target=self.base/'installed'
        (self.repo/'catalog').mkdir(parents=True)
        contents={'skills/demo-math/SKILL.md':b'new instructions\n',
                  'skills/demo-math/references/method.md':b'public reference\n'}
        rows=[]
        for name,data in contents.items():
            path=self.repo/name;path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(data)
            rows.append({'path':name,'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'mode':0o644})
        (self.repo/'catalog/skills.json').write_text(json.dumps({'skills':[{'name':'demo-math'}]}))
        (self.repo/'catalog/skill-files.json').write_text(json.dumps({'files':rows}))
        self.old=self.target/'demo-math/SKILL.md'
        self.old.parent.mkdir(parents=True)
        self.old.write_text('old instructions\n')
        self.evidence=self.target/'demo-math/evidence/untouched.bin'
        self.evidence.parent.mkdir()
        self.evidence.write_bytes(b'local evidence must survive')

    def call(self,*arguments,expect=0):
        result=subprocess.run([sys.executable,str(INSTALL),'--repo',str(self.repo),
                               '--target',str(self.target),*arguments],capture_output=True,text=True)
        self.assertEqual(result.returncode,expect,result.stdout+result.stderr)
        return json.loads(result.stdout if expect==0 else result.stderr)

    def test_dry_run_does_not_mutate(self):
        result=self.call()
        self.assertEqual(result['changed_files'],2)
        self.assertEqual(self.old.read_text(),'old instructions\n')
        self.assertFalse((self.repo/'.local').exists())
        self.assertFalse((self.target/'demo-math/references').exists())

    def test_backup_restore_and_preserve_evidence(self):
        result=self.call('--apply')
        journal=Path(result['journal'])
        backup=journal.parent/'files/skills/demo-math/SKILL.md'
        self.assertEqual(backup.read_text(),'old instructions\n')
        self.assertEqual(self.old.read_text(),'new instructions\n')
        self.assertEqual(self.evidence.read_bytes(),b'local evidence must survive')
        self.call('--restore',str(journal))
        self.assertEqual(self.old.read_text(),'new instructions\n')
        self.call('--restore',str(journal),'--apply')
        self.assertEqual(self.old.read_text(),'old instructions\n')
        self.assertFalse((self.target/'demo-math/references/method.md').exists())
        self.assertEqual(self.evidence.read_bytes(),b'local evidence must survive')
        self.assertEqual(self.call('--restore',str(journal),'--apply')['files'],0)

    def test_reinstall_is_idempotent(self):
        self.call('--apply')
        modified=self.old.stat().st_mtime_ns
        result=self.call('--apply')
        self.assertEqual(result['changed_files'],0)
        self.assertNotIn('journal',result)
        self.assertEqual(self.old.stat().st_mtime_ns,modified)

    def test_restore_refuses_later_edits(self):
        journal=self.call('--apply')['journal']
        self.old.write_text('later user edit\n')
        result=self.call('--restore',journal,'--apply',expect=2)
        self.assertIn('later edits',result['error'])
        self.assertEqual(self.old.read_text(),'later user edit\n')
        self.assertTrue((self.target/'demo-math/references/method.md').exists())

    def test_symlink_is_rejected_before_any_writes(self):
        outside=self.base/'outside';outside.mkdir()
        (self.target/'demo-math/references').symlink_to(outside,target_is_directory=True)
        result=self.call('--apply',expect=2)
        self.assertIn('symlink',result['error'])
        self.assertEqual(self.old.read_text(),'old instructions\n')
        self.assertFalse((outside/'method.md').exists())

    def test_manifest_path_escape_is_rejected(self):
        (self.repo/'catalog/skill-files.json').write_text(json.dumps({'files':[{
            'path':'skills/demo-math/../../../escape','sha256':'0'*64,'bytes':0,'mode':0o644}]}))
        self.assertIn('unsafe manifest path',self.call('--apply',expect=2)['error'])
        self.assertEqual(self.old.read_text(),'old instructions\n')


if __name__=='__main__': unittest.main()
