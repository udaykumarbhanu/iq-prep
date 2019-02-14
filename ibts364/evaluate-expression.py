class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        import operator
        numerals, operators = [], {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.div}

        for token in A:
            if token not in operators:
                numerals.append(int(token))
            else:
                y, x = numerals.pop(), numerals.pop()
                numerals.append(int(operators[token](x * 1.0, y)))
        return numerals.pop()

if __name__ == '__main__':
    A = [ "5", "1", "2", "+", "4", "*", "+", "3", "-" ]
    print Solution().evalRPN(A)
