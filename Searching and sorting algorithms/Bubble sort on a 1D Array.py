# Sorting algorithms: Bubble sort on a 1D Array.
# Optimisation 1 - Look upto (n - 1)th element where n is the number of passes.
# Optimisation 2 - Maintain a flag to check if the array is already sorted.
import random
import time
import matplotlib.pyplot as plot


def bubbleSort(x):
    n = len(x)
    start = time.time()
    for i in range(n):
        swap = False
        for j in range(n - 1 - i):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
                swap = True
        if not swap:
            # Array has already been sorted, stop.
            end = time.time()
            return [x, (end - start)]  # Returns a list containing the sorted array and execute time

    end = time.time()  # Returns the sorted array after all passes.
    return [x, (end - start)]


def main():
    # Goal: to create random lists of increasing lengths to demonstrate time complexity of bubble sort.
    dataPoints = int(input("Enter the number of data points: "))
    a = int(input("Enter lower limit of random lists: "))
    b = int(input("Enter upper limit of random lists: "))
    lengthArray = []
    execTimeArray = []
    worstCase = []
    bestCase = []

    print("....In Progress")

    for listLengths in range(1, dataPoints + 1):
        randomList = []
        for element in range(listLengths):
            randomList.append(random.randint(a, b))

        results = bubbleSort(randomList)  # A list with the sorted array and the time.

        execTimeArray.append((results[1]) * (10 ** 9))  # Converted to nanoseconds
        lengthArray.append(listLengths)
        worstCase.append((listLengths**2) * (10 ** 2)) # To compare with anticipated worst case time complexity of O(n^2)
        bestCase.append(listLengths * (10 ** 2))  # To compare with anticipated best case time complexity of O(n^2)

    print("Done! Click on the GUI and use Alt + f4 to terminate it.")
    plot.rcParams["figure.figsize"] = [7.5, 4.5]
    plot.rcParams["figure.autolayout"] = True
    plot.autoscale()
    plot.xlabel("Number of elements in the array (arrLen)")
    plot.ylabel("Sorting time of the array/nanoseconds")
    plot.title("Time complexity of bubble sort visualisation")
    plot.plot(lengthArray, execTimeArray, label="Actual run Time")
    plot.plot(lengthArray, bestCase, label="Best case, O(n)")
    plot.plot(lengthArray, worstCase, label="Worst case, O(n\u00b2)")
    plot.legend(bbox_to_anchor=(1.05, 1.0), loc='upper right')
    plot.show()


main()
