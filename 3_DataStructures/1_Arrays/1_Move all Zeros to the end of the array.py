"""
Input:
 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1
Output:
 1 ,2 ,3 ,4 ,1 ,0 ,0 ,0
"""
"""
Brute Force Approach
Time Complexity: O(k*(n-k)) ~ O(N^2) if all the elements are zeroes
"""
def moveZeroes2(nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 1
        swap_start_index = 0
        while i < len(nums):
            if nums[i]!=0 and nums[i-1]==0:
                swap_start_index = i
                while nums[i-1]==0 and i-1>=0:
                    nums[i], nums[i-1] = nums[i-1], nums[i]
                    i -= 1
                i = swap_start_index + 1
            else:
                i += 1
"""
Optimal Solution:
Time Complexity: O(N)
"""
def moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    # find 1st 0th position
    zero_index = -1
    for i in range(0,len(nums)):
        if nums[i]==0:
            zero_index = i
            break

    # if zeroes exist in the array
    if zero_index != -1:
        for i in range(zero_index+1, len(nums)):
            if nums[i]!=0:
                nums[zero_index], nums[i] = nums[i], nums[zero_index]
                zero_index += 1