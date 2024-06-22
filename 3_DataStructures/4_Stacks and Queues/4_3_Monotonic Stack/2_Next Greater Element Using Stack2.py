"""
Next Greater Element - Circular Array
Input: N = 11, A[] = {2, 10, 12, 1, 11}

Output: 10, 12, -1, 11, 12


Algorithm:
- traverse from right to left (2*size) => {2, 10, 12, 1, 11, 2, 10, 12, 1, 11}
                                          {0, 1,   2, 3, 4,  5,  6,  7, 8, 9}
- if elements in stack and remove elements that are less than ele in the arr to find the nearest greater ele 
    - now the top will be nge of current ele
    - add ele to nge only if i < size
- append current ele to stack
"""


def nextGreaterElement(arr):
    size = len(arr)
    nge_arr = [-1] * size
    st = []

    for i in range(2 * size - 1, -1, -1):
        while st and st[-1] <= arr[i % size]:
            st.pop()

        if i < size:
            if st:
                nge_arr[i] = st[-1]
        st.append(arr[i % size])
    return nge_arr


if __name__ == "__main__":
    arr = [3, 10, 4, 2, 1, 2, 6, 1, 7, 2, 9]
    res = nextGreaterElement(arr)
    print("The next greater elements are")
    print(*arr)
    print(*res)
