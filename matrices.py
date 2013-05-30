def add_lists(a, b):
    """
      >>> add_lists([1, 1], [1, 1])
      [2, 2]
      >>> add_lists([1, 2], [1, 4])
      [2, 6]
      >>> add_lists([1, 2, 1], [1, 4, 3])
      [2, 6, 4]
    """
    c = [0] * len(a)

    for index in range(len(a)):
        c[index] = a[index] + b[index]

    return c


def add_row(matrix):
    """
      >>> m = [[0, 0], [0, 0]]
      >>> add_row(m)
      [[0, 0], [0, 0], [0, 0]]
      >>> n = [[3, 2, 5], [1, 4, 7]]
      >>> add_row(n)
      [[3, 2, 5], [1, 4, 7], [0, 0, 0]]
      >>> n
      [[3, 2, 5], [1, 4, 7]]
    """
    new_row = [0] * len(matrix[0])
    new_matrix = matrix + [new_row]

    return new_matrix


def add_column(matrix):
    """
      >>> m = [[0, 0], [0, 0]]
      >>> add_column(m)
      [[0, 0, 0], [0, 0, 0]]
      >>> n = [[3, 2], [5, 1], [4, 7]]
      >>> add_column(n)
      [[3, 2, 0], [5, 1, 0], [4, 7, 0]]
      >>> n
      [[3, 2], [5, 1], [4, 7]]
    """
    new_matrix = []

    for row in matrix:
        new_matrix += [row + [0]]

    return new_matrix


def add_matrices(m1, m2):
    """
      >>> a = [[1, 2], [3, 4]]
      >>> b = [[2, 2], [2, 2]]
      >>> add_matrices(a, b)
      [[3, 4], [5, 6]]
      >>> c = [[8, 2], [3, 4], [5, 7]]
      >>> d = [[3, 2], [9, 2], [10, 12]]
      >>> add_matrices(c, d)
      [[11, 4], [12, 6], [15, 19]]
      >>> c
      [[8, 2], [3, 4], [5, 7]]
      >>> d
      [[3, 2], [9, 2], [10, 12]]
   """
    new_matrix = []

    for row_index in range(len(m1)):
        new_matrix += [add_lists(m1[row_index],m2[row_index])]

    return new_matrix
    

def scalar_mult(n, m):
    """
      >>> a = [[1, 2], [3, 4]]
      >>> scalar_mult(3, a)
      [[3, 6], [9, 12]]
      >>> b = [[3, 5, 7], [1, 1, 1], [0, 2, 0], [2, 2, 3]]
      >>> scalar_mult(10, b)
      [[30, 50, 70], [10, 10, 10], [0, 20, 0], [20, 20, 30]]
      >>> b
      [[3, 5, 7], [1, 1, 1], [0, 2, 0], [2, 2, 3]]
    """
    new_matrix = m[:]

    for o_index in range(len(m)):
        for i_index in range(len(m[o_index])):
            new_matrix[o_index][i_index] = new_matrix[o_index][i_index] * n

    return new_matrix

    
def row_times_column(m1, row, m2, column):
    """
      >>> row_times_column([[1, 2], [3, 4]], 0, [[5, 6], [7, 8]], 0)
      19
      >>> row_times_column([[1, 2], [3, 4]], 0, [[5, 6], [7, 8]], 1)
      22
      >>> row_times_column([[1, 2], [3, 4]], 1, [[5, 6], [7, 8]], 0)
      43
      >>> row_times_column([[1, 2], [3, 4]], 1, [[5, 6], [7, 8]], 1)
      50
    """
    sum = 0

    for index in range(len(m1[0])):
        sum += m1[row][index] * m2[index][column]

    return sum


def matrix_mult(m1, m2):
   """
      >>> matrix_mult([[1, 2], [3,  4]], [[5, 6], [7, 8]])
      [[19, 22], [43, 50]]
      >>> matrix_mult([[1, 2, 3], [4,  5, 6]], [[7, 8], [9, 1], [2, 3]])
      [[31, 19], [85, 55]]
      >>> matrix_mult([[7, 8], [9, 1], [2, 3]], [[1, 2, 3], [4, 5, 6]])
      [[39, 54, 69], [13, 23, 33], [14, 19, 24]]
    """
    new_matrix = []
    temp_matrix = []

    for o_index in range(len(m1)):
        for i_index in range(len(m2[0])):
            temp_matrix.append(row_times_column(m1, o_index, m2, i_index))

            if i_index == len (m2[0]) -1:
                new_matrix.insert(o_index, temp_matrix)
                temp_matrix = []

    return new_matrix


if __name__ == '__main__':
    import doctest
    doctest.testmod()
        
