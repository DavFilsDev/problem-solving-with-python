def two_sum(nums, target):
    seen = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in seen:
            return [seen[diff], i]
        seen[n] = i


if __name__ == "__main__":
    tests = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
        ([1, 5, 3, 7], 8)
    ]

    for nums, target in tests:
        print(nums, "target =", target, "=>", two_sum(nums, target))
