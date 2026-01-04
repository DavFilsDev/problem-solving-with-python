def max_product(arr):
    if not arr:
        return 0

    max_prod = arr[0]
    min_prod = arr[0]
    result = arr[0]

    for n in arr[1:]:
        temp_max = max(n, max_prod * n, min_prod * n)
        min_prod = min(n, max_prod * n, min_prod * n)
        max_prod = temp_max

        result = max(result, max_prod)

    return result


if __name__ == "__main__":
    tests = [
        [2, 3, -2, 4],
        [-2, 0, -1],
        [-2, 3, -4],
        [0, 2],
        [-1, -3, -10, 0, 60],
    ]

    for t in tests:
        print(t, "=>", max_product(t))
