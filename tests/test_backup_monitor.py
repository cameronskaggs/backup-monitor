import unittest
import subprocess
import filecmp

class TestBackupMonitor(unittest.TestCase):

    def test_backup_script(self):
        # Run backup-monitor.py
        subprocess.run(["python3", "backup-monitor.py"])

        self.assertTrue(filecmp.cmp("output/OldNotInNew.txt", "expected_output/OldNotInNew_1.txt"))

        self.assertTrue(filecmp.cmp("output/NewNotInOld.txt", "expected_output/NewNotInOld_1.txt"))

if __name__ == '__main__':
    unittest.main()