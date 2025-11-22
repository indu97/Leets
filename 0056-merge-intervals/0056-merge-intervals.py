class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        
        mergedIntervals = []
        intervals.sort()
        for interval in intervals:
            start = interval[0]
            end = interval[1]
            if not mergedIntervals or start > mergedIntervals[-1][1]:
                mergedIntervals.append(interval)
            else:
                mergedIntervals[-1][1] = max(mergedIntervals[-1][1], end)

        return mergedIntervals
