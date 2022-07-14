# Implement a method to find the number of occurrences of any given word in a book. A word is represented as a string and a book is represented as an array / list of strings.

# Optimize the method to be called multiple times.

# Examples:

# Input: [" The", "dog", "jumped", "in", "the", "dog", "house"], "dog"
# Output: 2


class Solution:
    def wordFreq(self, wlist: list, s: str) -> int:
        if len(wlist) == 0 or wlist is None or s is None or s == "":
            return -1
        count = 0

        for word in wlist:
            w = word.lower()
            if w == s.lower():
                count += 1
            else:
                pass
        return count


class Test:
    if __name__ == "__main__":
        sol = Solution()
        print(
            sol.wordFreq([" The", "dog", "jumped", "in", "the", "dog", "house"], "dog")
        )
