# Given an input string, write a function that returns the run-length encoded string for the input string.*

# Example:

# Input: "wwwwaaadexxxxxx"
# Output: "w4a3d1e1x6"
# Challenge: How would you decode the encoded string into the original string?


def runLengthEncoding(s: str):
    strList = list(s)
    ptr = 0

    while ptr < len(strList) - 1:

        occur = 1

        while ptr < len(strList) - 1 and strList[ptr] == strList[ptr + 1]:
            occur += 1
            ptr += 1

        ptr += 1

        print(strList[ptr - 1] + str(occur), end="")


if __name__ == "__main__":

    st = "wwwwaaadexxxxxxywww"
    runLengthEncoding(st)

# Can also use hashmap and a second array, but this is the best solution with O(n) time and o(1) space
