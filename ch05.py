def compare(a, b):
    """
      >>> compare(5, 4)
      1
      >>> compare(7, 7)
      0
      >>> compare(2, 3)
      -1
      >>> compare(42, 1)
      1
    """
    #  Your function body should begin here.
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0

def hypotenuse(a, b):
    """
      >>> hypotenuse(3, 4)
      5.0
      >>> hypotenuse(12, 5)
      13.0
      >>> hypotenuse(7, 24)
      25.0
      >>> hypotenuse(9, 12)
      15.0
    """
    return (a**2 + b**2)**0.5
        
def slope(x1, y1, x2, y2):
    """
      >>> slope(5, 3, 4, 2)
      1.0
      >>> slope(1, 2, 3, 2)
      0.0
      >>> slope(1, 2, 3, 3)
      0.5
      >>> slope(2, 4, 1, 2)
      2.0
    """
    return (float(y2) - float(y1))/(float(x2) - float(x1))

def intercept(x1, y1, x2, y2):
    """
      >>> intercept(1, 6, 3, 12)
      3.0
      >>> intercept(6, 1, 1, 6)
      7.0
      >>> intercept(4, 6, 12, 8)
      5.0
    """
    return float(y1) - slope(x1, y1, x2, y2)*float(x1)

def is_even(n):
    """
      >>> is_even(1)
      False
      >>> is_even(2)
      True
      >>> is_even(4)
      True
    """
    return n % 2 == 0

def is_odd(n):
    """
      >>> is_odd(1)
      True
      >>> is_odd(2)
      False
      >>> is_odd(3)
      True
    """
    return is_even(n) == False

def is_factor(f, n):
    """
      >>> is_factor(3, 12)
      True
      >>> is_factor(5, 12)
      False
      >>> is_factor(7, 14)
      True
      >>> is_factor(2, 14)
      True
      >>> is_factor(7, 15)
      False
    """
    return n % f == 0

def is_multiple(m, n):
    """
      >>> is_multiple(12, 3)
      True
      >>> is_multiple(12, 4)
      True
      >>> is_multiple(12, 5)
      False
      >>> is_multiple(12, 6)
      True
      >>> is_multiple(12, 7)
      False
    """
    return is_factor(n, m) == True

def f2c(t):
    """
      >>> f2c(212)
      100
      >>> f2c(32)
      0
      >>> f2c(-40)
      -40
      >>> f2c(36)
      2
      >>> f2c(37)
      3
      >>> f2c(38)
      3
      >>> f2c(39)
      4
    """
    C = (5*(float(t) - 32))/9
    return int(round(C))

def c2f(t):
    """
      >>> c2f(0)
      32
      >>> c2f(100)
      212
      >>> c2f(-40)
      -40
      >>> c2f(12)
      54
      >>> c2f(18)
      64
      >>> c2f(-48)
      -54
    """
    F = (9*float(t))/5 + 32
    return int(round(F))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
