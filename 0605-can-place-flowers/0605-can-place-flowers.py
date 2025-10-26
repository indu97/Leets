class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        flag = 0

        for i in range(l):

            if n > 0:
                # Check if Left side is empty
                if i!= 0:
                    if flowerbed[i-1] != 1 and flag!= 1:
                        flag = 0
                    else:
                        flag = 1

                #  Check if Right side is empty:
                if i!= l-1:
                    if flowerbed[i+1] != 1 and flag != 1:
                        flag = 0
                    else:
                        flag = 1

                if flag == 0 and flowerbed[i] == 0:   
                    n -= 1
                    flowerbed[i] = 1
                    flag = 1
                else:
                    flag = 0
            else: 
                return True

        print(flowerbed) 
        print(n)
        return False if n > 0 else True

            