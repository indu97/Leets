class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = ''
        for c in s.lower():
            if c.isalnum():
                p += c
        return p == p[::-1]