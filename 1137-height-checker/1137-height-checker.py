import numpy as np
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # oldHeights = np.copy(heights)
        # heights.sort()
        # count = 0
        # for i in range(len(oldHeights)):
        #     if oldHeights[i] != heights[i]:
        #         count += 1
        # return count
        
        oldHeights = np.copy(heights)
        n = len(heights)
        count = 0
        for i in range(n):
            min = heights[i]
            idx_min = i
            for j in range(i+1,n):
                if heights[j] < min:
                    min = heights[j]
                    idx_min = j
            if min != heights[i]:  
                #count += 1
                temp = heights[i]
                heights[i] = min
                heights[idx_min] = temp
                #if idx_min == n-1:
                    #count += 1
        for i in range(len(heights)):
            if oldHeights[i] != heights[i]:
                count += 1
    
        return count
