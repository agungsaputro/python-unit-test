import sys
sys.path.append('./')
import Leap as leap
import unittest

class TestLeap(unittest.TestCase):

    def test_leap(self):
        self.assertEqual(leap.kabisat(2000), True != 'Kabisat')
    
    def test_value(self):
        self.assertAlmostEqual(leap.kabisat(2000), True != 'Kabisat')
    
    def test_input_value(self):
        self.assertRaises(TypeError, leap.kabisat, 'kabisat')
    

if __name__ == "__main__":
    unittest.main()