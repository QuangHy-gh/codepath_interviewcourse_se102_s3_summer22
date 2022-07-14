"""
Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

Input: [1, 2, 5, 3, 7, 10, 9, 12]
Output: 5
Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted

Input: [1, 3, 2, 0, -1, 7, 10]
Output: 5
Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted
"""


def shortest_unsorted_array(arr):
    left = 0
    right = len(arr) - 1

    # while left pointer is less than right pointer, scan and look for out of order elements
    # [3,7,10] #10 , until we point to something
    # greater than 10
    # [2,7,12,5,9,4,20,6,35]
    # left pointer stops at 12
    # right pointer stops at 6
    # 4 , 5 , 20 will cause
    # [1, 2, 5, 3, 7, 10, 9, 12]
    # left will stop at 5
    # right will stop at 9
    # [1, 3, 2, 0, -1, 7, 10]
    # left will stop at 3
    # right will stop at -1

    while left < right and arr[left] < arr[left + 1]:
        left += 1

    if left == right:  # edge case were the array is
        # already sorted
        return 0

    while left < right and arr[right] > arr[right - 1]:
        right -= 1

    if right == 0:
        return len(arr)

    subMax = -float("inf")
    subMin = float("inf")
    for k in range(left, right):
        subMax = max(subMax, arr[k])
        subMin = min(subMin, arr[k])

    while left > 0 and arr[left - 1] > subMin:
        left -= 1
    while right < len(arr) - 1 and arr[right + 1] < subMax:
        right += 1

    return right - left + 1


print("shortest unsorted array")
print(shortest_unsorted_array([1, 2, 5, 3, 7, 10, 9, 12]))  # 5
print(shortest_unsorted_array([2, 7, 12, 5, 9, 4, 20, 6, 35]))  # 7
print(shortest_unsorted_array([1, 3, 2, 0, -1, 7, 10]))  # 5
print(shortest_unsorted_array([1, 2, 3, 4, 5]))  # 0
print(shortest_unsorted_array([]))  # 0
print(shortest_unsorted_array([3, 2, 1]))  # 3
