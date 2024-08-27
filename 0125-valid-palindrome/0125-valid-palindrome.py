class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''
        for i in s.lower():
            if i.isalnum():
                new_s = new_s + i
        n = len(new_s)
        for i in range(n):
            if new_s[i] != new_s[-i-1]:
                return False
        return True