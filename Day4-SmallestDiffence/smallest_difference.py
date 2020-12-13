# O(n^2) time | O(1) space
def smallestDifference(arrayOne, arrayTwo):  
    # Write your code here.
	smallest_pair= [None,None]
	smallest_value = None
	for arrOneIdx in  range(0,len(arrayOne),1):
		for arrTwoIdx in range(0,len(arrayTwo),1):
			abs_diff = abs(arrayOne[arrOneIdx] - arrayTwo[arrTwoIdx])
			if arrOneIdx == 0 and arrTwoIdx == 0:
				smallest_value = abs_diff
				continue
			if  abs_diff < smallest_value:
				smallest_value = abs_diff 
				smallest_pair[0] = arrayOne[arrOneIdx]
				smallest_pair[1] = arrayTwo[arrTwoIdx]
	return smallest_pair

# O(n^2) time | O(1) space 
# float('inf'), float('-inf')
 def smallestDifference(arrayOne, arrayTwo):  
    # Write your code here.
    smallest = [float('inf'), float('-inf')]
    for one in arrayOne:
        for two in arrayTwo:
            if abs(smallest[0] - smallest[1]) > abs(one - two):
                smallest = [one, two]
    return smallest