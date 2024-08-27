class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0 
        val = nums[0]
        for idx, ele in enumerate(nums):
            if idx != 0:
                if ele == val:
                    k += 1
                else: 
                    val = ele
                    if k > 0:
                        temp = nums[idx - k]
                        nums[idx - k] = nums[idx]
                        nums[idx] = temp
        return  len(nums) - k

        