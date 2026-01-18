def first_duplicate(nums):
    seen = {}

    for n in nums:
        if n in seen:
            return n
        seen[n] = 1

    return None


def run_tests():
    print("=== HASH MAP FREQUENCY TESTS ===")

    print(first_duplicate([2, 1, 3, 5, 3, 2]), "→ expected 3")
    print(first_duplicate([1, 2, 3, 4]), "→ expected None")
    print(first_duplicate([7, 7, 1, 2]), "→ expected 7")
    print(first_duplicate([]), "→ expected None")


if __name__ == "__main__":
    run_tests()
