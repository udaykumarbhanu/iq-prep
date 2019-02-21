'''Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

Read more details about roman numerals at Roman Numeric System

Example :

Input : "XIV"
Return : 14
'''

class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        numeral_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M": 1000}

        result = 0
        for i in xrange(len(A)):
            if i > 0 and numeral_dict[A[i]] > numeral_dict[A[i - 1]]:
                result += numeral_dict[A[i]] - 2 * numeral_dict[A[i - 1]]
                # print i, A[i], numeral_dict[A[i]] - 2 * numeral_dict[A[i - 1]], result
            else:
                result += numeral_dict[A[i]]
                # print i, A[i], numeral_dict[A[i]], result

        return result
if __name__ == '__main__':
    A = "XIV"
    print Solution().romanToInt(A)
