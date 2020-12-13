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


# O(nlog(n) + mlog(m)) time (because the length of the two arrays are different)| O(1) space 
def smallestDifference(arrayOne, arrayTwo):
	arrayOne, arrayTwo = sorted(arrayOne), sorted(arrayTwo)
    smallest=[float("inf"), float("-inf")]
	arrOneIdx, arrTwoIdx  = 0 , 0
	while ((arrOneIdx < len(arrayOne)) and  (arrTwoIdx < len(arrayTwo))):
		if abs(smallest[0]-smallest[1]) > abs(arrayOne[arrOneIdx] - arrayTwo[arrTwoIdx]):
			smallest[0] = arrayOne[arrOneIdx]
			smallest[1] = arrayTwo[arrTwoIdx]
		if arrayOne[arrOneIdx] < arrayTwo[arrTwoIdx]:
			arrOneIdx += 1
		elif arrayOne[arrOneIdx] > arrayTwo[arrTwoIdx]:
			arrTwoIdx += 1
		else:
			break
	return smallest

#{
#  "arrayOne": [10, 1000],
#  "arrayTwo": [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530]
#}

# [1000, 1014]
