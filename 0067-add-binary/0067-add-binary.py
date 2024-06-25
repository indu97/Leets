class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aL, bL = -len(a), -len(b)
        res = ""
        carry, i = 0, -1
        while i >= aL or i>= bL:
            aBit = int(a[i]) if i >= aL else 0
            bBit = int(b[i]) if i >= bL else 0
            val = aBit + bBit + carry
            if val == 2:
                val = 0
                carry = 1
            elif val == 3:
                val = 1
                carry = 1
            else:
                carry = 0
            res = str(val) + res
            i -= 1
        return "1" + res if carry else res