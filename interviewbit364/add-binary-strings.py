'''Given two binary strings, return their sum (also a binary string).

Example:

a = "100"

b = "11"
Return a + b = “111”.
'''

class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        if A is '':
            return B

        elif B is '':
            return A
        elif A is '' and B is '':
            return A
        else:
            a = A[::-1]
            b = B[::-1]
            m = len(a)-1
            n = len(b)-1
            i = j = 0

            carry = 0

            res = []
            while i<=m and j<=n:
                num = carry + int(a[i]) + int(b[j])
                res.append(str(num%10))
                carry = num/10
                i += 1
                j += 1

            while i<=m:
                num = carry + int(a[i])
                res.append(str(num%10))
                carry = num/10
                i += 1

            while j<=n:
                num = carry + int(b[j])
                res.append(str(num%10))
                carry = num/10
                j += 1

            if carry:
                res.append(carry)

            res = res[::-1]

            return ''.join(res)
if __name__ == "__main__":
    A = "100"
    B = "11"
    print Solution().addBinary(A, B)
