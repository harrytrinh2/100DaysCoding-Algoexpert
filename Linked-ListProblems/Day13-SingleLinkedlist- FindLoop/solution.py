# O(N) time | O(1) space
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def findLoop(head):
    # Write your code here.
	first = head.next
	second = head.next.next
	while first != second:
		first = first.next
		second = second.next.next
	first = head
	while first != second:
		first = first.next
		second = second.next
	return first