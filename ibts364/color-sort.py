'''Given an array with n objects colored red, white or blue,
sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
'''

class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        low = 0
        high = len(A)-1
        mid = 0

        while mid<=high:
            if A[mid] == 0:
                A[low], A[mid] = A[mid], A[low]
                low += 1
                mid += 1
            elif A[mid] == 1:
                mid += 1
            else:
                A[mid], A[high] = A[high], A[mid]
                high -= 1

        return A

print Solution().sortColors(A=[0, 1, 2, 1, 0, 1, 2, 2, 0])
