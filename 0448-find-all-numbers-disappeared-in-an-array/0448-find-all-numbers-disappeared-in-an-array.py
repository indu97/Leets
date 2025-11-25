class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        keyToFreq = defaultdict(int)

        for num in nums:
            keyToFreq[num] += 1
        
        out = []
        for i in range(1, len(nums)+1):
            if keyToFreq[i] == 0:
                out.append(i)

        return out
            