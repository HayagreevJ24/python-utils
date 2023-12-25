#   STATISTICS CALCULATOR PROGRAM - UTILITY PROGRAMS
import math


def dataentry(rawdata):
    #   Getting number of data items
    while True:
        try:
            numitems = int(input("Enter the number of values in your data set: "))
        except ValueError:
            print("Invalid input. Please try again.")
        else:
            break

    #   Getting the data items
    for i in range(numitems):
        while True:
            try:
                rawdata.append(float(input(f'Enter data number {i + 1}: ')))
            except ValueError:
                print("Invalid input. Please make sure your inputs are numbers.")
            else:
                break
    return rawdata


def sorting(rawdata):
    #   Arranges the list in ascending order
    sorteddata = []
    while rawdata:
        minimum = rawdata[0]  # Assigns maximum of list to be first element every iteration to find max of list.
        for i in range(len(rawdata)):  # Algorithm to find maximum of list for that iteration and update both lists.
            if rawdata[i] < minimum:
                minimum = rawdata[i]
        rawdata.remove(minimum)
        sorteddata.append(minimum)
    return sorteddata


def calculate(sorteddata):
    calculateditems = []

    #   Calculating mean (FIRST ELEMENT IN LIST OF calculateditems)
    datasum = 0
    sortedlen = len(sorteddata)
    for i in range(len(sorteddata)):
        datasum += sorteddata[i]
    calculateditems.append(round(datasum / sortedlen, 3))  # Rounded to 3 decimal places.

    # Calculating median (SECOND ELEMENT IN LIST OF calculateditems)
    if sortedlen % 2 == 0:
        calculateditems.append(
            (sorteddata[(math.floor((sortedlen + 1) / 2)) - 1] + sorteddata[(math.ceil((sortedlen + 1) / 2)) - 1]) / 2)
    else:
        calculateditems.append(sorteddata[int((sortedlen + 1) / 2) - 1])

    return calculateditems
    #   Calculating mode



def master():
    print('\nSTATISTICS CALCULATOR\nThis program calculates basic statistical values for a set of numerical data.\n')
    emptydata = []
    rawdata = dataentry(emptydata)
    sorteddata = sorting(rawdata)
    calculateditems = calculate(sorteddata)
    print(f'\nCalculated statistics:\nBasic statistics:\n'
          f'1. Arithmetic mean: {calculateditems[0]}\n'
          f'2. Median: {calculateditems[1]}\n'
          f'3. Mode: {calculateditems[2]}\n')


master()
