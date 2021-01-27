## O(2n) or O(3n) time because we may visit a number twice or third,
## but we can simplify to O(n) time | O(1) space 

def longestPeak(array):
	longestLength  = 0
	idx = 1
	while idx < len(array) -1 :
		isPeak = array[idx-1] < array[idx] and  array[idx] > array[idx+1] 
		if isPeak == False:
			idx+=1
			continue
		leftIdx = idx-2
		rightIdx = idx +2
		while leftIdx >= 0 and  array[leftIdx] < array[leftIdx+1]:
			leftIdx-= 1
		while  rightIdx < len(array) and array[rightIdx] < array[rightIdx-1] :
			rightIdx += 1
		currLenth = rightIdx - leftIdx -1
		longestLength = max(longestLength, currLenth)
		
		idx = rightIdx
	return longestLength 

# {"array": [1, 2, 3, 3, 4, 0, 10]}
# result = 3
# {"array": [1, 2, 3, 2, 1, 1]}
# result = 5