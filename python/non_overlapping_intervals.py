"""
Given a collection of intervals, find the minimum number of intervals you need to remove
to make the rest of the intervals non-overlapping.

Input: [ [1,2], [2,3], [3,4], [1,3] ]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
"""


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):

    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals = sorted(intervals, key=lambda x: x.start)
        curr_end = intervals[0].end
        erase = 0
        for interval in intervals[1:]:
            if interval.start < curr_end:
                erase += 1
                curr_end = min(curr_end, interval.end)
            else:
                curr_end = interval.end
        return erase


if __name__ == '__main__':
    print Solution().eraseOverlapIntervals([Interval(1,2), Interval(1,2), Interval(1,2)])
    print Solution().eraseOverlapIntervals([Interval(1,2), Interval(2,3), Interval(3,4), Interval(1,3)])
    print Solution().eraseOverlapIntervals([Interval(1,2), Interval(5,6), Interval(3,4)])
    print Solution().eraseOverlapIntervals([Interval(1,100), Interval(11,22), Interval(1,11), Interval(2,12)])