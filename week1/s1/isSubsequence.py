from typing import List


class Solution:
    def isSubsequence(self, s: List[str], s2: List[str]) -> bool:
        if len(s) < len(s2):
            print("Wrong length")
            return False
        else:
            l_ptr = 0
            r_ptr = len(s2)
            while r_ptr <= len(s) - 1:
                if s[l_ptr:r_ptr:1] == s2:
                    return True
                else:
                    l_ptr += 1
                    r_ptr += 1
        return False


if __name__ == "__main__":
    s1 = "laboratory"
    s2 = "rat"
    list_s1 = list(s1)
    list_s2 = list(s2)
    sol = Solution()
    print(sol.isSubsequence(list_s1, list_s2))
