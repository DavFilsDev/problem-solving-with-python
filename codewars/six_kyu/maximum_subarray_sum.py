# Kadane’s Algorithm -Solution
def max_sequence(arr):
    max_sum = 0
    current_sum = 0

    for n in arr:
        current_sum = max(0, current_sum + n)
        max_sum = max(max_sum, current_sum)

    return max_sum

if __name__ == "__main__":
    tests = [
        [],
        [-1, -2, -3],
        [1, 2, 3],
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [4, -1, 2, 1],
        [-5, 4, -1, 2, 1, -5],
        [-2, 1, -3, 4, -1, 2, 1]
    ]

    for t in tests:
        print(t, "=>", max_sequence(t))
