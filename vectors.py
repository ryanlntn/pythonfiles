def add_vectors(u, v):
    """
      >>> add_vectors([1, 0], [1, 1])
      [2, 1]
      >>> add_vectors([1, 2], [1, 4])
      [2, 6]
      >>> add_vectors([1, 2, 1], [1, 4, 3])
      [2, 6, 4]
      >>> add_vectors([11, 0, -4, 5], [2, -4, 17, 0])
      [13, -4, 13, 5]
    """
    c = [0] * len(u)
    
    for index in range(len(u)):
        c[index] = u[index] + v[index]

    return c


def mult_vectors(u, v):
    """
      >>> add_vectors([1, 0], [1, 1])
      [1, 0]
      >>> add_vectors([1, 2], [1, 4])
      [1, 8]
      >>> add_vectors([1, 2, 1], [1, 4, 3])
      [1, 8, 3]
      >>> add_vectors([11, 0, -4, 5], [2, -4, 17, 0])
      [22, 0, -68, 0]
    """
    c = [0] * len(u)
    
    for index in range(len(u)):
        c[index] = u[index] * v[index]

    return c
    

def scalar_mult(s, v):
    """
      >>> scalar_mult(5, [1, 2])
      [5, 10]
      >>> scalar_mult(3, [1, 0, -1])
      [3, 0, -3]
      >>> scalar_mult(7, [3, 0, 5, 11, 2])
      [21, 0, 35, 77, 14]
    """
    c = [0] * len(v)

    for index in range(len(v)):
        c[index] = v[index] * s

    return c


def dot_product(u, v):
    """
      >>> dot_product([1, 1], [1, 1])
      2
      >>> dot_product([1, 2], [1, 4])
      9
      >>> dot_product([1, 2, 1], [1, 4, 3])
      12
      >>> dot_product([2, 0, -1, 1], [1, 5, 2, 0])
      0
    """
    c = 0
    d = mult_vectors(u, v)

    for index in range(len(d)):
        c += d[index]

    return c


if __name__ == '__main__':
    import doctest
    doctest.testmod()

