"""
Example 1:

Input: height= [0,1,0,2,1,0,1,3,2,1,2,1]

Output: 6
https://takeuforward.org/data-structure/trapping-rainwater/
https://leetcode.com/problems/trapping-rain-water/description/
"""

"""
Algo 1:
for each ele pos find left max and right max and add min(leftmax, rightmax) - element as trapped water

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


"""
Algo 2:
- for finding leftmax and right max of each element we compute and store prefixmax and suffixmax
    and then for each element we add min(prefixmax[i], suffixmax[i]) - arr[i] as trapped water

TC: O(N) + O(N) + O(N) = O(N)
SC: O(3N)
"""


def trappedwater2(arr):
    water_trapped = 0
    size = len(arr)
    prefixmax = [0] * size
    suffixmax = [0] * size

    # prefixmax
    prefixmax[0] = arr[0]
    for i in range(1, size):
        prefixmax[i] = max(prefixmax[i - 1], arr[i])

    # suffixmax
    suffixmax[size - 1] = arr[size - 1]
    for i in range(size - 2, -1, -1):
        suffixmax[i] = max(suffixmax[i + 1], arr[i])

    for i in range(size):
        water_trapped += min(prefixmax[i], suffixmax[i]) - arr[i]
    return water_trapped


"""
Algo 3:
- for finding leftmax and right max of each element we compute and store prefixmax and suffixmax
    and then for each element we add min(prefixmax[i], suffixmax[i]) - arr[i] as trapped water

TC: O(N) - as we are using 2 pointer approach
SC: O(1) - no extra space
"""


def trappedwater3(arr):
    water_trapped = 0
    left = 0
    right = len(arr) - 1
    leftmax = 0
    rightmax = 0

    while left <= right:
        if arr[left] <= arr[right]:
            if arr[left] >= leftmax:
                leftmax = arr[left]
            else:
                water_trapped += leftmax - arr[left]
            left += 1
        else:
            if arr[right] >= rightmax:
                rightmax = arr[right]
            else:
                water_trapped += rightmax - arr[right]
            right -= 1
    return water_trapped


arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

# Algo 1
print(trappedwater1(arr))

# Algo 2
print(trappedwater2(arr))

# Algo 3
print(trappedwater3(arr))
