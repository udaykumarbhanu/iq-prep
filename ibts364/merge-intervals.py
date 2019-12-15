# 56. Merge Intervals

'''Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default
code definition to get new method signature.
'''

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals: return []

        result = []
        # sort input based on first item of the input List
        sorted_intervals = sorted(intervals, key=lambda x: x[0])

        result.append(sorted_intervals[0])
        for new_interval in sorted_intervals[1:]:

            # if start of new_interval <= last value of last item of result
            if new_interval[0]<= result[-1][-1]:
                result[-1][-1] = max(result[-1][-1], new_interval[-1])
            else:
                result.append(new_interval)

        return result

if __name__ == '__main__':
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print 'input intervals :', intervals

    print 'Output :'
    print Solution().merge(intervals)
