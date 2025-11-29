class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []

        my_dict = {
            '{' : '}',
            '[' : ']',
            '(' : ')'
        }

        for char in s:
            if char in my_dict.keys():
                my_stack.append(char)
            else:
                if len(my_stack) != 0:
                    value = my_stack.pop()
                    if char != my_dict[value]:
                        return False
                else:
                    return False

        return(len(my_stack) == 0)