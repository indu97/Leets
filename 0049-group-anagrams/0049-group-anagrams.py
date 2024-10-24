from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            dictionary[key].append(word)
        res = []
        for anagram in dictionary.values():
            res.append(anagram)
        return res