'''
https://leetcode.com/discuss/interview-question/396769/
'''

class Solution(object):
    def maximum_time(self, time_str):
        tim = list(time_str)

        if tim[0] == "?":
            if tim[1] <= "3" or tim[1] == "?":
                tim[0] = "2"
            else:
                tim[0] = "1"

        if tim[1] == "?":
            if tim[0] == "2":
                tim[1] = "3"
            else:
                tim[1] = "9"

        if tim[3] == "?":
            tim[3] = "5"
        if tim[4] == "?":
            tim[4] = "9"

        return "".join(tim)


if __name__ == '__main__':
    time_str = "?1:??"
    print Solution().maximum_time(time_str)
