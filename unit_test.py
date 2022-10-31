import unittest
import warnings
from log_reader import LogReader

warnings.filterwarnings("ignore", category=ResourceWarning)

class TestCase(unittest.TestCase):
    def test_success_output(self):
        # test for success result
        lr = LogReader("success_log.csv")
        self.assertListEqual([' 2', ' 1', ' 4'], lr.csv_reader())
    
    def test_error_output(self):
        # test for error result
        lr = LogReader("err_log.csv")
        with self.assertRaises(Exception):
            lr.csv_reader()


if __name__ == "__main__":
    unittest.main()
