# Sort all even numbers in ascending order and then sort all odd numbers in descending order

# Input  : arr[] = {1, 2, 3, 5, 4, 7, 10}
# Output : arr[] = {7, 5, 3, 1, 2, 4, 10}


def sort_odd_even_nums(arr):
	start_index = 0
	end_index = len(arr) - 1

	# count the odd numbers in the array.
	odd_count = 0
	while start_index < end_index:

		# Check if current element is odd, keep increasing the start index.
		if arr[start_index] & 1 == 1:
			start_index += 1
			odd_count += 1

		# Check if current element is even, keep decreasing the end index.
		if arr[end_index] & 1 == 0:
			end_index -= 1

		# swap the odd and even element if they are at wrong position.
		if start_index < end_index:
			arr[start_index], arr[end_index] = arr[end_index], arr[start_index]

	# print arr, odd_count
	
	odd_arr = arr[: odd_count]
	odd_arr.sort(reverse=True)
	even_arr = arr[odd_count: ]
	even_arr.sort()

	odd_arr.extend(even_arr)

	return odd_arr


def sort_odd_even_nums_2(arr):
	# Make all the odd number as negative odd number. 
	for i in range(len(arr)):
		if arr[i] & 1 == 1:
			arr[i] = -(arr[i])

	# print arr
	
	# Now sort the array.
	arr.sort()

	# Revert odd numbers from negative odd to postive odd number. 
	for i in range(len(arr)):
		if arr[i] & 1 == 1:
			arr[i] = -(arr[i])


	return arr


if __name__ == '__main__':
	arr = [1, 2, 3, 5, 4, 7, 10]
	print sort_odd_even_nums(arr)

	print sort_odd_even_nums_2(arr)
