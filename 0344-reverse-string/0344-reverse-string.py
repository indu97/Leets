class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """        
        my_stack = []

        for char in s:
            my_stack.append(char)

        i = 0
        while(len(my_stack) != 0):
            s[i] = my_stack.pop()
            i += 1