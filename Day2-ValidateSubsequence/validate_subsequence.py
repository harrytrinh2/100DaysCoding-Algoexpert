# Time: O(n) | Space: O(1)
def isValidSubsequence(array, sequence):
    # Write your code here.
	idx=0
	seq_length = len(sequence)
	for element in array:
		if element == sequence[idx]:
			idx+=1
		if idx == seq_length:
			return True
	return False

# Time: O(n) | Space: O(1)
def isValidSubsequence(array, sequence):
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            return True
        if sequence[seqIdx] == value:
            seqIdx += 1

    return seqIdx == len(sequence)

# Time: O(n) | Space: O(1)
def isValidSubsequence(array, sequence):
    seqIdx = 0
    arrIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)		

#{
#  "array": [5, 1, 22, 25, 6, -1, 8, 10],
#  "sequence": [5, 1, 22, 22, 25, 6, -1, 8, 10]
#}
# result: Flase
print(isValidSubsequence(array,sequence))
