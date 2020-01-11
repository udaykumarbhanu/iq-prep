'''
https://leetcode.com/discuss/interview-question/398026/

Given a string S consisting of N letters a and b. In one move you can replace one letter by the other (a by b or b by a).

Write a function solution that given such a string S, returns the minimum number of moves required to obtain a string
containing no instances of three identical consecutive letters.

Example 1:

Input: "baaaaa"
Output: 1
Explanation: The string without three identical consecutive letters which can be obtained is one move is "baabaa".
Example 2:

Input: "baaabbaabbba"
Output: 2
Explanation: There are four valid strings obtainable in two moves, for example "bbaabbaabbaa".
Example 3:

Input: "baabab"
Ouput: 0
Assumptions:

N is an integer within the range [0, ..200,000];
string S consists of only characteres a and b.
'''

class Solution(object):
    def minMoves(self, s):
        if not s:
            return 0

        moves = 0
        for i in range(len(s)):
            running_length = 1
            j = i
            while j + 1 < len(s) and s[j] == s[j+1]:
                running_length += 1
                j += 1

            moves += running_length/3

        return moves


if __name__ == '__main__':
    s = "baaaaa"
    print  Solution().minMoves(s)

    s = "baaabbaabbba"
    print  Solution().minMoves(s)

    s = "baabab"
    print  Solution().minMoves(s)
