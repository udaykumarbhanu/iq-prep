'''Given an array S of n integers, are there elements a, b, c in S such
that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
The solution set must not contain duplicate triplets. For example, given
array S = {-1 0 1 2 -1 -4},
A solution set is:
(-1, 0, 1)
(-1, -1, 2)
'''
class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        result = []
        if len(A)<3:
            return result

        A.sort()
        first = 0
        third = len(A) - 1

        while first<third-1:
            second = first + 1
            third = len(A) - 1
            while second<third:
                temp = A[first] + A[first + 1] + A[third]
                if temp == 0:
                    result.append([A[first], A[first + 1], A[third]])
                    first += 1
                    third -= 1
                    while second<third and A[second] == A[second-1]:
                        second += 1
                    while second<third and A[third] == A[third+1]:
                        third -= 1
                elif temp<0:
                    first += 1
                else:
                    third -= 1
                    
            first += 1

        return result

if __name__ == '__main__':
    A = [-1, 0, 1, 2, -1, -4]
    print Solution().threeSum(A)
