"""
Input:
 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1
Output:
 1 ,2 ,3 ,4 ,1 ,0 ,0 ,0
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