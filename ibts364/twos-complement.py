class Solution(object):
    def bitwiseComplement(self, N):
        """pwd

        :type N: int
        :rtype: int
        """
        if not N:
            return 1

        result = 0
        power = 1

        while N>0:
            result += (N%2 ^ 1) * power
            power <<= 1
            N >>= 1

        return result

if __name__ == '__main__':
    N = 5
    # result: 2
    print Solution().bitwiseComplement(N)
