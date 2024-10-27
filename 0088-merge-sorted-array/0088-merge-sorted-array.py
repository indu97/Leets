class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res = []
        i, j = 0, 0

        # 2 pointers to each array, add the smallest to res until we reach end of one of the arrays
        while(i < m and j < n):
            if nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        
        # In case of residual elements in one array, add them to the result
        if i < m:
            while(i < m):
                res.append(nums1[i])
                i += 1

        if j < n:
            while(j < n):
                res.append(nums2[j])
                j += 1

        # copy res into nums1
        for i in range(m + n):
            nums1[i] = res[i]

