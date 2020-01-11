'''
1. Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        table = dict()

        for index, num in enumerate(nums):
            if target-num in table:
                return [index, table[target-num]]
            else:
                table[num] = index

        return []

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    # Expected Result: [0, 1] or [1, 0]
    print Solution().twoSum(nums, target)