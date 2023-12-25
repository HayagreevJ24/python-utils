#   Calculating Sin X up till a particular accuracy using Taylor's series.
import math  # Required for Factorial and pi.

print('\nThis program calculates sin of a angle in degrees with taylor\'s series.')

#   Getting user input for the value of maximum number up till which taylor's series will go.
maxlim = 0
while True:
    try:
        maxlim = int(input("\nAccuracy of answer (maximum value used for power and factorial in taylor series): "))
    except ValueError:
        print("Invalid input.")
        continue
    else:
        if maxlim % 2 == 0 or maxlim < 1:
            print("Make sure the end number is odd and is positive.")
            continue
        else:
            break

#   Input in degrees
radians = 0
while True:
    try:
        degrees = float(input("Enter the value of the angle in degrees: "))
    except ValueError:
        print("Invalid input.")
        continue
    else:
        radians = degrees * (math.pi / 180)
        break

#   Appending all the terms in a list.
termlist = []

for i in range(1, maxlim, 2):
    try:
        termlist.append((radians ** i) / (math.factorial(i)))
    except OverflowError:
        print("\nSorry. It looks like the accuracy entered is too large. please try again.") # Transfer this to input loop.
        exit()

#   Alternating operations using list index.
sin = 0

for k in range(0, len(termlist)):
    if k % 2 == 0:
        sin += termlist[k]
    else:
        sin -= termlist[k]


#   Printing the output
print(f'Accurate sin of angle: {sin}')
#   END.
#   WORK IN PROGRESS....