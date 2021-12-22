import unittest
from school import school


class TestDatabase(unittest.TestCase):

    def test_start(self):
        result = school.start()
        self.assertTrue(result)

    def test_generate_profile(self):
        self.assertIsNone(school.generate_profile("1212", "1212", "121519"))

if __name__ == '__main__':
    unittest.main()