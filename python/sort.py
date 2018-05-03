'''
Sorting Algorithms
* Bubble Sort
* Insertion Sort
* Selection Sort
* Merge Sort
* Quick Sort
* Heap Sort

					Time  								Space
					Worst   	Avg 		Best 		

Bubble Sort 		O(n^2)		O(n^2)		O(n)		O(1)
Insertion Sort		O(n^2)		O(n^2)		O(n)		O(1)
Selection Sort		O(n^2)		O(n^2)		O(n^2)		O(1)

Merge Sort 			O(nlogn)	O(nlogn)	O(nlogn)	O(n)
Quick Sort 			O(n^2)		O(nlogn)	O(nlogn)	O(logn)
Heap Sort 			O(nlogn)	O(nlogn)	O(nlogn)	O(1)


Reference:
http://www.geeksforgeeks.org/sorting-algorithms/#algo
http://www.geeksforgeeks.org/know-sorting-algorithm-set-1-sorting-weapons-used-programming-languages/
'''
import random

def bubbleSort(a):
	'''
	Bubble up the largest element to the end.
	Repeatedly swap the adjacent elements if they are in wrong order until no more swap occus for an iteration.
	Time: O(n^2) avg/worst, O(1) best
	Space: O(1)
	'''
	for i in range(len(a)):
		swap = False
		for j in range(len(a)-i-1):
			if a[j] > a[j+1]:
				a[j], a[j+1] = a[j+1], a[j]
				swap = True
		if swap == False: break
	return a

def insertionSort(a):
    '''
    Like we sort playing cards in our hands - insert the smallest to the front.
    Pick an element a[i] and insert it into sorted sequence a[0:i-1] for i =1 to n-1
    Time: O(n^2) avg/worst, O(1) best
    Space: O(1)
    '''
    for i in range(1, len(a)):
        key = a[i]
        j = i-1
        while j >=0 and key < a[j] :
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a

def selectionSort(a):
	'''
	Repeatedly find smallest element from remaining unsorted array, and put it at the beginning.
	Time: O(n^2) avg/worst, O(n) best
	Space: O(1)
	'''
	for i in range(len(a)):
		min_index = i
		for j in range(i+1, len(a)):
			if a[min_index] > a[j]:
				min_index = j
		a[i], a[min_index] = a[min_index], a[i]
	return a

def mergeSort(a):
	'''
	Use recursion. 
	Repeatedly divide array in half, sort each of the halves, and merge them.
	Time: O(nlogn) avg/worst
	Space: O(n)
	'''
	if len(a)<=1:
		return a
	mid = len(a)//2
	left = mergeSort(a[:mid])
	right = mergeSort(a[mid:])
	_merge(left, right, a)
	return a

def _merge(left, right, a):
	'''Helper method for mergeSort'''
	i = j = k = 0
	while i<len(left) and j<len(right):
		if left[i]<right[j]:
			a[k]=left[i]
			i+=1
		else:
			a[k]=right[j]
			j+=1
		k+=1

	while i<len(left):
		a[k]=left[i]
		i+=1
		k+=1

	while j<len(right):
		a[k]=right[j]
		j+=1
		k+=1
	# print("Checking",i,j,k, a)


def quickSort(a):
	'''
	Use divide and conquer. 
	Repeatedly pick a random (or first or last) element as pivot, 
	and partiion the array with smaller elements before pivot and larger elements after the pivot
	Time: O(n^2) avg/worst , O(nlogn) best
	Space: O(logn)
	'''
	_quicksort(a, 0, len(a)-1)
	return a

def _quicksort(a, start, end):
	'''Helper method for quickSort'''
	if start>=end:
		return a
	# pivot = start
	# pivot = end
	pivot = random.randrange(start, end+1)
	new_pivot = _partition(a, start, end, pivot)
	_quicksort(a, start, new_pivot)
	_quicksort(a, new_pivot+1, end)

def _partition(a, start, end, pivot):
	'''
	Helper method for quickSort
	Idea: First, move the pivot to the end, 
	repeatedly move 'smaller element' to the front,
	move back the pivot just behind the last 'smaller elements'
	'''
	a[pivot], a[end] = a[end], a[pivot]
	index = start
	for i in range(start, end):
		if a[i]<a[end]:
			a[i], a[index] = a[index], a[i]
			index += 1
	a[index], a[end] = a[end], a[index]
	return index


def heapSort(a):
	'''
	The heap-sort algorithm converts the input array a into a max heap and then repeatedly extracts the max value.

	Build a max heap from the input data.
	At this point, the largest item is stored at the root of the heap. 
	Replace it with the last item of the heap followed by reducing the size of heap by 1. 
	Finally, heapify the root of tree.
	Repeat above steps while size of heap is greater than 1.
	'''
	n = len(a)

	# build a max heap from a (heapify subtree in top-down manner)
	for i in range(n, -1, -1):
		_heapify(a, n, i)
		# print(i, "checking max heap", a)

	# one by one extract max elements (swap the root with the last element, 
	# then heapify subtree at root with reduced size, so that we could have inplace sorting)
	for i in range(n-1, 0, -1):
		a[i], a[0] = a[0], a[i]
		_heapify(a, i, 0)

	return a

def _heapify(a, n, i):
	'''
	Helper method for heapSort
	Use recursion. Heapify subtree of size n rooted at index i.
	'''
	largest = i 
	l = 2*i+1
	r = 2*(i+1)
	if l<n and a[i]<a[l]:
		largest = l
	if r<n and a[largest]<a[r]:
		largest = r
	if largest != i:
		a[i], a[largest] = a[largest], a[i]
		_heapify(a, n, largest)

