'''Given an array of strings, return all groups of strings that are anagrams.
Represent a group by a list of integers representing the index in the original
list. Look at the sample case for clarification.
'''
class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        import collections
        group_anagrams = collections.defaultdict(list)

        for index, s in enumerate(A):
            group_anagrams[tuple(sorted(s))].append(index+1)

        return group_anagrams.values()

if __name__ == '__main__':
    A = [ "abcd", "dcba", "dcba", "abcd", "abcd", "adbc", "dabc", "adcb" ]
    print Solution().anagrams(A)
