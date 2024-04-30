class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
 
 
class Stack:
 
    # Initializing a stack.
    # Use a dummy node, which is
    # easier for handling edge cases.
    def __init__(self):
        self.head = Node("head")
        self.size = 0
 
    # Check if the stack is empty
    def isEmpty(self):
        return self.size == 0
 
    # Push a value into the stack.
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
 
    # Remove a value from the stack and return.
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value




class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """


        stack = Stack()

        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.push(i)
            else:
                if stack.isEmpty():
                    return False
                elif (i == ")" and stack.pop() != "(") or (i == "}" and stack.pop() != "{") or (i == "]" and stack.pop() != "["):
                    return False
        return stack.isEmpty()


