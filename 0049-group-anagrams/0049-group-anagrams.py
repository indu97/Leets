class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for i in range(len(strs)):
            key = ''.join(sorted(strs[i]))
            if key in dictionary:
                dictionary[key].append(strs[i])
            else:
                dictionary[key] = [strs[i]]
        res = []
        for anagram in dictionary.values():
            res.append(anagram)
        return res