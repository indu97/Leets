class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(" ", "")
        p = ''
        for c in s:
            if c.isalnum():
                p += c
        return p == p[::-1]