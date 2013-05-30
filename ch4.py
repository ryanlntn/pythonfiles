def is_divisable_by_n(x, n):
    if (x % n) == 0:
        print 'Yes,',x,'is divisible by', n
    else:
        print 'No,',x,'is not divisible by', n

is_divisable_by_n(10, 2)
is_divisable_by_n(9, 2)
is_divisable_by_n(10, 3)
is_divisable_by_n(9, 3)
