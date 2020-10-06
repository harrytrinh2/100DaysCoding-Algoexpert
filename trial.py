# O(n) time | O(1) space			
# --------------------------------------------------------
def moveElementToEnd(array, toMove):
	left  = 0
	right = len(array) - 1 # minus 1 because array starts from 0
	print("original_array",array)
	print(right,array[right])
	while left < right:
		if array[right] == toMove:
			right -= 1
		if array[left] != toMove:
			left += 1
		if array[left] == toMove and array[right] != toMove:
			array[left], array[right] = array[right], array[left]
	return array

print(moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2],2))