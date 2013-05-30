def num_digits(n):
    """
      >>> num_digits(12345)
      5
      >>> num_digits(0)
      1
      >>> num_digits(-12345)
      5
    """
    if n == 0:
        return 1
    count = 0
    while abs(n):
        count += 1
        n = abs(n) / 10
    return count
        

def num_even_digits(n):
    """
      >>> num_even_digits(123456)
      3
      >>> num_even_digits(2468)
      4
      >>> num_even_digits(1357)
      0
      >>> num_even_digits(2)
      1
      >>> num_even_digits(20)
      2
    """
    count = 0
    while n:
        digit = n % 10
        if digit == 0 or digit == 2 or digit == 4 or digit == 6 or digit == 8:
            count += 1
        n /= 10
    return count

def print_digits(n):
    """
      >>> print_digits(13789)
      9 8 7 3 1
      >>> print_digits(39874613)
      3 1 6 4 7 8 9 3
      >>> print_digits(213141)
      1 4 1 3 1 2
    """
    while n:
        print n % 10,
        n /= 10

def sum_of_squares_of_digits(n):
    """
      >>> sum_of_squares_of_digits(1)
      1
      >>> sum_of_squares_of_digits(9)
      81
      >>> sum_of_squares_of_digits(11)
      2
      >>> sum_of_squares_of_digits(121)
      6
      >>> sum_of_squares_of_digits(987)
      194
    """
    sum = 0
    while n:
        digit = n % 10
        sum += digit**2
        n /= 10
    return sum
        

if __name__ == '__main__':
    import doctest
    doctest.testmod()
