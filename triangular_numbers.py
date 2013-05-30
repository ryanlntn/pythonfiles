def print_triangular_numbers(n):
    x = 1
    while x <= n:
        print x, '\t', x*(x+1)/2
        x += 1
    print
