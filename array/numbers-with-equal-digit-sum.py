# https://leetcode.com/discuss/interview-question/365872/

def numbers_with_equal_digit_sum(nums):
	if not nums:
		return -1 

	table = dict()
	result = -1

	for num in nums:
		total = 0
		num_copy = num
		while num > 0:
			total += num%10
			num /= 10
		
		if total not in table:
			table[total] = num_copy
		else:
			result = max(result, table[total] + num_copy)
			table[total] = max(num_copy, table[total])
			
	return result


if __name__ == '__main__':
	A = [51, 71, 17, 42]
	print numbers_with_equal_digit_sum(A)