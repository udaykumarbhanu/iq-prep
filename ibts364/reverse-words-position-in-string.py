class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, A):
        words = A.split()
        words = words[::-1]

        return ' '.join(words)

if __name__ == '__main__':
    A = "the sky is blue"
    print Solution().reverseWords(A)
