class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        # nums = nums[n-k:]+nums[:n-k]
        # print(nums)
        # for i in range(k):
        #     for j in range(n-1):
        #         temp = nums[j]
        #         nums[j] = nums[-1]
        #         nums[-1] = temp
        a = nums[:n-k]
        for i in range(k):
            nums[i] = nums[n-k+i]
        for i in range(n-k):
            nums[k+i] = a[i]
