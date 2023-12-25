# Bogosort algorithm on a 1D array with demonstration of time complexity
import random
import time
import math
import matplotlib.pyplot as plot
from matplotlib.ticker import ScalarFormatter


def sortedCheck(listToScan):
    if len(listToScan) == 1:
        return True
    for i in range(len(listToScan) - 1):
        if listToScan[i] > listToScan[i + 1]:
            return False
    return True


def bogoSort(arrToSort):
    start = time.time()
    while not(sortedCheck(arrToSort)):
        random.shuffle(arrToSort)
    end = time.time()
    return [arrToSort, (end - start)]  # Returns the sorted list and execute time in a list.


def getRandomList(lower, upper, length):
    randomList = []
    for i in range(length):
        randomList.append(random.randint(lower, upper))
    return randomList


def main():
    arrLenLimit = int(input("Enter the maximum length of the list you want to sort: "))
    low = int(input("Enter the lower bound of random integer generation: "))
    high = int(input("Enter the upper bound of random integer generation: "))

    # Lists for plotting array length vs time.
    listOfLengths = []
    actualTimes = []
    worstCase = []  # Factorial
    bestCase = []   # Linear
    sqauredCase = []  # Intermediate
    exponent = -14

    print("In progress...")
    for i in range(1, arrLenLimit + 1):
        listOfLengths.append(i)
        worstCase.append(math.factorial(i) * (10 ** exponent))  # add scientific notation for scaling for all beflow
        bestCase.append(i * (10 ** exponent))
        sqauredCase.append(i ** 2 * (10 ** exponent))
        # Sorts the array and retrieves execute time.
        randomList = getRandomList(low, high, i)
        actualTimes.append(bogoSort(randomList)[1] * (10 ** -9))  # The function returns a list with execute time in second position. - Converted to nanoseconds

    # Plotting the results
    print("Use Alt + f4 to terminate window.")
    plot.rcParams["figure.figsize"] = [7.5, 4.5 ]
    plot.rcParams["figure.autolayout"] = True
    plot.title("Time complexity of bogosort visualisation")
    plot.xlabel("Number of elements in the array (arrLen)")
    plot.ylabel("Sorting time of the array/nanoseconds")
    # Plot length vs execute time
    plot.plot(listOfLengths, actualTimes, label="Actual run time")
    plot.plot(listOfLengths, bestCase, label="Best case - O(n)")
    plot.plot(listOfLengths, sqauredCase, label="Intermediate - O(n\u00b2)")
    plot.plot(listOfLengths, worstCase, label="Worst case - O(n!)")
    plot.legend(bbox_to_anchor=(1.05, 1.0), loc='upper right')
    plot.gca().yaxis.set_major_formatter(ScalarFormatter(useMathText=False))
    plot.show()



main()