import unittest
from roman import *

class RomanTests(unittest.TestCase):

  # test to_roman function

  def test_toroman_less_ten(self):
    self.assertEqual(num_to_roman(5),'V')
    self.assertEqual(num_to_roman(9),'IX')
    self.assertEqual(num_to_roman(3),'III')
    self.assertEqual(num_to_roman(8),'VIII')

  def test_toroman_less_hunderd(self):
    self.assertEqual(num_to_roman(67),'LXVII')
    self.assertEqual(num_to_roman(11),'XI')
    self.assertEqual(num_to_roman(43),'XLIII')

  def test_toroman_less_thousand(self):
    self.assertEqual(num_to_roman(845),'DCCCXLV')
    self.assertEqual(num_to_roman(666),'DCLXVI')
    self.assertEqual(num_to_roman(111),'CXI')
  
  def test_toroman_more_thousand(self):
    self.assertEqual(num_to_roman(1247),'MCCXLVII')
    self.assertEqual(num_to_roman(2785),'MMDCCLXXXV')
    self.assertEqual(num_to_roman(3999),'MMMCMXCIX')


  def test_lower_boundaries(self):
    msg = "this should raise out ouf boundary exception"
    with self.assertRaises(OutOfBoundaryArgument,msg=msg):
      a = num_to_roman(0)
    with self.assertRaises(OutOfBoundaryArgument,msg=msg):
      a = num_to_roman(-10)
  
  def test_upper_boundaries(self):
    msg = "this should raise out ouf boundary exception"
    with self.assertRaises(OutOfBoundaryArgument,msg=msg):
      a = num_to_roman(4000)



  # test to_num function

  def test_tonum_less_ten(self):
    self.assertEqual(roman_to_num('V'),5)
    self.assertEqual(roman_to_num('IX'),9)
    self.assertEqual(roman_to_num('VII'),7)
    self.assertEqual(roman_to_num('VIII'),8)

  def test_tonum_less_hundred(self):
    self.assertEqual(roman_to_num('XIX'),19)
    self.assertEqual(roman_to_num('XL'),40) # check that
    self.assertEqual(roman_to_num('LXIV'),64) # check that
    # ...

  def test_tonum_less_thousand(self):
    self.assertEqual(roman_to_num('CMLVI'),956)
    self.assertEqual(roman_to_num('DXXI'),521)
    self.assertEqual(roman_to_num('DCCIII'),703)
  
  def test_tonum_more_thousand(self):
    self.assertEqual(roman_to_num('MDCCCXCI'),1891)
    self.assertEqual(roman_to_num('MMVII'),2007)
    self.assertEqual(roman_to_num('MMMDCXVIII'),3618)


  def test_illegal_carac(self):
    with self.assertRaises(IllegalRomanCharac):
      a = roman_to_num('B')
      b = roman_to_num('G')
      c = roman_to_num('')
  
  def test_illegal_sequence(self):
    with self.assertRaises(IllegalCharacSequence):
      a = roman_to_num('XIXIX')
    with self.assertRaises(IllegalCharacSequence):
      b = roman_to_num('VX')
    with self.assertRaises(IllegalCharacSequence):
      c = roman_to_num('VIX')
    with self.assertRaises(IllegalCharacSequence):
      d = roman_to_num('CDM')
    with self.assertRaises(IllegalCharacSequence):
      d = roman_to_num('XXXX')
    with self.assertRaises(IllegalCharacSequence):
      d = roman_to_num('LL')
    with self.assertRaises(IllegalCharacSequence):
      d = roman_to_num('IIIM')

if __name__ == '__main__':
    unittest.main()
