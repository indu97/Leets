import math

class Solution:
    def pal_check(self, s: str, start, end, counter):
        print(s[start:end+1])
        n = end - start + 1
        for i in range(n):
            # if forward and backward pointer are not same, del once
            # print(s[i], s[end - i - 1])
            if s[start + i] != s[end - i]:
                if counter == 0:
                    return self.pal_check(s, i + 1, n - i - 1, 1) or self.pal_check(s, i, n - i - 2, 1)
                else:
                    return False
        return True
            

    def validPalindrome(self, s: str) -> bool:
        return self.pal_check(s, 0, len(s) - 1, 0)