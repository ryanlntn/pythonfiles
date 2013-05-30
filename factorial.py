#
# factorial.py
#

def factorial(n):
    k = 1
    product = n
    if n == 0:
        return 1
    else:
        while n > k:
            product *= (n - k)
            k += 1
        return product
