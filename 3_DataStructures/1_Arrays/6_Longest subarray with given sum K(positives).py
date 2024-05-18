def lenOfLongSubarr (arr, n, k) : 
    i = 0
    j = 0
    summ = arr[0]
    max_len = 0
    while j < len(arr):
        while summ > k  and i <= j:
            summ -= arr[i]
            i += 1
        if summ == k:
            max_len = max(max_len, j-i+1)
        
        j += 1
        if j < len(arr):
            summ += arr[j]
        
    return max_len

print(lenOfLongSubarr([2,3,5,1,9],5,10))