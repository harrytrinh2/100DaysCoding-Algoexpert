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
print(arrayOfProducts([5, 1, 4, 2]))