"""
Input:
arr1[] = {1,2,3,4,5}  
arr2[] = {2,3,4,4,5}
Output:

 {1,2,3,4,5}

Input:

n = 10,m = 7.
arr1[] = {1,2,3,4,5,6,7,8,9,10}
arr2[] = {2,3,4,4,5,11,12}
Output:
 {1,2,3,4,5,6,7,8,9,10,11,12}
"""

arr = []
arr1 = [1,2,3,4,5,6,7,8,9,10]
arr2 = [2,3,4,4,5,11,12]
i = 0
j = 0
k = 0
while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        if k==0:
            arr.append(arr1[i])
        else:
            if arr[-1]<arr1[i]:
                arr.append(arr1[i])
        i += 1
    elif arr1[i] == arr2[j]:
        arr.append(arr1[i])
        i += 1
        j += 1
    else:
        if k==0:
            arr.append(arr1[i])
        else:
            if arr[k-1]<arr2[j]:
                arr.append(arr2[j])
        j += 1
    k += 1

while i < len(arr1):  # If any elements left in arr1
    if arr[-1] != arr1[i]:
        arr.append(arr1[i])
    i += 1

while j < len(arr2):  # If any elements left in arr2
    if arr[-1] != arr2[j]:
        arr.append(arr2[j])
    j += 1
print(arr)
    
