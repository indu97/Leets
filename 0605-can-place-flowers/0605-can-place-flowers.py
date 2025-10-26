class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        bed = [0] + flowerbed + [0]
        l = len(bed)

        for i in range(1,l-1):
            if bed[i-1] == bed[i] == bed[i+1] == 0:
                n -= 1
                bed[i] = 1
                if n == 0 : 
                    return True
        return n <= 0

            