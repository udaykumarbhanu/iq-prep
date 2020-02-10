'''
https://www.interviewbit.com/problems/merge-intervals/

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].

Example 2:

Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] would result in [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

Make sure the returned intervals are also sorted.
'''


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        if not intervals: return [new_interval]

        intervals.append(new_interval)
        intervals.sort(key=lambda x: x.start)
        # print intervals

        result = []
        result.append(intervals[0])
        for i in range(1, len(intervals)):
            if result[-1].end > intervals[i].start:
                result[-1].end = max(result[-1].end, intervals[i].end)
            else:
                result.append(intervals[i])

        return result


if __name__ == '__main__':
    intervals = [[1, 3], [6, 9]]
    new_interval = [2, 5]

    print Solution().insert(intervals, new_interval)