import unittest
from converter import *

class TestRomanConversion(unittest.TestCase):
    def test_convert_to_roman(self):
        self.assertEqual(convert_to_roman(8), "VIII") 
        self.assertEqual(convert_to_roman(2021), "MMXXI")  

    def test_convert_to_number(self):
        self.assertEqual(convert_to_number("XIV"), 14)  
        self.assertEqual(convert_to_number("XVVIII"), 'errror')  

if __name__ == '__main__':
    unittest.main()
