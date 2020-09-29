# # O(n^2) time | O(1) space
-----------------------Solution 1 -----------------------------------------
def twoNumberSum(array, targetSum):
    # Write your code here.
	for i in range(0,len(array)):
		for j in range(1,len(array)):
			if (array[i] + array[j] == targetSum ) and (i != j):
				return [array[i] , array[j] ]
	return []


# # O(n^2) time | O(1) space
---------------------------Solution 2-------------------------------------
def twoNumberSum(array, targetSum):
    # Write your code here.
	for i in range(0,len(array)-1):
		for j in range(i+1,len(array)):
			if (array[i] + array[j] == targetSum ) and (i != j):
				return [array[i] , array[j] ]
	return []



# # O(n) time | O(n) space
---------------------------Solution 3-------------------------------------
def twoNumberSum(array, targetSum):
    # Write your code here.
	for i in range(0,len(array)):
		firstNumber = array[i]
		secondNumber = targetSum - firstNumber
		if secondNumber in array[i+1:]:
			return sorted([firstNumber, secondNumber])
	return []


# # O(nlogn) time | O(1) space
---------------------------Solution 4-------------------------------------
def twoNumberSum(array, targetSum):
    # Write your code here.
	array.sort()
	left  = 0 
	right = len(array) -1
	while left < right:
		currentSum = array[left] + array[right]
		if currentSum == targetSum:
			return [array[left] , array[right]]
		elif currentSum < targetSum:
			left+=1
		elif currentSum > targetSum:
			right-=1
	return []