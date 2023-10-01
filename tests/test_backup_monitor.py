import unittest
import subprocess
import filecmp

class TestBackupMonitor(unittest.TestCase):

    def test_backup_script(self):

        subprocess.run(["python3", "backup-monitor.py"])
        self.assertTrue(filecmp.cmp("OldNotInNew.txt", "expected_output/OldNotInNew_1.txt"))
        self.assertTrue(filecmp.cmp("NewNotInOld.txt", "expected_output/NewNotInOld_1.txt"))

if __name__ == '__main__':
    unittest.main()