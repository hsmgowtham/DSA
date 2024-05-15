"""
Insertion Merge Algorithm:
------------------------
- Divide: Divide the list or array recursively into two halves until it can no more be divided.
- Conquer: Each subarray is sorted individually using the merge sort algorithm.
- Merge: The sorted subarrays are merged back together in sorted order. The process continues until all elements from both subarrays have been merged.
- Time complexity: O(nlogn) in all cases.
- Space complexity: O(n), Additional space is required for the temporary array used during merging.
- Merge sort has a worst-case time complexity of O(N logN), which means it performs well even on large datasets.

li - leftindex
ri - rightindex
"""


def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        # recursively divide the left and right arrays until one left
        merge_sort(left_arr)
        merge_sort(right_arr)

        # merge
        merge(arr, left_arr, right_arr)
    return arr



def merge(arr, left_arr, right_arr):
    i = 0 # left_arr index
    j = 0 # right_arr index
    k = 0 # merged_arr index

    # merge arrays
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1


arr = [13, 46, 24, 52, 20, 9]
print(merge_sort(arr))
