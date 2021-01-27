def balancedBrackets(string):
    # if the length of the string is odd, then returns Flase
    openingBrackets = "{(["
    closingBrackets = "})]"
    matchingBrackets = {"}": "{", ")": "(", "]": "["}
    balanced_stack = []
    for char in string:
        if char in openingBrackets:
            balanced_stack.append(char)
        elif char in closingBrackets:
            if len(balanced_stack) == 0:
                return False

            if balanced_stack[-1] == matchingBrackets[char]:
                balanced_stack.pop()
            else:
                return False
        else:
            continue
    return len(balanced_stack) == 0

print(balancedBrackets("([])(){}(())()()"))
## True

print(balancedBrackets("{}gawgw()"))
## True


print(balancedBrackets("()[]{}{"))
## False

print(balancedBrackets(")[]}"))
## False

