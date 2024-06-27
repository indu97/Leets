# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         return (n > 0) and 1162261467 % n == 0

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def zero():
            return 0
        ans = defaultdict(zero)
        ans[1]=1
        ans[3]=1
        ans[9]=1
        ans[27]=1
        ans[81]=1
        ans[243]=1
        ans[729]=1
        ans[2187]=1
        ans[6561]=1
        ans[19683]=1
        ans[59049]=1
        ans[177147]=1
        ans[531441]=1
        ans[1594323]=1
        ans[4782969]=1
        ans[14348907]=1
        ans[43046721]=1
        ans[129140163]=1
        ans[387420489]=1
        ans[1162261467]=1
        
        return ans[n]