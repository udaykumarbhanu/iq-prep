'''Implement int sqrt(int x).

Compute and return the square root of x.

If x is not a perfect square, return floor(sqrt(x))

Example :

Input : 11
Output : 3
'''

class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):

        # base case
        if A == 0 or A == 1:
            return A

        start = 1
        end = A

        while start <= end:
            mid = (start + end)/2

            if mid * mid == A:
                return mid
            elif mid * mid < A:
                start = mid + 1
                result = mid
            else:
                end = mid - 1

        return result

if __name__ == '__main__':
    A = 11
    print Solution().sqrt(A)
