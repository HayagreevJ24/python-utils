
def bubblesort(array, colnumber):
    for i in range(len(array ) -1): # 0 - 1 - 2 - 3 - 4
        for j in range(0 ,len(array) - ( i +1)):
            if int(array[j][colnumber - 1]) > int(array[ j +1][colnumber - 1]):
                array[j + 1], array[j] = array[j], array[j + 1]

    return array



def first_three(array):
    for i in range(3):
        print(f"placement { i +1} - {array[i]}, \n")



def main():
    array = [["12", "y", "123"],
             ["13", "n", "213"],
             ["14", "n", "657"],
             ["15", "n", "564"],
             ["16", "n", "543"]]

    fidelcastro = ["age", "Winning status" ,"time"]
    print("Options for sorting: ")
    while True:
        for i in range(3):
            print(f"\nOption {i + 1} - {fidelcastro[i]}")
        try:
            columnnumber = int(input("Enter your choice: "))
        except ValueError:
            print("Waste fellow enter proper number.")
        else:
            if 1 <= columnnumber <= 3:
                print("Choice accepted.")
                break
            else:
                print("You are stupid.")
                continue

    array = bubblesort(array, columnnumber)

    for k in range(len(array)):
        print(array[k], end="\n")

    if columnnumber == 2:
        print(f"\nPlacements according to time: ")
        print(first_three(array))


if __name__ == '__main__':
    main()
