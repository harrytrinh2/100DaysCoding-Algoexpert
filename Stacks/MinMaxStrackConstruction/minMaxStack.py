# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.minMaxStack = []  # to hold min, max value at any given value in the stack
        self.stack = []  ## hold an empty list

    ## O(1) time | O(1) space
    ## peak is used to return the value of the end of the list or the array
    def peek(self):
        return self.stack[len(self.stack) - 1]
    ## grab the last element of an array

    ## ** if you use a linked list, you can just need to grap the tail of the linked list


    ## O(1) time | O(1) space
    ## pop a value of the stack
    def pop(self):
        self.minMaxStack.pop()

        return self.stack.pop()
        ## ** if we're dealing with the linked list, we just need to remove the tail of the link list

    ## O(1) time | O(N) space
    def push(self, number):
        '''
        First, we want to update the min and max of the minMaxStack
        '''
        newMinMax = {"min": number, "max": number}

        ## if minMaxStack is not empty
        if len(self.minMaxStack):
            lastMinMax = self.minMaxStack[len(self.minMaxStack) - 1]  # lastMinMax{"min":x, "max":y}

            newMinMax["min"] = min(lastMinMax["min"], number)
            newMinMax["max"] = max(lastMinMax["max"], number)

        self.minMaxStack.append(newMinMax)
        self.stack.append(number)

    ## O(1) time | O(N) space
    def getMin(self):
        # Write your code here.
        return self.minMaxStack[len(self.minMaxStack) - 1]["min"]

    ## O(1) time | O(N) space
    def getMax(self):
        # Write your code here.
        return self.minMaxStack[len(self.minMaxStack) - 1]["max"]



stack = MinMaxStack()
print("push 5 into the array")
stack.push(5)
print(stack.getMin())
print(stack.getMax())
print(stack.peek())

print("push 7 into the array")
stack.push(7)
print(stack.getMin())
print(stack.getMax())
print(stack.peek())


print("push 2 into the array")
stack.push(2)
print(stack.getMin())
print(stack.getMax())
print(stack.peek())

'''
Correct output:
push 5 into the array
5
5
5
push 7 into the array
5
7
7
push 2 into the array
2
7
2
'''