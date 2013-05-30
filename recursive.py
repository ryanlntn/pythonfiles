def recursive_min(nested_num_list):
    """
      >>> recursive_min([2, 9, [1, 13], 8, 6])
      1
      >>> recursive_min([2, [[100, 7], 90], [1, 13], 8, 6])
      1
      >>> recursive_min([2, [[13, 7], 90], [1, 100], 8, 6])
      1
      >>> recursive_min([[[13, 7], 90], 2, [1, 100], 8, 6])
      1
    """
    smallest = nested_num_list[0]
    while type(smallest) == type([]):
        smallest = smallest[0]

    for element in nested_num_list:
        if type(element) == type([]):
            min_of_elem = recursive_min(element)
            if smallest > min_of_elem:
                smallest = min_of_elem
        else:                           # element is not a list
            if smallest > element:
                smallest = element

    return smallest


def recursive_count(target, nested_num_list):
    """
      >>> recursive_count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]])
      4
      >>> recursive_count(7, [[9, [7, 1, 13, 2], 8], [7, 6]])
      2
      >>> recursive_count(15, [[9, [7, 1, 13, 2], 8], [2, 6]])
      0
      >>> recursive_count(5, [[5, [5, [1, 5], 5], 5], [5, 6]])
      6
    """
    counter = 0
    
    for element in nested_num_list:
        if type(element) == type([]):
            counter += recursive_count(target, element)
        else:
            if element == target:
                counter += 1

    return counter


def flatten(nested_num_list):
    """
      >>> flatten([2, 9, [2, 1, 13, 2], 8, [2, 6]])
      [2, 9, 2, 1, 13, 2, 8, 2, 6]
      >>> flatten([[9, [7, 1, 13, 2], 8], [7, 6]])
      [9, 7, 1, 13, 2, 8, 7, 6]
      >>> flatten([[9, [7, 1, 13, 2], 8], [2, 6]])
      [9, 7, 1, 13, 2, 8, 2, 6]
      >>> flatten([[5, [5, [1, 5], 5], 5], [5, 6]])
      [5, 5, 1, 5, 5, 5, 5, 6]
    """
    flat_list = []
    
    for element in nested_num_list:
        if type(element) == type([]):
            flat_list += flatten(element)
        else:
            flat_list += [element]

    return flat_list
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()
