# OOP Python Program to implement Normal queues.

"""
Normal queues - Implementation docstring

Object Constructor:

- First In, First out [FIFO]


(a) Parameters - InitSize, InitType

(b) Declare instance variables
     - InitElement - An Initialising element taken from parameter
     - InitSize - An Initialising element taken from parameter.
       [If initType is of some valid datatype - Validation]
       [Later use in methods]
     - Queue array - Declare of size InitNumber with InitElements.
     - Front pointer
     - Rear Pointer
     - Number of elements


Object methods:

1. isEmpty():
    Parameters: None.
    Returns: True/False
    Algorithm: Checks if the number of elements is zero or not.
    Validation: None

2. isFull():
    Parameters: None.
    Returns: True/False
    Algorithm: Checks if the number of elements equals InitSize
    Validation: None

3. queuesearch():
    Parameters: What needs to be searched for in the queue. [searchElement]
    Returns: True/False
    Algorithm: Linear search: Iterate through the queue, check for desired element.
    Validation: None


4. enqueue():
    Parameters: What needs to be put in the queue. [enqueueElement]
    Return: True if the operation was a success.
    Algorithm:
        - Increment rearPointer first, then add element in that array index.
        - Increment number of elements.
    Validation:
        - Check if enqueueElement is same datatype as InitElement, otherwise rEX.
        - Check for overflow error using previous methods, rEX as app.
        - Check if the elements have been filled in till the end. rEX as app.

5. dequeue():
    Parameters: None.
    Return: The element that has been dequeued. [Declare local var for same.]
    Algorithm:
      - Remove what is in the frontPointerth index, store in local var.
      - Decrement number of elements.
      - Check if number of elements is 0, then set pointers to -1.
      - Otherwise: Increment frontPointer

    Validation:
       - Check for underflow error using previous methods, rEX as app.


"""

class UnderflowError(Exception):
    """Custom exception for dequeueing validation."""
    pass

class EnqueuelimitError(Exception):
    """ Custom exception for enqueueing validation - when rearpointer points to last element in the array in a normal queue more enqueue ops not possible."""
    pass

class Queue:
    # Constructor for queues
    def __init__(self, InitSize, InitType):
        self.InitSize = InitSize
        if InitType == "str":
            self.InitElement = ""
        elif InitType == "int":
            self.InitElement = 0
        elif InitType == "float":
            self.InitElement = 0.0
        else:
            raise TypeError("Invalid Datatype for queue declaration. Datatype can only be \"str\", \"int\", \"float\".")

        self.queueArr = [self.InitElement] * self.InitSize
        self.frontPointer = -1
        self.rearPointer = -1
        self.numberOfElements = 0

    # Methods for queues

    def isEmpty(self):
        if self.numberOfElements == 0:
            return True
        else:
            return False

    def isFull(self):
        if self.numberOfElements == self.InitSize:
            return True
        else:
            return False

    def queueSearch(self, searchElement):
        for queueElement in self.queueArr:
            if queueElement == searchElement:
                return True
        return False

    def enqueue(self, enqueueElement):
        # Validation of datatype and overFlowError
        if not isinstance(enqueueElement, type(self.InitElement)):
            raise TypeError(f"Element to enqueue does not correspond with datatype of queue.\nQueue has datatype {type(self.InitElement)}, attempted to enqueue element of type {type(enqueueElement)}.")
        elif self.isFull():
            raise OverflowError("Queue is full. Cannot enqueue more elements.")
        elif self.rearPointer == self.InitSize - 1:  # Indicates that queue has been filled to the end.
            raise EnqueuelimitError("Elements have been enqueued till the end. Cannot enqueue more elements.")
        else:
            self.rearPointer += 1
            self.queueArr[self.rearPointer] = enqueueElement
            self.numberOfElements += 1

            if self.numberOfElements == 1:
                self.frontPointer = 0
                # Required code because initially frontPointer is -1 and it needs to become 0 once first element has been queued in.

    def dequeue(self):
        # Validation of underflowError
        if self.isEmpty():
            raise UnderflowError("Queue is empty. Cannot dequeue more elements.")
        else:
            dequeuedElement = self.queueArr[self.frontPointer]
            self.queueArr[self.frontPointer] = self.InitElement
            self.numberOfElements -= 1
            if self.isEmpty():
                self.frontPointer, self.rearPointer = -1, -1
            else:
                self.frontPointer += 1

        return dequeuedElement


def main():
    # Standard Demonstrative code here
    # Uncomment code to demonstrate errors.
    myNormalQueue = Queue(10, "int")
    print(f"Is the queue empty: {myNormalQueue.isEmpty()}")
    print(f"Is the queue full: {myNormalQueue.isFull()}")
    # myErroneousQueue = Queue(10, "complex") # Queue does not support complex datatype hence this will generate TypeError.
    print(myNormalQueue.queueArr)

    for i in range(1, 11):
        myNormalQueue.enqueue(i)
        print(myNormalQueue.queueArr)

    print(f"Is the queue empty: {myNormalQueue.isEmpty()}")
    print(f"Is the queue full: {myNormalQueue.isFull()}")

    # myNormalQueue.enqueue(19)  # Will cause an overflowerror.
    # myNormalQueue.enqueue(6 + 7j) # Will cause TypeError as we have tried to enqueue a complex element into an integer queue.
    print("\n")
    for i in range(10):
        print(myNormalQueue.queueArr)
        # myNormalQueue.enqueue(10)  # Will cause enqueueElementError since queue is filled till the end, and you cannot fill more elements.
        a = myNormalQueue.dequeue(); print(a)

    # myNormalQueue.dequeue()  # Will cuase an UnderflowError.

    print(f"Does the queue contain element 100? {myNormalQueue.queueSearch(100)}")
    print(f"Does the queue contain element 0? {myNormalQueue.queueSearch(0)}")
    print(f"Does the queue contain a null value? {myNormalQueue.queueSearch(None)}")


main()


def main2():
    # Enter custom demonstrative code here - and comment main()
    pass


main2()