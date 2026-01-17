def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def run_tests():
    print("=== BINARY SEARCH TESTS ===")

    nums = [1, 3, 5, 7, 9, 11, 13]

    print(binary_search(nums, 1), "→ expected 0")
    print(binary_search(nums, 7), "→ expected 3")
    print(binary_search(nums, 13), "→ expected 6")
    print(binary_search(nums, 4), "→ expected -1")
    print(binary_search(nums, 100), "→ expected -1")


if __name__ == "__main__":
    run_tests()