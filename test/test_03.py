import sys
sys.path.append('./')
import Rating as rating
import unittest

class TestRating(unittest.TestCase):

    def test_count(self):
        self.assertEqual(rating.rating_film(12),'BIMBINGAN ORANG TUA')
    
    def test_value(self):
        self.assertAlmostEqual(rating.rating_film(12),'BIMBINGAN ORANG TUA')
    
    def test_input_value(self):
        self.assertRaises(TypeError,rating.rating_film, 'BIMBINGAN ORANG TUA')

if __name__ == "__main__":
    unittest.main()