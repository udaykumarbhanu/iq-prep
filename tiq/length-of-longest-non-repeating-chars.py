'''
3. Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = dict()
        start = max_length = 0

        if not s:
            return max_length

        for index, char in enumerate(s):
            # when new upcoming character is IN table.
            if char in table and start <= table[char]:
                start = table[char] + 1
            # when new upcoming character is NOT IN table.
            else:
                max_length = max(max_length, index-start + 1)

            # For both the case update the table, character: index pair
            table[char] = index

        return max_length

if __name__ == '__main__':
    s = "pwwkew"
    # Expected Output: 3
    print Solution().lengthOfLongestSubstring(s)
