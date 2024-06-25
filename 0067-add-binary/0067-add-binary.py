class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m = len(a)
        n = len(b)

        if len(a) > len(b):
            while(len(a) > len(b)):
                b = '0' + b

        if len(b) > len(a):
            while(len(b) > len(a)):
                a = '0' + a

        s = ""
        carry = 0
        i = len(a) - 1
        while i >= 0:
            summ = int(a[i]) + int(b[i]) + carry
            val = summ % 2
            carry = summ // 2
            s = str(val) + s
            i -= 1

        if carry == 1: 
            s = '1' + s
        return s