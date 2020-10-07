def isMonotonic(array):
    # Write your code here.
	increase,decrease = 1,1
	for index, i in enumerate(array):
		if index == 0:
			continue
		if index == 1:
			if i >= array[index-1]:
				increase+=1
			elif i <= array[index-1]:
				decrease+=1
		if increase>=2:
			if i >= array[index-1]:
				increase+=1
		if decrease>=2:
			if i <= array[index-1]:
				decrease+=1
	if increase == (len(array) +1) or decrease == (len(array) +1):
		return True
	else:
		return False

print(isMonotonic([-1, -1, -2, -3, -4, -5, -5, -5, -6, -7, -8, -8, -9, -10, -11]))