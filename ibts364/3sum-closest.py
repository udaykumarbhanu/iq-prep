'''Given an array S of n integers, find three integers in S such that the sum
is closest to a given number, target.
Return the sum of the three integers.

Assume that there will only be one solution

Example:
given array S = {-1 2 1 -4},
and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        A.sort()
        first = 0
        third = len(A) - 1
        result = A[0] + A[1] + A[2]

        while first < third - 1:
            second = first + 1
            third = len(A) - 1
            while second < third:
                temp = A[first] + A[second] + A[third]
                if abs(B-temp) < abs(B-result):
                    result = temp

                if temp < B:
                    second += 1
                else:
                    third -= 1

            first += 1
        return result

if __name__ == '__main__':
    A =[-1, 2, 1, -4]
    B = 1
    print Solution().threeSumClosest(A, B)
