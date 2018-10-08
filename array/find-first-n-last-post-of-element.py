'''Given a sorted array with possibly duplicate elements, the task is to 
find indexes of first and last occurrences of an element x in the given 
array.
'''

# modified version of binary search.
def first(arr, low, high, x):
	if high>=low:
		mid = (low+high)/2

		if (arr[mid] == x and (mid == 0 or x>arr[mid-1])):
			return mid
		elif x>arr[mid]:
			return first(arr, mid+1, high, x)
		else:
			return first(arr, low, mid-1, x)

	return -1


def last(arr, low, high, x) : 
	if high>=low: 
		mid = (low+high)/2

		if (arr[mid] == x and (mid == high or x<arr[mid+1])): 
			return mid 
		elif x < arr[mid]: 
			return last(arr, low, mid-1, x) 
		else : 
			return last(arr, mid+1, high, x) 
			
	return -1



if __name__ == '__main__':
	arr = [1, 3, 5, 5, 5, 5, 67, 123, 125]
	
	x = 5
	low = 0 
	high = len(arr)-1

	print 'First occurrence of {} is {}'.format(x, first(arr, low, high, x))

	print 'Last occurrence of {} is {}'.format(x, last(arr, low, high, x))

