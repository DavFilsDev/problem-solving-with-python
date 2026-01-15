def has_pair_with_sum(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return False

print(has_pair_with_sum([1, 2, 3, 4, 6], 6))  # True
print(has_pair_with_sum([1, 2, 3, 9], 8))    # False
