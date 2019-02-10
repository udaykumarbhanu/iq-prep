'''Problem: Given an m x n matrix, find all common elements present in 
	all rows in O(mn) time and one traversal of matrix.
'''


def common_elements_in_all_rows(mat, m, n):
	first_row_dict = {data : 1 for data in set(mat[:][0])}
	# print first_row_dict

	for row in range(1, m):
		for col in range(n):
			if first_row_dict[mat[row][col]] == i:
				first_row_dict[mat[row][col]] = i + 1

	for k, v in first_row_dict.iteritems():
		if v != 1:
			print k


if __name__ == '__main__':

	mat = [[1, 2, 1, 4, 8],
	   [3, 7, 8, 5, 1],
	   [8, 7, 7, 3, 1],
	   [8, 1, 2, 7, 9]]

	m = len(mat[:])
	n = len(mat[:][0])

	# print m, n

	common_elements_in_all_rows(mat, m, n)