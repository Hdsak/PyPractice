from name_function import get_formatted_name as gfn
import unittest
class Unittest_name(unittest.TestCase):
    def test_first(self):
        formatted_name=gfn("janis",'joplin')
        self.assertEqual(formatted_name,"Janis Joplin")

unittest.main()