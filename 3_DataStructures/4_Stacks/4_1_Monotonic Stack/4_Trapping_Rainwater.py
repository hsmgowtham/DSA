"""
Example 1:

Input: height= [0,1,0,2,1,0,1,3,2,1,2,1]

Output: 6
https://takeuforward.org/data-structure/trapping-rainwater/
https://leetcode.com/problems/trapping-rain-water/description/

Algo 1:
for each ele pos find left max and right max and add min(leftmax, rightmax) - ele as trapped water

TC: O(N*N) as for each index we are calculating leftMax and rightMax so it is a nested loop.
SC: O(1)
"""


def trappedwater1(arr):
    water_trapped = 0
    for i in range(len(arr)):
        leftmax = 0
        rightmax = 0

        # find leftmax
        j = i
        while j >= 0:
            leftmax = max(leftmax, arr[j])
            j -= 1

        # find rightmax
        j = i
        while j < len(arr):
            rightmax = max(rightmax, arr[j])
            j += 1
        water_trapped += min(leftmax, rightmax) - arr[i]
    return water_trapped


arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

# Algo 1
print(trappedwater1(arr))
