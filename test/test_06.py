import sys
sys.path.append('./')
import Mode as mode
import unittest

class TestMode(unittest.TestCase):

    def test_mode(self):
        self.assertEqual(mode.most_frequent([1,2,3,4,5,6,6,8,8,6,9]),6)
    
    def test_value(self):
        self.assertAlmostEqual(mode.most_frequent([87.5, 88.5, 60.5, 90.5, 88.5]),88.5)
    
    def test_input_value(self):
        self.assertRaises(TypeError,mode.most_frequent,1)


if __name__ == "__main__":
    unittest.main()