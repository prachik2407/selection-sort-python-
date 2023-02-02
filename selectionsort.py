def selectionSort(array, size):
	for i in range(size):
		min_index = i
		for j in range(i + 1, size):
			if array[j] < array[min_index]:                             #for selecting the minimum value
				min_index = j
		(array[i], array[min_index]) = (array[min_index], array[i])     #for swapping the value 
arr = [45, 0, 11, 88, 6, 34, 56, 23, 65]
size = len(arr)
selectionSort(arr, size)
print('The array after sorting is:')
print(arr)