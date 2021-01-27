## O(n) time | O(n) space
def arrayOfProducts(array):
    # Write your code here.
	result = []
	for idx in range(0,len(array),1):
		runningProduct = 1
		leftidx = idx-1
		rightidx = idx +1
		while leftidx >= 0:
			runningProduct *= array[leftidx]
			leftidx -= 1
		while rightidx <= (len(array) -1) :
			runningProduct *= array[rightidx]
			rightidx += 1
		result.append(runningProduct)
	return result
		
# {"array": [5, 1, 4, 2]}
# [8, 40, 10, 20]
	