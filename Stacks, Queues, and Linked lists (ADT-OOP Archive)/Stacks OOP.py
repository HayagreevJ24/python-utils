# Program to create a stack using object-oriented programming.

"""
Stack:

- First in, Last out (FILO)


initNumber = input from user
initType = input from user

stackArr  = [] will already come initialised by constructor
numElements = 0
lastPointer = -1


(a) push operation
- increment array index
- put the element in len(stackArr) - 1 - lastPointer th index
- increment element number

validation rules:

1. numElements = size of array, we return an overflow error/
lastPointer = initNumber - 1
2. check if the item that is pushed has the same datatype as the inittype

(b) pop [remove the topmost element from the array]
- set the element in len(StackArr) - 1 - lastPointer th index to initialising variable
- decrement lastPointer
- increment element number

validation rules:
1. numElements = 0, return underflow/
lastPointer = -1


(c) search [linear search for an element in the stack]
- init an index and set it to 0
- traverse through the length of array and check if it is present.

(d) isEmpty [check if the stack has any elements at all]
- check if the number of elements is 0

(e) isFull [check if the stack is completely full]
- check if the number of elements is initNumber
"""

class Stack:
    # Constructor function for instance variables
    def __init__(self, initNumber, initType):
        self.numberOfElements = 0
        self.topPointer = -1
        if initType == "str":
            self.initVariable = ""
        elif initType == "int":
            self.initVariable = 0
        elif initType == "float":
            self.initVariable = 0.0
        else:
            raise TypeError("Incorrect datatype for stack declaration. Datatype can only be \"str\", \"int\", or \"float\".")

        self.stackArr = [self.initVariable] * initNumber

    def isEmpty(self):
        if self.numberOfElements == 0:
            return True
        else:
            return False

    def isFull(self):
        if self.numberOfElements == len(self.stackArr):
            return True
        else:
            return False

    def push(self, elementToPush):
        if self.isFull():
            raise OverflowError("Stack is full. Cannot push more elements.")
        else:
            if not isinstance(elementToPush, type(self.initVariable)):
                raise TypeError("Datatype of element to push does not match stack declaration.")
            else:
                self.topPointer += 1
                self.stackArr[len(self.stackArr) - 1 - self.topPointer] = elementToPush
                self.numberOfElements += 1
                return True  # Indication that push operation was succesful.

    def pop(self):
        if self.isEmpty():
            raise OverflowError("Stack is empty. No elements to pop.")
        else:
            itemtoReturn = self.stackArr[len(self.stackArr) - 1 - self.topPointer]
            self.stackArr[len(self.stackArr) - 1 - self.topPointer] = self.initVariable
            self.topPointer -= 1
            self.numberOfElements -= 1
            return itemtoReturn

    def elementSearch(self, elementToSearch):
        index = 0
        for data in self.stackArr:
            if data == elementToSearch:
                return True
        return False
# End of class definition


def main():
    """
    Demonstrative code here
    """


customStack = Stack(4, "int")
print(customStack.stackArr)
for i in range(len(customStack.stackArr)):
    customStack.push(9)
    print(customStack.stackArr)
a = customStack.pop(); print(a)
b = customStack.pop(); print(b)
c = customStack.pop(); print(c)
d = customStack.pop(); print(d)
# Uncomment below code to demonstrate error
# customStack.push(True) # Will raise typeError due to pushing element not having same type as stack declaration.
# e = customStack.pop(); print(e)  # Will raise overflowerror (underflowerror) due to stack being empty.
# customStack.push("custom string") # Will raise typeError due to validation in push method.

print(customStack.isEmpty())
print(customStack.isFull())
print(customStack.elementSearch(10))
print(customStack.elementSearch(9))
print(customStack.elementSearch(0))  # Will evaluate to True since on popping all elements the stack is reset to initType ground state.

# End of main function


main()

