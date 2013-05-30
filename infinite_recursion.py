#
# infinite_recursion.py
#

import sys

def recursion_depth(number):
    print "Recursion depth number %d." % number
    try:
        recursion_depth(number + 1)
    except:
        print "Maximum recursion depth exceeded."

sys.setrecursionlimit(200)

recursion_depth(0)
