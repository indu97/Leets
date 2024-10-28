class Solution:
    def pal_check(self, s: str, start: int, end: int, counter: int) -> bool:
        while start < end:
            if s[start] != s[end]:
                if counter == 1:
                    return False
                # Skip the left character or the right character
                return self.pal_check(s, start + 1, end, 1) or self.pal_check(s, start, end - 1, 1)
            start += 1
            end -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        return self.pal_check(s, 0, len(s) - 1, 0)
