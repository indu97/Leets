class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        threshold = max(candies) - extraCandies
        res = [False] * len(candies)

        for i in range(len(candies)):
            if candies[i] >= threshold:
                res[i] = True
        
        return res
        