"""
Bubble Sort Algorithm (Swap Adjacent):
------------------------
- Compares adjacent elements and swaps them if they're in the wrong order.
- Repeats this process until the list is sorted.
- Time complexity: O(n^2) in the worst and average cases, O(n) in the best case (if the list is already sorted).
- Space complexity: O(1) as it requires only a constant amount of additional space.
- Not efficient for large datasets due to its quadratic time complexity.
"""

def bubble_sort(arr):
    for i in range(len(arr)-1, -1, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [13,46,24,52,20,9]
print(bubble_sort(arr))