import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import time
import unittest

ROOT=Path(__file__).resolve().parents[1]
RUN=ROOT/'skills/python-math/scripts/run_math.py'


class PythonExecutionTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='python-math-test-')
        self.addCleanup(self.temp.cleanup)
        self.base=Path(self.temp.name)
        self.script=self.base/'calculation.py'
        self.logs=self.base/'runs'

    def command(self,*options):
        return [sys.executable,str(RUN),'--python',sys.executable,'--workdir',str(self.base),
                '--log-root',str(self.logs),*options,str(self.script)]

    def status(self):
        paths=list(self.logs.glob('*/run.json'))
        self.assertEqual(len(paths),1)
        return json.loads(paths[0].read_text())

    def test_default_log_root_stays_on_data(self):
        code = (
            'import runpy,sys; '
            'entry=runpy.run_path(sys.argv[1]); print(entry["default_log_root"]())'
        )
        keys = ('MATH_RESEARCH_RUN_DIR', 'TMPDIR', 'TMP', 'TEMP', 'XDG_CACHE_HOME')
        environment = dict(os.environ, **dict.fromkeys(keys, '/private/tmp'))
        result = subprocess.check_output([sys.executable, '-c', code, str(RUN)], text=True, env=environment)
        self.assertEqual(result.strip(), '/Volumes/data/CodexTemp/Math-Research-Skills/python-math-runs')
        environment['TEMP'] = '/Volumes/data/CodexTemp'
        result = subprocess.check_output([sys.executable, '-c', code, str(RUN)], text=True, env=environment)
        self.assertEqual(result.strip(), '/Volumes/data/CodexTemp/python-math-runs')

    def test_exact_calculation_and_process_exit(self):
        self.script.write_text('from fractions import Fraction\nprint(Fraction(1,3)+Fraction(1,6))\n')
        result=subprocess.run(self.command('--require','fractions'),capture_output=True,text=True,timeout=20)
        self.assertEqual(result.returncode,0,result.stderr)
        report=self.status()
        self.assertEqual(report['state'],'succeeded')
        self.assertEqual(Path(report['stdout']).read_text().strip(),'1/2')
        self.assertIn('fractions',report['runtime']['modules'])
        with self.assertRaises(ProcessLookupError): os.kill(report['pid'],0)

    def test_missing_dependency_prevents_user_script(self):
        marker=self.base/'must-not-exist'
        self.script.write_text('from pathlib import Path\nPath('+repr(str(marker))+').write_text("ran")\n')
        result=subprocess.run(self.command('--require','math_research_deliberately_missing_dependency'),capture_output=True,text=True,timeout=20)
        self.assertEqual(result.returncode,2)
        self.assertIn('No existing environment',result.stderr)
        self.assertFalse(marker.exists())
        self.assertFalse(self.logs.exists())

    def test_script_failure_is_not_success(self):
        self.script.write_text('import sys\nprint("diagnostic",file=sys.stderr)\nsys.exit(7)\n')
        result=subprocess.run(self.command(),capture_output=True,text=True,timeout=20)
        self.assertEqual(result.returncode,7)
        report=self.status()
        self.assertEqual(report['state'],'failed')
        self.assertIn('diagnostic',Path(report['stderr']).read_text())

    def test_timeout_terminates_the_created_process(self):
        self.script.write_text('import time\ntime.sleep(10)\n')
        result=subprocess.run(self.command('--timeout','0.2'),capture_output=True,text=True,timeout=10)
        self.assertEqual(result.returncode,124,result.stderr)
        report=self.status()
        self.assertEqual(report['state'],'timed-out')
        with self.assertRaises(ProcessLookupError): os.kill(report['pid'],0)

    def test_cancel_terminates_the_created_process(self):
        self.script.write_text('import time\ntime.sleep(10)\n')
        process=subprocess.Popen(self.command(),stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        try:
            deadline=time.monotonic()+10
            report=None
            while time.monotonic()<deadline:
                paths=list(self.logs.glob('*/run.json'))
                if paths:
                    try: report=json.loads(paths[0].read_text())
                    except json.JSONDecodeError: report=None
                    if report and report.get('pid'): break
                time.sleep(0.02)
            self.assertIsNotNone(report)
            self.assertIn('pid',report)
            process.send_signal(signal.SIGTERM)
            stdout,stderr=process.communicate(timeout=10)
            self.assertEqual(process.returncode,130,stdout+stderr)
            self.assertEqual(self.status()['state'],'cancelled')
            with self.assertRaises(ProcessLookupError): os.kill(report['pid'],0)
        finally:
            if process.poll() is None:
                process.kill();process.wait()


if __name__=='__main__': unittest.main()
