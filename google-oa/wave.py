'''
https://www.interviewbit.com/problems/wave-array/

Given an array of integers, sort the array into a wave like array and return it,
In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5.....

Example

Given [1, 2, 3, 4]

One possible answer : [2, 1, 4, 3]
Another possible answer : [4, 1, 3, 2]
'''


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        if len(A) == 1: return A

        A.sort()

        n = len(A)

        A1 = A[:n/2]
        A2 = A[n/2:]

        B = zip(A1, A2)
        print type(B)
        result = []
        for a, b in B:
            result.append(a)
            result.append(b)
        return result

        # for i in range(0, n, 2):
        #     if i + 1 < n:
        #         A[i], A[i + 1] = A[i + 1], A[i]
        #
        # return A


if __name__ == '__main__':
    A = [1, 2, 3, 4]
    print Solution().wave(A)