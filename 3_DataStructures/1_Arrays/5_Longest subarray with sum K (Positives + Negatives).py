"""
Brute Force: O(n^2)
SC: O(1)
"""
def longest_subarray_brute_force(arr, k):
    n = len(arr)
    max_length = 0
    for i in range(n):
        for j in range(i, n):
            current_sum = sum(arr[i:j + 1])
            if current_sum == k:
                max_length = max(max_length, j - i + 1)
    return max_length

# Example
print(longest_subarray_brute_force([1, 2, 3, 7, 1], 7))  # Output: 2

"""
Prefix Sum with Nested Loops: O(n^2)
SC: O(n)
"""
def longest_subarray_prefix_nested(arr, k):
    n = len(arr)
    prefix_sum = [0] * n
    prefix_sum[0] = arr[0]

    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]

    max_length = 0
    for i in range(n):
        for j in range(i, n):
            current_sum = prefix_sum[j] - (prefix_sum[i - 1] if i > 0 else 0)
            if current_sum == k:
                max_length = max(max_length, j - i + 1)
    return max_length

# Example
print(longest_subarray_prefix_nested([1, 2, 3, 7, 1], 7))  # Output: 2

"""
Optimized Prefix Sum with Hash Map: O(n)
SC: O(n)
"""
def longest_subarray_hashmap(arr, k):
    prefix_sum_map = {}
    prefix_sum = 0
    max_length = 0

    for i in range(len(arr)):
        prefix_sum += arr[i]

        if prefix_sum == k:
            max_length = i + 1

        if (prefix_sum - k) in prefix_sum_map:
            max_length = max(max_length, i - prefix_sum_map[prefix_sum - k])

        if prefix_sum not in prefix_sum_map:
            prefix_sum_map[prefix_sum] = i

    return max_length

# Example
print(longest_subarray_hashmap([1, 2, 3, 7, 1], 7))  # Output: 2


"""
Sliding Window (Only for Non-Negative Arrays)
TC: O(n)
SC: O(1)
"""
def longest_subarray_sliding_window(arr, k):
    start = 0
    current_sum = 0
    max_length = 0

    for end in range(len(arr)):
        current_sum += arr[end]

        while current_sum > k and start <= end:
            current_sum -= arr[start]
            start += 1

        if current_sum == k:
            max_length = max(max_length, end - start + 1)

    return max_length

# Example
print(longest_subarray_sliding_window([1, 2, 3, 7, 1], 7))  # Output: 2
