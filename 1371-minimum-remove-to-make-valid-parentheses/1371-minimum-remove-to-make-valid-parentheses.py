class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s_list = list(s)
        counter = 0
        for idx, c in enumerate(s):
            if c == '(':
                stack.append([idx, c])
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    s_list.pop(idx - counter)
                    counter += 1
        
        while stack:
            popped_array = stack.pop()
            idx = popped_array[0]
            s_list.pop(idx - counter)
        
        return ''.join(s_list)
        
        
        
        
        
        
        
        
        
        # stack = []
        # offensive_idx = []
        # for idx, c in enumerate(s):
        #     if c == '(':
        #         stack.append([idx, c])
        #     elif c == ')':
        #         if stack:
        #             stack.pop()
        #         else:
        #             offensive_idx.append(idx)
        # while stack:
        #     popped_array = stack.pop()
        #     idx = popped_array[0]
        #     offensive_idx.append(idx)
        
        # res = ''
        # for idx, c in enumerate(s):
        #     if idx not in offensive_idx:
        #         res = res + c
        # return res