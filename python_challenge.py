#
# python_challenge.py
#

from string import maketrans

intab = 'cdefghijklmnopqrstuvwxyzab'
outtab = 'abcdefghijklmnopqrstuvwxyz'
trantab = maketrans(intab, outtab)

def decode(s):
    punctuation = " ()'."
    for letter in s:
        if letter not in punctuation:
            print chr(ord(letter) + 2),
        else:
            print letter,
