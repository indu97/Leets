class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        offensive_idx = []
        for idx, c in enumerate(s):
            if c == '(':
                stack.append([idx, c])
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    offensive_idx.append(idx)
        while stack:
            popped_array = stack.pop()
            idx = popped_array[0]
            offensive_idx.append(idx)
        
        res = ''
        for idx, c in enumerate(s):
            if idx not in offensive_idx:
                res = res + c
        return res