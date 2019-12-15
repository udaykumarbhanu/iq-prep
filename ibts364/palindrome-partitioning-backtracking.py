class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        if not s: return [[]]

        self.backtrack(s, result, [], 0)
        return result

    def is_palindrome(self, s, si, ei):
        # print s[si:ei] == s[si:ei:-1], s[si:ei]
        return s[si:ei] == s[si:ei:-1]

    def backtrack(self, s, result, temp, si):
        #print temp, result
        if si == len(s):
            result.append(temp[:])
            return
        else:
            for i in range(si, len(s)):
                if self.is_palindrome(s, si, i+1):
                    temp.append(s[si:i+1])
                    self.backtrack(s, result, temp, i+1)
                    # print temp, result
                    temp.pop(-1)

if __name__ == '__main__':
    s = 'aab'
    print Solution().partition(s)
