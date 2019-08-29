


def num_to_roman(num):
  """
  Convert any number from 1 to 3999 (included) to its roman writing (string)
  num: int (0 < num < 4000)
  result: string
  """
  if num <= 0:
    raise OutOfBoundaryArgument("input number should be greater than 0")
  if num >= 4000:
    raise OutOfBoundaryArgument("input number should be lesser than 4000")
  res = ""

  # more or equal than 1000
  if num >= 1000:
    m = num // 1000
    res += "M" * m
    num = num % 1000  

  # more or equal than 100
  if num >= 100:
    c = num // 100
    if c <= 3:
      res += "C" * c
    elif c == 4:
      res += "CD"
    elif c <= 8:
      res += "D" + "C" * (c-5)
    elif c == 9:
      res += "CM"
    num = num % 100

  
  # decimals
  if num >= 10:
    d = num // 10
    if d <= 3:
      res += "X" * d
    elif d == 4:
      res += "XL"
    elif d <= 8:
      res += "L" + "X" * (d-5)
    else:
      res += "XC"
    num = num % 10

  # units
  if num <= 3:
    res += "I" * num
  elif num == 4:
    res == "IV"
  elif num <= 8:
    res += "V" + "I" * (num-5)
  else:
    res += "IX"
  return res



def roman_to_num(roman):
  return read_dict(roman,0)[1]

def read_dict(roman,count):
  d2={
    'CM': 900,
    'CD': 400,
    'XC': 90,
    'XL': 40,
    'IX': 9,
    'IV': 4
  }
  d1 = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
  }
  r2, r1 = roman[:2], roman[:1]
  if(r2 in d2):
    return read_dict(roman[2:],count + d2[r2])
  elif(r1 in d1):
    return read_dict(roman[1:],count + d1[r1])
  elif len(roman)>0:
    raise IllegalRomanCharac(": "+r1)
  else:
    return ("",count)


def roman_to_num_OLD(roman):
  """
  convert any roman writing to arabic writing. Only covers number from 1 to 3999 (included)
  roman: string representing the roman writing
  result: int
  """
  valid, c = check_valid_charac(roman)
  if not valid:
    raise IllegalRomanCharac("{}: {} is an illegal character for roman numbers".format(roman,c))
  roman_saved = roman
  res = 0

  if roman[:4] != "MMMM": # exception raised at the end
    while roman[0] == "M":
      res += 1000
      roman = roman[1:]

  if len(roman) == 0: # in case there is no decimal / unit
    return res
  elif len(roman) >= 2 and roman[0:2] == "CD":
    res += 400
    roman = roman[2:]
  elif len(roman) >= 2 and roman[0:2] == "CM":
    res += 900
    roman = roman[2:]
  else:
    if roman[0] == "D":
      res += 500
      roman = roman[1:]
    if roman[:4] != "CCCC": # exception raised at the end
      while roman[0] == "C":
        res += 100
        roman = roman[1:]

  if len(roman) == 0: # in case there is no decimal / unit
    return res
  elif len(roman) >= 2 and roman[0:2] == "XL":
    res += 40
    roman = roman[2:]
  elif len(roman) >= 2 and roman[0:2] == "XC":
    res += 90
    roman = roman[2:]
  else:
    if roman[0] == "L":
      res += 50
      roman = roman[1:]
    if roman[:4] != "XXXX": # exception raised at the end
      while len(roman) > 0 and roman[0] == "X":
        res += 10
        roman = roman[1:]

  if len(roman) == 0: # in case there is no unit
    pass
  elif len(roman) == 2 and roman[:2] == "IV":
    res += 4
    roman = roman[2:]
  elif len(roman) == 2 and roman[:2] == "IX":
    res += 9
    roman = roman[2:]
  else:
    if roman[0] == "V":
      res += 5
      roman = roman[1:]
    if roman[:4] != "IIII": # exception raised at the end
      while len(roman) > 0 and roman[0] == "I":
        res += 1
        roman = roman[1:]

  if(len(roman) > 0):
    msg = "Illegal character '{}' in {}".format(roman[0],roman_saved)
    raise IllegalCharacSequence(msg)
  return res


def check_valid_charac(roman):
  """ 
  check if the input roman number contains illegal characters
  input: str representing the number
  returns (bool, c): 
        bool: True if the given roman string does not contain illegal character
        c: illegal character, None if there is none
  """
  legal = "IVXLCDM"
  for c in roman:
    if not (c in legal):
      return (False, c)
  return (True, None)


# Exception classes

class RomanException(Exception):
  """
  interface for all the exceptions used
  """
  def __init__(self, message):
    self.message = message 

class OutOfBoundaryArgument(RomanException):
  """
  raised when the input number (int) is out of bound
  """
  pass

class IllegalCharacSequence(RomanException):
  """
  raised when there is an illegal character in the roman writing (ex: G)
  """
  pass 

class IllegalRomanCharac(RomanException):
  """
  raised when the characters in the roman writing are legal but not in the right order
  """
  pass