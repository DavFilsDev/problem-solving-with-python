# sliding_window_test.py

def max_subarray_sum(arr, k):
    if len(arr) < k:
        return None

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i]
        window_sum -= arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


def longest_unique_substring(s):
    seen = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


def run_tests():
    print("=== FIXED SIZE SLIDING WINDOW ===")
    print(max_subarray_sum([2, 1, 5, 1, 3, 2], 3), "→ expected 9")
    print(max_subarray_sum([1, 2, 3, 4, 5], 2), "→ expected 9")
    print(max_subarray_sum([1, 1, 1, 1], 4), "→ expected 4")

    print("\n=== VARIABLE SIZE SLIDING WINDOW ===")
    print(longest_unique_substring("abcabcbb"), "→ expected 3")
    print(longest_unique_substring("bbbbb"), "→ expected 1")
    print(longest_unique_substring("pwwkew"), "→ expected 3")


if __name__ == "__main__":
    run_tests()
