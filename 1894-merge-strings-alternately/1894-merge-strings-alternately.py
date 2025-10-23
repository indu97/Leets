class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)
        out = []
        for i in range(max(m,n)):
            if (i < m):
                out.append(word1[i])
            else:
                out.append(word2[i:])
                break
            if (i < n):
                out.append(word2[i])
            else:
                out.append(word1[i+1:])
                break
        return "".join(out)
        