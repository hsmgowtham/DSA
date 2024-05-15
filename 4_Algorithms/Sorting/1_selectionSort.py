"""
Selection Sort Algorithm:
------------------------
- Works by repeatedly finding the minimum element from the unsorted portion and moving it to the beginning.
- Time complexity: O(n^2) in all cases.
- Not suitable for large datasets due to its quadratic time complexity.
- In-place sorting algorithm.
"""

def selection_sort(arr):
    for i in range(0, len(arr)-1): 
        min_ele_position = i       
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_ele_position]:
                min_ele_position = j
        print(i, j, arr[i], arr[min_ele_position])
        arr[i],arr[min_ele_position] = arr[min_ele_position],arr[i]
    return arr

arr = [5,4,3,2,1]
print(selection_sort(arr))