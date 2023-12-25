# Object-oriented implementation of Linked lists.

"""
Single Linked Lists - Implementation Docstring.

Object attributes (Instance variables):
    1. Skeleton
    (a) 2D array holding the data items and the pointers.
    (b)

    2. Pointers
    (a) Free pointers - Indicates the next free memory space.
    (b) Start Pointer for each file. [Created on the go]
        - The FIRST Start pointer is initialised to 0.
        - The SUBSEQUENT start pointers are initialised to the free pointer.



Methods:
    1. def add
       :param - The element to be added into the linked list
       :returns - True if the operation was a success. False otherwise.

    # CONTINUE FROM HERE.
    





"""

class LinkedList:
    def __init__(self, listSize, listType):

        # Declaring the Instance variables

        match listType:
            case "int": self.InitElement = 0
            case "str": self.InitElement = ""
            case "float": self.InitElement = 0.0
            case _: raise TypeError("Linked list can only be of type \"str\", \"int\", or \"float\".")

        self.InitSize = listSize
        self.LinkedListData = [self.InitElement] * self.InitSize
        self.LinkedListPointers = [(i + 1) for i in range(self.InitSize - 1)]
        self.LinkedListPointers.append(None)  # The last pointer should be set to null.
        self.FreePointer = 0
        self.StartPointer = 0


