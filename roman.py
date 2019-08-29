

p_thousand ={
  'MMM': 3000,
  'MM': 2000,
  'M': 1000
}

p_hundred ={
  'CM': 900,
  'DCCC': 800,
  'DCC': 700,
  'DC': 600,
  'CD': 400,
  'CCC': 300,
  'CC': 200,
  'D': 500,
  'C': 100
}

p_dec ={
  'LXXX': 80,
  'LXX': 70,
  'LX': 60,
  'XC': 90,
  'XL': 40,
  'XXX': 30,
  'XX': 20,
  'L': 50,
  'X': 10
}

p_unit ={
  'IX': 9,
  'VIII': 8,
  'VII': 7,
  'VI': 6,
  'IV': 4,
  'III': 3,
  'II': 2,
  'V': 5,
  'I': 1
}

# This solution work although it is not very elegant
def roman_to_num(roman):
  """
  convert the input roman string to its corresponding arabic writing (as int)
  raise error if the input string does not correspond to a valid roman number
  """
  valid, c = check_valid_charac(roman)
  if not valid:
    raise IllegalRomanCharac('"{}": unvalid roman character'.format(c))
  num = 0
  roman, c = check_dict(roman,p_thousand)
  num += c
  roman, c = check_dict(roman,p_hundred)
  num += c
  roman, c = check_dict(roman,p_dec)
  num += c
  roman, c = check_dict(roman,p_unit)
  num += c
  if(len(roman)>0):
    raise IllegalCharacSequence(roman+": unvalid roman character sequence")
  return num


def check_dict(roman,patterns):
  """
  auxiliary function for roman to num
  take a roman writing and a dictionnary
  look over pattern in the dictionnary, if one is met return the corresponding value and crop the roman writing
  else return 0 (roman unchanged)
  """
  for p, value in patterns.items():
    if p == roman[:len(p)]:
      return (roman[len(p):],value)
  return (roman,0)


# FAIL to IllegalCharacSequence Check
def roman_to_num_V1(roman):
  """
  convert the input roman string to its corresponding arabic writing (as int)
  """
  return read_dict(roman,0)[1]

# auxilary recursive function
def read_dict(roman,count):
  """
  take a roman writing as input
  look over pattern in the dictionnary, if one is met return the corresponding value and crop the roman writing
  """
  patterns ={
    'CM': 900,
    'CD': 400,
    'XC': 90,
    'XL': 40,
    'IX': 9,
    'IV': 4,
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
  }
  for p, add in patterns.items():
    if p == roman[:len(p)]:
      return read_dict(roman[len(p):],count+add)
  if len(roman)>0:
    raise IllegalRomanCharac(roman+": "+roman[:1]+" is illegal charac")
  return ("", count) 


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


def check_valid_charac(roman):
  """ 
  check if the input roman number contains illegal characters
  input: str representing the number
  returns (bool, c): 
        bool: True if the given roman string does not contain illegal character
        c: illegal character, None if there is none
  """
  if len(roman) == 0:
    return (False,"")
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
