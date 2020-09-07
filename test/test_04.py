import sys
sys.path.append('./')
import Trim as trim
import unittest

class TestMode(unittest.TestCase):

    def test_mode(self):
        self.assertEqual(trim.trim_text("ini adalah tulisan yang sangat panjang",8),'ini adal...')
    
    def test_value(self):
        self.assertAlmostEqual(trim.trim_text("ini adalah tulisan yang sangat panjang",8),'ini adal...')
    
    def test_input_value(self):
        self.assertRaises(TypeError,trim.trim_text,1)


if __name__ == "__main__":
    unittest.main()