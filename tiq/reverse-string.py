'''344. Reverse String
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.



Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
'''
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(s)-1

        while start<end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

        # return s

if __name__ == '__main__':
    s = ["h","e","l","l","o"]
    # Expected output: None (in-place modification)
    print Solution().reverseString(s)
