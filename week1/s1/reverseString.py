from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> List[str]:

        l_ptr = 0
        r_ptr = len(s) - 1

        while l_ptr < r_ptr:
            temp = s[l_ptr]
            s[l_ptr] = s[r_ptr]
            s[r_ptr] = temp
            l_ptr += 1
            r_ptr -= 1

        return s


if __name__ == "__main__":
    sol = Solution()
    str = "bob"
    list_str = list(str)
    print("".join(sol.reverseString(list_str)))
