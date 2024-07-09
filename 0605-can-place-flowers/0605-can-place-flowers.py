class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev = 0
        for idx, val in enumerate(flowerbed):
            if idx != len(flowerbed) - 1:
                if not prev and not val and not flowerbed[idx+1]:
                    n = n - 1
                    val = 1
                    prev = val
                else: 
                    prev = val
            else:
                if not prev and not val:
                    n = n - 1
                    val = 1
                    prev = val
                else: 
                    prev = val
        if n <= 0:
            return True


        