class Solution:
    def __init__(self):
        self.romanValue = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

    def romanToInt(self, s: str) -> int:
        result = 0
        for ind, val in enumerate(s[:-1]):
            if self.romanValue[val] < self.romanValue[s[ind+1]]:
                result -= self.romanValue[val]
            else:
                result += self.romanValue[val]
        return result + self.romanValue[s[-1]]


