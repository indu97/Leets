class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(target, idx, comb):
            if idx >= len(candidates):
                return
            # if target == 0:
            #     res.append(comb)
            if target > 0:
                c = target // candidates[idx]
                for i in range(c + 1):
                    newtarget = target - i*candidates[idx]
                    if newtarget == 0:
                        res.append(comb + [candidates[idx]]*i)
                    else: 
                        helper(newtarget, idx + 1, comb + [candidates[idx]]*i)
        helper(target, 0, [])
        return res
                
                