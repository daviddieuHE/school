import unittest
from school import school


class TestDatabase(unittest.TestCase):

    def test_start(self):
        self.assertTrue(school.start())

    def test_generate_profile(self):
        self.assertIsNone(school.generate_profile("David", "Dieu", "21/11/1998"))
        self.assertFalse(school.generate_profile("", "", ""))
        self.assertFalse(school.generate_profile("", "", "21/11/"))


    def test_generate_updated_profile(self):
        self.assertIsNone(school.generate_updated_profile(7, "David", "Dieu", "21/11/1998"))
        self.assertFalse(school.generate_updated_profile("", "", "", ""))
        self.assertFalse(school.generate_updated_profile(7, "David", "Dieu", "21/11/19"))
        self.assertFalse(school.generate_updated_profile("aaaa", "David", "Dieu", "21/11/1998"))

    def test_get_student_name(self):
        self.assertIsNone(school.get_student_name(11))
        self.assertFalse(school.get_student_name(""))
        self.assertFalse(school.get_student_name("aze"))

    def test_show_students_list(self):
        self.assertTrue(school.show_students_list())




if __name__ == '__main__':
    unittest.main()
