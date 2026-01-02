def X(s):
    from functools import reduce
    from operator import xor
    return reduce(xor, map(int, s.split()))
