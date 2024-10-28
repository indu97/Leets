class Solution:
    def pal_check(self, s: str, left, right, counter):
        while(left < right):
            if s[left] != s[right]:
                if counter == 1:
                    return False
                return self.pal_check(s, left + 1, right, 1) or self.pal_check(s, left, right - 1, 1)
            left += 1
            right -= 1
        return True
            

    def validPalindrome(self, s: str) -> bool:
        return self.pal_check(s, 0, len(s) - 1, 0)