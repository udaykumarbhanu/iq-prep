# 78. Subsets
'''Given a set of distinct integers, nums, return all possible subsets (the power set).

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
'''
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if not nums: return result

        nums.sort()
        # backtrack(input_array, result, temp_array, start_index)
        self.backtrack(nums, result, [], 0)
        return result

    def backtrack(self, nums, result, temp_result, start_index):
        result.append(temp_result[:])

        for index in xrange(start_index, len(nums)):
            temp_result.append(nums[index])
            self.backtrack(nums, result, temp_result, index+1)
            temp_result.pop(len(temp_result)-1)

if __name__ == '__main__':
    nums = [1, 2, 3]
    print Solution().subsets(nums)
