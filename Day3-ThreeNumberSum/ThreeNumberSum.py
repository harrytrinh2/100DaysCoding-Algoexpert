# O(n^3) time | O(n) space

def threeNumberSum(array, targetSum):
	array.sort()
    # Write your code here.
	output = []
	for i in range(0,len(array)-2):
		for j in range(i+1,len(array)-1):
			for k in range(j+1,len(array)):
				if ((array[i] + array[j] + array[k]) == targetSum)  :
					output.append([array[i], array[j], array[k]])
	return output

# O(n^2) time | O(n) space

def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()  # nlogn
    print(array)
    results = []
    for current in range(len(array)):
        left = current + 1
        right = len(array) - 1
        while left < right:
            print( array[current], array[left], array[right])
            result = array[current] + array[left] + array[right]
            if result == targetSum:
                results.append([array[current], array[left], array[right]])
                left += 1
                right -= 1
            elif result < targetSum:
                left += 1
            else:
                right -= 1
    return results
print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6],0 ))

#[[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
