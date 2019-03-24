'''Given an array and a value, remove all the instances of that value in
the array.
Also return the number of elements left in the array after the operation.
It does not matter what is left beyond the expected length.

Example:
If array A is [4, 1, 1, 2, 1, 3] and value elem is 1,
then new length is 3, and A is now [4, 2, 3]
Try to do it in less than linear additional space complexity.
'''

# class Solution:
#     # @param A : list of integers
#     # @param B : integer
#     # @return an integer
#     def removeElement(self, A, B):
#         if not A:
#             return 0
#         if len(A) == 1 and A[0] == B:
#             return 0
#
#         left = 0
#         right = len(A)-1
#         while left<=right:
#             if A[left] !=  B:
#                 left += 1
#             else:
#                 A[left], A[right] = A[right], A[left]
#                 right -= 1
#         print A[:left]
#         return left
#
# if __name__ == '__main__':
#     A = [4, 1, 1, 2, 1, 3]
#     B = 1
#     # expected result:
#     # 0 1 0 3 1 0 0 0 1 0 0 3 3 1 1 3 3 0 3 0 1 0 0 3 3 0 3 0 3 3 1 3 3 0 3 3 0 3 3 0 0 0 0 1 3 0 3 1 3 1 0 3 3 3 3 3 3 3 3 1 3 1 0 0 0 1 0 3 1 0 3 0 1 1 3 0 1 1 3 3 0 1 1 3 1 1 3 0 1 0 1 3 1 3 1 1 0 0 3 0 1 1 1 3 0 3 3 0 3 0 1 3 0 0 1 3 1 1 0 0 3 0 1 1 0 1 0 0 0 1 1 0 3 3 0 1 3 0 0 1 0 1 0 0 0 0 3 0 0 1 0 3 0 3 3 3 0 3 3 1 0 1 1 0 0 3 1 1 3
#
#     print Solution().removeElement(A, B)

# working Solution in iq
class Solution:
# @param A : list of integers
# @param B : integer
# @return an integer
    def removeElement(self, A, B):
        ''' Maintain position of free slot.
            We shift any valid element in this slot.
        '''
        slot = 0
        for x in A:
            if x != B:
                # May replace an element by itself, nevermind.
                A[slot] = x
                slot += 1

        return slot

if __name__ == '__main__':
    A = [1, 4, 1, 1, 2, 1, 3]
    B = 1
    print Solution().removeElement(A, B)
