class Solution:
    def climbStairs(self, n: int) -> int:
        # for i = 0 to n+1:
        #     twos = n - i // 2
        #     if twos = int(twos):
        # if n == 1: 
        #     return 1
        # elif n == 2:
        #     return 2
        # else:
        #     return self.climbStairs(n-1) + self.climbStairs(n-2)
        arr = [0] * (n+1)
        arr[1] = 1
        if n >= 2:
            arr[2] = 2
            for i in range(3, n+1):
                arr[i] = arr[i-1] + arr[i-2]
        return arr[n]