class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            if carry != 0: 
                sum = digits[i] + carry
                carry = sum // 10
                digits[i] = sum % 10
                if i == 0 and carry!= 0:
                    digits.insert( 0, carry)
                
        return digits