# Solution 1 - O(n2)
def smallestDifference(arrayOne, arrayTwo):  # O(n2)
    # Write your code here.
    smallest = [float('inf'), float('-inf')]
	z
    for one in arrayOne:
        for two in arrayTwo:
            if abs(smallest[0] - smallest[1]) > abs(one - two):
                smallest = [one, two]
    return smallest

