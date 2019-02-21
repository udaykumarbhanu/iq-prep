'''Given an integer, convert it to a roman numeral, and return a string corresponding to its roman numeral version

Input is guaranteed to be within the range from 1 to 3999.

Example :

Input : 5
Return : "V"

Input : 14
Return : "XIV"
'''

class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
        numeral_dict = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL",
            50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM",
            1000: "M"}

        result = []
        key_set = sorted(numeral_dict.keys())

        while A>0:
            for key in reversed(key_set):
                while A/key > 0:
                    A -= key
                    result += numeral_dict[key]

        return "".join(result)


if __name__ == '__main__':
    A = 14
    print Solution().intToRoman(A)
