'''Remove duplicates from Sorted Array
Given a sorted array, remove the duplicates in place such that each element
appears only once and return the new length.
Note that even though we want you to return the new length, make sure to change
the original array as well in place

Do not allocate extra space for another array, you must do this in place with
constant memory.
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if  not A:
            return 0

        start = 0
        i = 1
        while i<len(A):
            if A[start] != A[i]:
                start += 1
                A[start] = A[i]
                i += 1
            else:
                i += 1
        return start + 1

if __name__ == '__main__':
    A = [1,1,2]
    print Solution().removeDuplicates(A)
