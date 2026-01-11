def find_it(seq):
    result = 0
    for n in seq:
        result ^= n
    return result

tests = [
    [7],
    [0],
    [1,1,2],
    [0,1,0,1,0],
    [1,2,2,3,3,3,4,3,3,3,2,2,1]
]

for t in tests:
    print(t, "=>", find_it(t))
