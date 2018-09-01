# Given a sorted array arr[] of n elements, write a function to search a given element 
# target in arr[].

# Time Complexity: O(log(n))
# Space Complexity: O(1)

def binary_search_iter(arr, left, right, target):
	while(left<=right):
		mid = left + (right-left)//2
		if arr[mid]==target:
			return mid
		elif arr[mid]<target:
			left = mid + 1
		else:
			right = mid - 1

	# for condition: left>right OR target not found.
	return -1


def binary_search_rec(arr, left, right, target):
	if right>=left:
		mid = left + (right-left)//2

		if arr[mid]==target:
			return mid
		elif arr[mid]<target:
			return binary_search_rec(arr, mid+1, right, target)
		else:
			return binary_search_rec(arr, left, mid-1, target)

	# When left>right OR target not found in whole array.
	return -1

if __name__ == '__main__':
	arr = [0, 1, 2, 3, 4, 6]
	left = 0
	right = len(arr) - 1
	target = 4 
	print binary_search_iter(arr, left, right, target)

	print binary_search_rec(arr, left, right, target)



