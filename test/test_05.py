import sys
sys.path.append('./')
import NumtoWord as num
import unittest

class TestMode(unittest.TestCase):

    def test_mode(self):
        self.assertEqual(num.spell(1),'One')
    
    def test_value(self):
        self.assertAlmostEqual(num.spell(12),'Twelve')
        
    def test_input_value(self):
        self.assertRaises(TypeError,num.spell,'One')


if __name__ == "__main__":
    unittest.main()