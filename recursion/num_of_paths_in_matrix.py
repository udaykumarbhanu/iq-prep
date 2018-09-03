# Count all possible paths from top left to bottom right of a mXn matrix.

'''
Solution using Recursion.
Time complexity: O(2^n) exponential
Space: O(2^n)
'''

def number_of_paths(m, n):
	if m == 1 or n == 1:
		return 1

	return number_of_paths(m-1, n) + number_of_paths(m, n-1)


if __name__ == '__main__':
	m = 3
	n = 3

	print number_of_paths(m, n)
	
