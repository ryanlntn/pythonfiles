"""
  >>> type(fruit)
  <type 'str'>
  >>> len(fruit)
  8
  >>> fruit[:3]
  'ram'
"""

fruit = 'rambutan'

"""
  >>> group = "John, Paul, George, and Ringo"
  >>> group[12:x]
  'George'
  >>> group[n:m]
  'Paul'
  >>> group[:r]
  'John'
  >>> group[s:]
  'Ringo'
"""

group = "John, Paul, George, and Ringo"
x = 18
r = 4
n = 6
m = 10
s = 24

"""
  >>> len(s)
  8
  >>> s[4:6] == 'on'
  True
"""

s = 'xxxxonxx'

def jklmnopq():
    prefixes = "JKLMNOPQ"
    suffix = "ack"

    for letter in prefixes[:4]:
        print letter + suffix
    for letter in prefixes[5]:
        print letter + 'u' + suffix
    for letter in prefixes[6]:
        print letter + suffix
    for letter in prefixes[7]:
        print letter + 'u' + suffix

def count_letters(string, letter, start):
    index = start
    count = 0
    while index < len(string):
        if string[index] == letter:
            count += 1
        index += 1
    print count
