def luck_check(st):
    if not st:
        raise ValueError("Empty string")

    if not st.isdigit():
        raise ValueError("Input must be a decimal number")

    n = len(st)
    half = n // 2

    left = st[:half]
    right = st[-half:]

    sum_left = sum(int(d) for d in left)
    sum_right = sum(int(d) for d in right)

    return sum_left == sum_right

tests = [
    "003111",
    "813372",
    "17935",
    "56328116",
    "123456"
]

for t in tests:
    print(t, "=>", luck_check(t))

luck_check("")        # ValueError
