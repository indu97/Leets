class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0 
        c = 1
        val = nums[0]
        for idx, ele in enumerate(nums):
            if idx > 0:
                if ele == val:
                    if c < 2:
                        c += 1
                    else:
                        k += 1
                else: 
                    val = ele
                    c = 1
                temp = nums[idx - k]
                nums[idx - k] = nums[idx]
                nums[idx] = temp       
        return len(nums) - k
        