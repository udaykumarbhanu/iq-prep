'''Find the intersection of two sorted arrays.
OR in other words,
Given 2 sorted arrays, find all the elements which occur in both the arrays.

Example :

Input :
    A : [1 2 3 3 4 5 6]
    B : [3 3 5]

Output : [3 3 5]

Input :
    A : [1 2 3 3 4 5 6]
    B : [3 5]

Output : [3 5]
'''

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        result = []
        if not A or not B:
            return result

        first_left = 0
        first_right = len(A) - 1

        second_left = 0
        second_right = len(B) - 1

        while (first_left<=first_right and second_left<=second_right):
            if A[first_left] == B[second_left]:
                result.append(A[first_left])
                first_left += 1
                second_left += 1
            elif A[first_left] < B[second_left]:
                first_left += 1
            else:
                second_left += 1

        return result


if __name__ == '__main__':
    A = [1, 2, 3, 3, 4, 5, 6]
    B = [3, 5]
    print Solution().intersect(A, B)
