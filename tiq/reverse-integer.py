"""
7. Reverse Integer
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        number_range = int(2**31)

        reverse = 0
        if x<0:
            x = -1*x
            while x>0:
                digit = x%10
                reverse = reverse*10 + digit
                x = x/10

            reverse = -1*reverse
        else:
            while x>0:
                digit = x%10
                reverse = reverse*10 + digit
                x = x/10

            reverse = reverse

        if reverse > number_range or reverse < -number_range:
            return 0
        else:
            return reverse

if __name__ == '__main__':
    x = -123
    # Expected output: -321
    print Solution().reverse(x)
