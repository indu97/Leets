class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)
        start, end = newInterval

        # 1) Add all intervals that end before newInterval starts
        while i < n and intervals[i][1] < start:
            res.append(intervals[i])
            i += 1

        # 2) Merge all intervals that overlap with newInterval
        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        res.append([start, end])

        # 3) Add the rest (intervals completely after)
        while i < n:
            res.append(intervals[i])
            i += 1

        return res

