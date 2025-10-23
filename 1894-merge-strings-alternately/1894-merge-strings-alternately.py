class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)
        out = ""
        for i in range(max(m,n)):
            if (i < m):
                out += word1[i]
            else:
                out += word2[i:]
                break
            if (i < n):
                out += word2[i]
            else:
                out += word1[i+1:]
                break
        return out
        