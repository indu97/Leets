class Solution:
    def reverseVowels(self, s: str) -> str:
        vow = {'a','e','i','o','u'}
        keys = []
        idxs = []
        for idx, val in enumerate(s):
            if val.lower() in vow:
                keys.append(val)
                idxs.append(idx)
        i = 0
        for val in keys[::-1]:
            pos = idxs[i]
            s = s[:pos] + val + s[pos+1:]
            i += 1
        return s