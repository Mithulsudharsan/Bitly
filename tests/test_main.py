import sys
import unittest
import pandas as pd  

sys.path.append('../')

from main import extract_hash, format_output, count_clicks

class TestProjectFunctions(unittest.TestCase):

    def test_extract_hash(self):
        self.assertEqual(extract_hash("http://bit.ly/abc123"), "abc123")

    def test_format_output(self):
        df_input = pd.DataFrame({
            'long_url': ['http://example.com', 'http://example.org'],
            'count': [10, 5]
        })
        expected_output = [{'http://example.com': 10}, {'http://example.org': 5}]
        self.assertEqual(format_output(df_input), expected_output)

if __name__ == '__main__':
    unittest.main()
