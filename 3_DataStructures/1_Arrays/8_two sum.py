"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

"""
Brute Force approach
TC: O(n^2)
SC: O(1)
"""
def twoSum(nums, target):
    for i in range(0, len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]

"""
Optimal approach: Storing target-val in hashmap with index
TC: O(n)
SC: O(n)
"""
def twoSum1(nums, target):
    hash_map = {}
    for i in range(0, len(nums)):
        temp = target-nums[i]
        if target-nums[i] in hash_map:
            return [i, hash_map[temp]]
        else:
            hash_map[nums[i]] = i



    

