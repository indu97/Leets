class Solution:
    def maxPower(self, s: str) -> int:
        maxPower = 0
        power = 0
        uniqueChar = s[0]

        for val in s:
            if val == uniqueChar:
                power += 1
            else: 
                uniqueChar = val
                power = 1
            if maxPower < power:
                maxPower = power
        return maxPower