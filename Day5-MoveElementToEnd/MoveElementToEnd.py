# O(n^2) time | O(1) space
def moveElementToEnd(array, toMove):
    # Write your code here.
	final_Array = []
	count=0
	for element in array:
		if element == toMove:
			count+=1
		else:
			final_Array.append(element)
	for i in range(0,count):
		final_Array.append(toMove)
	return final_Array
# O(n) time | O(1) space			
# --------------------------------------------------------
def moveElementToEnd(array, toMove):
    left, right = 0, len(array) - 1
	while left < right:
		if array[right] == toMove:
			right -= 1
		if array[left] != toMove:
			left += 1
		if array[left] == toMove and array[right] != toMove:
			array[left], array[right] = array[right], array[left]
	return array