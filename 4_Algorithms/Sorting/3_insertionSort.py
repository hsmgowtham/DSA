"""
Insertion Sort Algorithm:
------------------------
- Builds the final sorted array one element at a time by repeatedly taking the next element 
  and inserting it into the proper position in the already sorted part of the array.
- Time complexity: O(n^2) in the worst and average cases, O(n) in the best case (if the list is already sorted).
- Space complexity: O(1) as it requires only a constant amount of additional space.
- Efficient for small datasets or nearly sorted arrays.
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr

    
arr = [13,46,24,52,20,9]    
print(insertion_sort(arr))