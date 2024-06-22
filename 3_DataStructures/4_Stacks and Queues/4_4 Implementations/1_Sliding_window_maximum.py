"""
Input: arr = [4,0,-1,3,5,3,6,8], k = 3

Output: [4,3,5,5,6,8]

Explanation: 

Window position                   Max
------------------------         -----
[4  0  -1] 3  5  3  6  8           4
 4 [0  -1  3] 5  3  6  8           3
 4  0 [-1  3  5] 3  6  8           5
 4  0  -1 [3  5  3] 6  8           5
 4  0  -1  3 [5  3  6] 8           6
 4  0  -1  3  5 [3  6  8]          8
"""

"""
Algo 1 (Brute Force) --------
1 loop for 0 to n
1 inner loop for k length window
TC: O(N*(n-k))

Algo 2(Optimal) --------------
Algorithm:
1. **Initialize Data Structures:**
   - Use a deque (`que`) to store indices of array elements.
   - Prepare an output list to store the maximum values for each window.

2. **Slide the Window:**
   - Start with the right pointer `r` and iterate through the array.

3. **Maintain the Deque:**
   - For each element `nums[r]`:
     - Remove elements from the deque that are less than the current element. They are no longer useful because they can’t be the maximum in the current window or any future windows that include `nums[r]`.
     - Add the current index `r` to the deque.

4. **Remove Out of Bounds Indices:**
   - If the leftmost index in the deque is outside the current window (i.e., less than `r - k + 1`), remove it.

5. **Record the Maximum for the Current Window:**
   - When the window is fully formed (i.e., when `r` is at least `k - 1`), the element at the front of the deque is the maximum for the current window. Append it to the output list.

6. **Continue the Process:**
   - Move to the next element and repeat until the end of the array.

7. **Return the Result:**
   - After processing all windows, return the output list containing the maximum values for each window.

   TC: O(N)
"""
import collections


def getMaximumWindow(nums, k):
    que = collections.deque()
    output = []
    l = r = 0
    while r < len(nums):
        while que and nums[que[-1]] < nums[r]:
            que.pop()
        que.append(r)

        if l > que[0]:
            que.popleft()

        if (r + 1) >= k:
            output.append(nums[que[0]])
            l += 1
        r += 1
    return output
