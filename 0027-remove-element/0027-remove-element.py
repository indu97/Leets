class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for idx, ele in enumerate(nums):
            if ele == val:
                k += 1
            elif k > 0:
                temp = nums[idx-k]
                nums[idx-k] = nums[idx]
                nums[idx] = temp
        return len(nums) - k