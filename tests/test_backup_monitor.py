import unittest
import subprocess
import filecmp

class TestBackupMonitor(unittest.TestCase):

    def test_backup_script(self):

        subprocess.run(["python3", "backup-monitor.py", "-o", "input/Old.sha1.txt", "-n", "input/New.sha1.txt"])
        self.assertTrue(filecmp.cmp("OldNotInNew.txt", "expected_output/OldNotInNew_1.txt"))
        self.assertTrue(filecmp.cmp("NewNotInOld.txt", "expected_output/NewNotInOld_1.txt"))

        subprocess.run(["python3", "backup-monitor.py", "-o" "input/Old-load-test.sha1.txt", "-n", "input/New-load-test.sha1.txt", "-or", "LoadOldNotInNew.txt", "-nr", "LoadNewNotInOld.txt"])
        self.assertTrue(filecmp.cmp("LoadOldNotInNew.txt", "expected_output/OldNotInNew_load.txt"))
        self.assertTrue(filecmp.cmp("LoadNewNotInOld.txt", "expected_output/NewNotInOld_load.txt"))
    
if __name__ == '__main__':
    unittest.main()