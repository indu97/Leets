class Solution:
    def addBinary(self, a: str, b: str) -> str:

        if len(a) > len(b):
            while(len(a)>len(b)):
                b = '0' + b

        if len(b) > len(a):
            while(len(b)>len(a)):
                a = '0' + a
        s = ""
        carry = 0
        i = len(a) - 1
        while i >= 0:
            val = int(a[i]) + int(b[i]) + carry
            if val == 2:
                val = 0
                carry = 1
            elif val == 3:
                val = 1
                carry = 1
            else:
                carry = 0
            s = str(val) + s
            i -= 1

        if carry == 1: 
            s = '1' + s
        return s

            
        