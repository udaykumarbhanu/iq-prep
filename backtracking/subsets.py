"""LC: 78. Subsets
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return []

        result = []
        self.backtrack(nums, result, [], 0)

        return result


    def backtrack(self, nums, result, temp, start_index):
        result.append(temp[:])

        for i in range(start_index, len(nums)):
            temp.append(nums[i])
            self.backtrack(nums, result, temp, i + 1)

            temp.pop(-1)


if __name__ == '__main__':
    nums = [1, 2, 3]
    print Solution().subsets(nums)