class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if strs is None: return None
        res = strs[0]
        for word in strs[1:]:
            i = 0
            while i < len(word) and i < len(res):
                if word[i] != res[i]:
                    res = res[0:i:]
                    break
                i += 1
            else: res = res[:i]
        return res
            