'''
https://www.geeksforgeeks.org/majority-element/
Write a function which takes an array and prints the majority element (if it exists), otherwise prints "No Majority Element".
'''

import collections
import sys

def majority_element(arr):
	counter = collections.Counter(arr)
	key, value = counter.most_common(1)[0]
	
	if value >= len(arr)/2:
		print key
	else:
		print 'No majority element is present!'


def majority_element2(arr):
	d = dict()
	
	for item in arr:
		d[item] = d.get(item, 0) + 1

	max_value = max_key = -sys.maxsize

	for v, k in d.iteritems():
		if v > max_value:
			max_value = v
			max_key = k


	if v >= len(arr)/2:
		print k
	else:
		print 'No majority element is present!'



if __name__ == '__main__':
	majority_element([2,2,2,2,5,5,2,3,3])
	majority_element2([2,2,2,2,5,5,2,3,3])
