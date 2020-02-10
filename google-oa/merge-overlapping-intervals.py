'''
https://www.interviewbit.com/problems/merge-overlapping-intervals/

Given a collection of intervals, merge all overlapping intervals.

For example:

Given [1,3],[2,6],[8,10],[15,18],

return [1,6],[8,10],[15,18].

Make sure the returned intervals are sorted.
'''


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        if not intervals: return intervals

        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            if result[-1][-1] > intervals[i][0]:
                result[-1][-1] = max(result[-1][-1], intervals[i][-1])
            else:
                result.append(intervals[i])

        return result


if __name__ == '__main__':
    intervals = [[1,3],[2,6],[8,10],[15,18]]

    print Solution().merge(intervals)
