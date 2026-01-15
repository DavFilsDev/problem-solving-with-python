def max_subarray_sum(arr, k):
    if len(arr) < k:
        return None

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i]        # add next element
        window_sum -= arr[i - k]    # remove left element
        max_sum = max(max_sum, window_sum)

    return max_sum
