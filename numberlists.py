def only_evens(numbers):
    """
      >>> only_evens([1, 3, 4, 6, 7, 8])
      [4, 6, 8]
      >>> only_evens([2, 4, 6, 8, 10, 11, 0])
      [2, 4, 6, 8, 10, 0]
      >>> only_evens([1, 3, 5, 7, 9, 11])
      []
      >>> only_evens([4, 0, -1, 2, 6, 7, -4])
      [4, 0, 2, 6, -4]
      >>> nums = [1, 2, 3, 4]
      >>> only_evens(nums)
      [2, 4]
      >>> nums
      [1, 2, 3, 4]
    """
    evens = []

    for n in numbers:
        if n % 2 == 0:
            evens += [n]

    return evens


def only_odds(numbers):
    """
      >>> only_odds([1, 3, 4, 6, 7, 8])
      [1, 3, 7]
      >>> only_odds([2, 4, 6, 8, 10, 11, 0])
      [11]
      >>> only_odds([1, 3, 5, 7, 9, 11])
      [1, 3, 5, 7, 9, 11]
      >>> only_odds([4, 0, -1, 2, 6, 7, -4])
      [-1, 7]
      >>> nums = [1, 2, 3, 4]
      >>> only_odds(nums)
      [1, 3]
      >>> nums
      [1, 2, 3, 4]
    """
    odds = []

    for n in numbers:
        if n % 2 != 0:
            odds += [n]

    return odds


def multiples_of(num, numlist):
    """
      >>> multiples_of(3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
      [3, 6, 9]
      >>> multiples_of(4, [15, 16, 17, 18, 19, 20])
      [16, 20]
    """
    multiples = []

    for n in numlist:
        if n % num == 0:
            multiples += [n]

    return multiples


if __name__ == '__main__':
    import doctest
    doctest.testmod()
