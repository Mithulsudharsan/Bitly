import sys
import unittest
import pandas as pd
import logging

# Configure logging to capture errors for the test runs
logging.basicConfig(
    filename='/Users/mithulsudharsanravikumar/Downloads/bitly/log_files/test_errors.log',  # Specifies the file where errors should be logged
    level=logging.ERROR,         # Sets the logging level to ERROR to capture all errors
    format='%(asctime)s - %(levelname)s - %(message)s',  # Defines the format of the log messages
    datefmt='%Y-%m-%d %H:%M:%S'   # Sets the format for date and time in log messages
)

# Add the directory containing your module to the system path
sys.path.insert(0, '/Users/mithulsudharsanravikumar/Downloads/bitly/src')

from main import extract_hash, format_output, count_clicks

class TestProjectFunctions(unittest.TestCase):
    """Defines test cases for functions used in the project."""

    def test_extract_hash(self):
        """Test the extract_hash function with various URL formats."""
        try:
            # Tests with typical URL containing a hash
            self.assertEqual(extract_hash("http://bit.ly/abc123"), "abc123")
            # Test with URL that includes additional path segments
            self.assertEqual(extract_hash("http://bit.ly/abc123/more"), "more")
            # Test with an empty string to see how function handles it
            self.assertEqual(extract_hash(""), "")
        except Exception as e:
            logging.error(f"Test 'test_extract_hash' failed: {e}")
            raise

    def test_format_output(self):
        """Test the format_output function to ensure it formats data correctly."""
        try:
            # Standard DataFrame input
            df_input = pd.DataFrame({
                'long_url': ['http://example.com', 'http://example.org'],
                'count': [10, 5]
            })
            expected_output = [{'http://example.com': 10}, {'http://example.org': 5}]
            self.assertEqual(format_output(df_input), expected_output)

            # DataFrame with zero count to test function's response to zeros
            df_zero = pd.DataFrame({
                'long_url': ['http://zero.com'],
                'count': [0]
            })
            expected_zero_output = [{'http://zero.com': 0}]
            self.assertEqual(format_output(df_zero), expected_zero_output)
        except Exception as e:
            logging.error(f"Test 'test_format_output' failed: {e}")
            raise

    def test_count_clicks(self):
        """Test the count_clicks function to ensure it correctly counts and sorts URL clicks."""
        try:
            # DataFrame with multiple similar entries to test aggregation
            df_clicks = pd.DataFrame({
                'long_url': ['http://example.com', 'http://example.com', 'http://example.org']
            })
            # Expected result after counting and sorting
            expected_counts = pd.DataFrame({
                'long_url': ['http://example.com', 'http://example.org'],
                'count': [2, 1]
            }).sort_values(by='count', ascending=False).reset_index(drop=True)
            result_counts = count_clicks(df_clicks)
            result_counts = result_counts.sort_values(by='count', ascending=False).reset_index(drop=True)
            # Test if the actual result matches the expected result
            pd.testing.assert_frame_equal(result_counts, expected_counts)
        except Exception as e:
            logging.error(f"Test 'test_count_clicks' failed: {e}")
            raise

# Run the tests and handle any uncaught exceptions
if __name__ == '__main__':
    try:
        unittest.main()
    except Exception as e:
        logging.error(f"Error running unittests: {e}")
        raise
