class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        l=heights.copy()
        heights.sort()
        ans=0
        for i in range(len(l)):
            if l[i]!=heights[i]:
                ans+=1

        return ans

