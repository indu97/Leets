from collections import defaultdict
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def translate_integer(nums: int) -> int:
            res = 0
            for c in str(num):
                res = res * 10 + mapping[int(c)]
            return res

        res_list: dict[int, int] = {}
        for num in nums:
            res_list[num] = translate_integer(num)
        nums.sort(key=lambda val: res_list[val])
        return nums