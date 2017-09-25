# (Implement Stack using inheritance) In Listing 12.13, the Stack class is
# implemented using composition. Define a new Stack class using inheritance
# that extends list.
# Draw UML diagrams of the new class. Implement it. Write a test program that
# prompts the user to enter five strings and displays them in reverse order.
class Stack(list):
    def __init__(self):
        super().__init__(self)

    def push(self, element):
        self.append(element)

    def peek(self):
        return self[len(self) - 1]

    def isEmpty(self):
        return len(self) == 0

def test():

    stack1 = Stack()
    for i in range(5):
        strng = input("Enter string " + str(i + 1) + " : ")
        stack1.push(strng)

    while not stack1.isEmpty():
        print(stack1.pop())

test()
