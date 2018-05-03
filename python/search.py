'''
Search Algorithms
* Binary Search
* Linear Search

					Time 		Space
Binary Search		O(logn)		O(1)
Linear Search		O(n)		O(1)
'''

def binarySearch(a, val):
	'''Binary search for sorted array'''
	low = 0
	high = len(a)-1
	while low <= high:
		mid = (low + high)//2
		if a[mid] == val:
			return mid
		elif a[mid] < val:
			low = mid + 1
		else:
			high = mid -1
	return -1 

def linearSearch(a, val):
	'''Sequential search for array'''
	for i in range(len(a)):
		if a[i]==val:
			return i
	return -1