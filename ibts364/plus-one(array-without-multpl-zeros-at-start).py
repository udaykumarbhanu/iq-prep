'''Given a non-negative number represented as an array of digits,

add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.

Example:

If the vector has [1, 2, 3]

the returned vector should be [1, 2, 4]

as 123 + 1 = 124.
'''

class Solution:
    # @param A : list of integers
    # @return a list of integers

    def plusOne(self, A):
        n = len(A)

        for index in range(n-1, -1, -1):
            if A[index] < 9:
                A[index] += 1

                # Case1: [1, 2, 3]
                return A
            else:
                # Case2: [1, 2, 9]
                A[index] = 0

        # Case3: [9, 9, 9]
        A.insert(0, 1)

        return A

if __name__ == '__main__':
    A = [9, 9, 9]
    print Solution().plusOne(A)
