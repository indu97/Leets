class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # res = []
        # i, j = 0, 0

        # # 2 pointers to each array, add the smallest to res until we reach end of one of the arrays
        # while(i < m and j < n):
        #     if nums1[i] <= nums2[j]:
        #         res.append(nums1[i])
        #         i += 1
        #     else:
        #         res.append(nums2[j])
        #         j += 1
        
        # # In case of residual elements in one array, add them to the result
        # if i < m:
        #     while(i < m):
        #         res.append(nums1[i])
        #         i += 1

        # if j < n:
        #     while(j < n):
        #         res.append(nums2[j])
        #         j += 1

        # # copy res into nums1
        # for i in range(m + n):
        #     nums1[i] = res[i]

        # Solution 2:
        # Start comparing the ends of both arrays, move the largest to the end of nums1 until you reach end of nums2

        i, j = m - 1, n - 1 
        write_ptr = m + n - 1
        while(j >= 0 and i >=0):
            print(write_ptr)
            if nums1[i] <= nums2[j]:
                nums1[write_ptr] = nums2[j]
                j -= 1
            else:
                nums1[write_ptr] = nums1[i]
                i -= 1
            write_ptr -= 1

        # In case of residual elements in nums2, move them 
        if j >= 0:
            while(j >= 0):
                nums1[write_ptr] = nums2[j]
                write_ptr -= 1
                j -= 1