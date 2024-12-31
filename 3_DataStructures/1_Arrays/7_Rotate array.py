"""
Initial Approach
Time Complexity: O(k*n)
Space Complexity: O(1)
"""
def run1(nums, k):
    while k!=0:
        # print("k", k)
        j = 0
        current_val = nums[j]
        size = len(nums)
        while (j+1)%size!=0:
            next_val = nums[(j+1)%size]
            nums[(j+1)%size] = current_val
            current_val = next_val
            j += 1
            # print(nums)
        nums[(j+1)%size] = current_val
        k-=1


"""
Optimal Approach:

Reverse subarray

Time Complexity: O(n)
Space Complexity: O(1)
"""
def run2(nums, k):
    n = len(nums)
    k = k % n  # Handle cases where k > n
    
    # Helper function to reverse a segment of the array
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    # Step 1: Reverse the entire array
    reverse(0, n - 1)
    # Step 2: Reverse the first k elements
    reverse(0, k - 1)
    # Step 3: Reverse the rest
    reverse(k, n - 1)

nums=[1,2,3,4,5,6,7]
k=3
run1(nums,k)
print(nums)