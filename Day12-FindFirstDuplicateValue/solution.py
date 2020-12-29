# O(n) time | O(n) space
# using Dictionary to store
def firstDuplicateValue(array):
    # Write your code here.
  eleDict = {}
    for i in array:
    if i not in eleDict:
      eleDict[i] = 1
    else:
      return i
  return -1

# O(n) time | O(n) space
# using Set to store
def firstDuplicateValue(array):
    # Write your code here.
  seen = set()
    for i in array:
    if i not in seen:
      seen.add(i)
    else:
      return i
  return -1

# O(N) time | O(1) space
def firstDuplicateValue(array):
    # Write your code here.
  for value in array:
    if array[abs(value)-1] < 0:
      return abs(value)
    array[abs(value) -1] *= -1 
    return -1

print(firstDuplicateValue([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]))
print(firstDuplicateValue([2, 1, 1]))