class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        import operator as op
        operators = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.div}

        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                y, x = int(stack.pop()), int(stack.pop())
                stack.append(int(operators[token](x, y)))

        return int(stack.pop())

if __name__ == '__main__':
    A = [ "4", "13", "5", "/", "+" ]
    print Solution().evalRPN(A)
