# 0(n) time | O(1) space
def isMonotonic(array):
    # Write your code here
	if len(array) ==2:
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
