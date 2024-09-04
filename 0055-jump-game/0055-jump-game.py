class Solution:
    memDict = {}
    # def subCanJump(self, nums, idx, n, reachable) -> bool:
    #     canJumpBool = False
    #     for step in range(1,nums[idx]+1):
    #         if nums[idx] == 0:
    #             dpDict[idx] = False
    #             return False
    #         if idx + step == n - 1:
    #             dpDict[idx] = True
    #             return True
    #         if idx in dpDict: 
    #             return dpDict[idx]
    #         else:
    #             canJumpBool = self.subCanJump(nums, idx+step, n, dpDict) | canJumpBool
    #     dpDict[idx] = canJumpBool
    #     return canJumpBool

    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n - 1
        for i in range(n - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return True if goal == 0 else False
