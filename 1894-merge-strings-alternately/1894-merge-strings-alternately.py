class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)
        out = ""
        for i in range(m+n):
            if (i < m and i < n):
                out += word1[i]
                out += word2[i]
            else:
                if (i < m):
                    out += word1[i]
                if (i < n):
                    out += word2[i]
        return out
        