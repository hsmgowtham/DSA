"""
Nearest Smaller Element in the array such that the element has an index smaller than i. - Fixed (Smaller to the left)
Input 1:
    A = [4, 5, 2, 10, 8]
Output 1:
    G = [-1, 4, -1, 2, 2]


Algorithm:
- traverse from left to right (size)
- if elements in stack and remove elements that are less than ele in the arr to find the nearest greater ele 
    - now the top will be nse of current ele
- append current ele to stack
"""


def nearestSmallerElement(arr):
    size = len(arr)
    nse_arr = [-1] * size
    st = []

    for i in range(0, size):
        while st and st[-1] >= arr[i]:
            st.pop()

        if st:
            nse_arr[i] = st[-1]
        st.append(arr[i])
    return nse_arr


if __name__ == "__main__":
    arr = [4, 5, 2, 10, 8]
    res = nearestSmallerElement(arr)
    print("The nearest smaller elements are")
    print(*arr)
    print(*res)
