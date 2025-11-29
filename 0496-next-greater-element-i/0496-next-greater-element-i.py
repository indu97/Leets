class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = []
        for num in nums1:
            i = 0
            while(nums2[i]!= num):
                i += 1
            
            while(i < len(nums2)):
                if nums2[i] > num:
                    out.append(nums2[i])
                    break
                i += 1
            
            if i == len(nums2):
                out.append(-1)

        return out