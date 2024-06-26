# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         for i in s:
#             if s.rindex(i) == s.index(i):
#                 return s.index(i)
#         return -1
        
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        l = Counter(s)
        for i,j in l.items():
            if j == 1:
                return s.index(i)
        return -1