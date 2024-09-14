class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            t_letter = t[i]
            s_letter = s[i]
            if s_letter not in count:
                count[s_letter] = 1
            else:
                count[s_letter] += 1
            
            if t_letter not in count:
                count[t_letter] = -1
            else:
                count[t_letter] -= 1
        for value in count.values():
            if value != 0:
                return False
        return True