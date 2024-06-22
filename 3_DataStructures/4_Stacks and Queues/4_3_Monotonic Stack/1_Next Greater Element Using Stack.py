"""
Next Greater Element - Fixed Array(Not Circular)
Input: N = 11, A[] = {3,10,4,2,1,2,6,1,7,2,9}

Output: 10,-1,6,6,2,6,7,7,9,9,-1


Algorithm:
- traverse from right to left
- if elements in stack and remove elements that are less than ele in the arr to find the nearest greater ele 
    - now the top will be nge of current ele
- append current ele to stack
"""


def nextGreaterElement(arr):
    size = len(arr)
    nge_arr = [-1] * size
    st = []

    for i in range(size - 1, -1, -1):
        while st and st[-1] <= arr[i]:
            st.pop()

        if st:
            nge_arr[i] = st[-1]
        st.append(arr[i])
    return nge_arr


if __name__ == "__main__":
    arr = [3, 10, 4, 2, 1, 2, 6, 1, 7, 2, 9]
    res = nextGreaterElement(arr)
    print("The next greater elements are")
    print(*arr)
    print(*res)
