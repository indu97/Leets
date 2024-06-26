import numpy as np
from collections import Counter
class Solution:
    def heightChecker(self, h: List[int]) -> int:
        return sum(v != u for v,u in zip(h,sorted(h)))
