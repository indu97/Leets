class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        str_pattern_dict = {}
        pattern_str_dict = {}
        s = s.split()
        i = 0
        if len(s) != len(pattern):
            return False
        for word in s:
            if word in str_pattern_dict:
                if str_pattern_dict[word] != pattern[i]:
                    return False
            elif pattern[i] in pattern_str_dict:
                if pattern_str_dict[pattern[i]] != word:
                    return False
            else:
                str_pattern_dict[word] = pattern[i]
                pattern_str_dict[pattern[i]] = word
            i += 1
        return True
    