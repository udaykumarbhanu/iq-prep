'''Given two binary strings, return their sum (also a binary string).

Example:

a = "100"

b = "11"
Return a + b = "111".
'''
class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        carry = 0
        result = ""
        for i in xrange(max(len(A), len(B))):
            val = 0
            if i<len(A):
                print A[-i], i
                val = carry + int(A[-i])
            if i<len(B):
                val = carry + int(B[-i])

            carry = val%10
            result += str(val/10)

        if carry:
            result = str(carry) + result

        return result

if __name__ == '__main__':
    A = "100"
    B = "111"

    print Solution().addBinary(A, B)
