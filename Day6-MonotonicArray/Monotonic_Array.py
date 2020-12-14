# 0(n) time | O(1) space
def isMonotonic(array):
    # Write your code here.
	isNonDecreasing = True
	isNonIncreasing = True
    for i in range(0, len(array)-1):
		if array[i] < array[i+1]:
			isNonDecreasing = False
		if array[i] > array[i+1]:
			isNonIncreasing = False
	return isNonIncreasing or isNonDecreasing
# return True or False -> kq la True


# 0(n) time | O(1) space
def isMonotonic(array):
    # Write your code here
	if len(array) <=2:
		return True
	for i in range(1, len(array)-1):
		prev_element = array[i-1]
		curr_element = array[i]
		next_element = array[i+1]
		if prev_element <= curr_element <= next_element or prev_element >= curr_element >= next_element:
			continue
		else:
			return False
	return True


# isMonotonic[-1, -5, -10, -1100, -1101, -1102, -9001]
# result= True