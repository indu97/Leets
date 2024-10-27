class Solution:
    def pal_check(self, s: str, counter):
        n = len(s)
        for i in range(n // 2):
            # if forward and backward pointer are not same, del once
            if s[i] != s[n - i - 1]:
                if counter == 0:
                    s_1 = s[:i] + s[i + 1:]
                    s_2 = s[:n - i - 1] + s[n - i:]
                    return self.pal_check(s_1, 1) or self.pal_check(s_2, 1)
                else:
                    return False
        return True
            

    def validPalindrome(self, s: str) -> bool:
        return self.pal_check(s, 0)