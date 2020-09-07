import sys
sys.path.append('./')
import Count as count
import unittest

class TestCount(unittest.TestCase):

    def test_count(self):
        self.assertEqual(count.count_chars("saya"),4)
    
    def test_input_value(self):
        self.assertRaises(TypeError, count.count_chars,1)

    def test_value(self):
        self.assertAlmostEqual(count.count_chars("saya"),4)
    

if __name__ == "__main__":
    unittest.main()

