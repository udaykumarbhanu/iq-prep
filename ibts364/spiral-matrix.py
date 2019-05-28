class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = list()

        if not matrix:
            return result

        rs = 0
        re = len(matrix)-1
        cs = 0
        ce = len(matrix[0])-1

        while rs <= re and cs <= ce:

            #left to right row-wise traverse.
            for col in range(cs, ce+1):
                result.append(matrix[rs][col])

            #move to next row
            rs += 1

            #top to bottom column-wise traverse.
            for row in range(rs, re+1):
                result.append(matrix[row][ce])

            #reduce columns of matrix
            ce -= 1

            #rigth to left row-wise traverse.
            if rs<=re:
                for col in reversed(range(cs, ce+1)):
                    result.append(matrix[re][col])

                #reduce rows of matrix
            re -= 1

            #bottom to top column-wise traverse.
            if cs<=ce:
                for row in reversed(range(rs, re+1)):
                    result.append(matrix[row][cs])

            #decrease columns from left side of matrix.
            cs += 1

        return result


if __name__ == '__main__':
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print Solution().spiralOrder(matrix)
