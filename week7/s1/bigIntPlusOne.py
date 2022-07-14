# Implement a function to increment an arbitrary precision integer represented in the form of an array, where each element in the array corresponds to a digit.

# Examples:

# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: 123 + 1 = 124

# Input: [5,8,9]
# Output: [5,9,0]
# Explanation: 589 + 1 = 590

# Edge Case: [], [0], [9][9][9]

from array import array


def plusOne(arr: array):

    if not arr:
        return [1]

    ptr = len(arr) - 1

    while ptr > -1:
        arr[ptr] = arr[ptr] + 1

        if arr[ptr] < 10:
            return arr
        else:
            arr[ptr] = 0
            ptr -= 1

    arr.insert(0, 1)
    return arr


print(plusOne([1, 2, 3]))  # [1, 2, 4]
print(plusOne([5, 8, 9]))  # [5, 9, 0]
print(plusOne([9, 9, 9]))  # [1, 0, 0, 0]
print(plusOne([]))  # [1]
print(plusOne([0]))  # [1]
