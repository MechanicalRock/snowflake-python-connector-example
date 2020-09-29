import unittest
from src import snowflake

class DockerCommandsTestCase(unittest.TestCase):
    def test_snowflake_connection(self):
        row_count= snowflake.snowflake_connection()
        assert row_count is 10
