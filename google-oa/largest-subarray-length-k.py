'''
https://leetcode.com/discuss/interview-question/352459/

'''

class Solution(object):
    def largest_subarray_lenth_k(self, A, k):
        if k == 1:
            return max(A)

        first_index = 0
        for i in xrange(1, len(A) - k + 1):
            if A[first_index] < A[i]:
                first_index = i

        return A[first_index: first_index + k]



if __name__ == '__main__':
    A = [1, 4, 3, 2, 5]
    k = 4

    print Solution().largest_subarray_lenth_k(A, k)
