## -------------------------------
## O(n^2) time | O(n) space
def arrayOfProducts(array):
    # Write your code here.
	result = []
    for i in range(len(array)):
		runningProduct = 1
		for j in range(len(array)):
			if j != i:
				runningProduct *= array[j]
		result.append(runningProduct)
	return result
## -------------------------------
## O(n) time | O(n) space
def arrayOfProducts(array):
	product = [1 for _ in range(len(array))]

	leftRunningProduct = 1
	for i in range(len(array)):
		product[i] = leftRunningProduct
		leftRunningProduct *= array[i]


	print(product)
	rightRunningProduct =1
	print(leftRunningProduct)
	for i in reversed(range(len(array))):
		product[i] *= rightRunningProduct
		rightRunningProduct *= array[i]

	print(leftRunningProduct)
	print(product)
	print(rightRunningProduct)
arrayOfProducts([5, 1, 4, 2])

##-------------------------------
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

