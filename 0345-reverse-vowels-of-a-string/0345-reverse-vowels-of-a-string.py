class Solution:
    def reverseVowels(self, s: str) -> str:
        vow = {'a','e','i','o','u','A','E','I','O','U'}
        existing_keys = []
        existing_idxs = []
        for idx, val in enumerate(s):
            if val in vow:
                existing_keys.append(val)
                existing_idxs.append(idx)
        i = 0
        for val in existing_keys[::-1]:
            pos = existing_idxs[i]
            s = s[:pos] + val + s[pos+1:]
            i += 1
        return s