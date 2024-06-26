import numpy as np
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        oldHeights = np.copy(heights)
        heights.sort()
        count = 0
        for i in range(len(oldHeights)):
            if oldHeights[i] != heights[i]:
                count += 1
        return count
        