
def firstDuplicateValue(array):
	# Write your code here.
	for i in range(0,len(array),1):
		if array[i] < 0:
			return abs(array[i])
		idx = abs(array[i]) -1
		array[idx] = - array[i] 
	print(array)
	return -1


print(firstDuplicateValue([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]))
print(firstDuplicateValue([2, 1, 1]))