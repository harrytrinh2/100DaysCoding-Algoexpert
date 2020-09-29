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
				

array = [5,1,22,25,6,-1,8,10]
sequence = [1,6,-1,10]

# array = [1,1,1,1,1]
# sequence = [1,1,1]

print(isValidSubsequence(array,sequence))
