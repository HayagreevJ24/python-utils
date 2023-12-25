#   Positive decimal integers to hexadecimal and binary converter.

#   Required arrays and a brief about what the program does.
print("\nThis calculator converts denary numbers to hexadecimal, binary, and octal.")
raw_hex, raw_binary, raw_oct, final_hex, final_binary, final_oct = ([] for a in range(6))

#   Input for denary number.
while True:
    try:
        decimal = int(input("Enter a positive integer in denary system: "))
    except ValueError:
        print("Invalid input. ")
        continue
    else:
        if decimal <= 0:
            print("Please enter a positive integer.")
            continue
        else:
            decimal1 = decimal  # Variable to use in binary
            decimal2 = decimal  # Variable to use in octal
            break

#   Appending the values in the respective number system in reverse order (by default) to the raw lists.
while decimal > 0:
    raw_hex.append(decimal % 16)
    decimal = decimal // 16

while decimal1 > 0:
    raw_binary.append(decimal1 % 2)
    decimal1 = decimal1 // 2

while decimal2 > 0:
    raw_oct.append(decimal2 % 8)
    decimal2 = decimal2 // 8

#   Using raw values and a for loop with decrementing index iterations to append the values into the final lists.
for i in range(len(raw_hex) - 1, -1, -1):
    if raw_hex[i] < 10:
        final_hex.append(raw_hex[i])
    if raw_hex[i] == 10:
        final_hex.append("A")
    if raw_hex[i] == 11:
        final_hex.append("B")
    if raw_hex[i] == 12:
        final_hex.append("C")
    if raw_hex[i] == 13:
        final_hex.append("D")
    if raw_hex[i] == 14:
        final_hex.append("E")
    if raw_hex[i] == 15:
        final_hex.append("F")

for k in range(len(raw_binary) - 1, -1, -1):
    final_binary.append(raw_binary[k])

for m in range(len(raw_oct) - 1, -1, -1):
    final_oct.append(raw_oct[m])

#   Printing the output in the form of a continuous string rather than list with for loop.
print("\n")

print("Hexadecimal: ", end="")
for j in range(len(final_hex)):
    print(final_hex[j], end="")
print("\u2081", end="")
print("\u2086", end="")

print("\n")

print("Binary: ", end="")
for l in range(len(final_binary)):
    print(final_binary[l], end="")
print("\u2082", end="")

print("\n")

print("Octal: ", end="")
for n in range(len(final_oct)):
    print(final_oct[n], end="")
print("\u2088")



#   END.
#   Can do list.reverse() to reverse list and reduce amount of code.