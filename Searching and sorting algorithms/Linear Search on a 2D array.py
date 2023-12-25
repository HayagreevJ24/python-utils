# Linear search on a 2D Array with multiple fields. [Search by field.]

records = [
    [215, 'Sophia', 'Anderson', 'Los Angeles', 'California'],
    [176, 'Daniel', 'Garcia', 'Phoenix', 'Arizona'],
    [398, 'Emily', 'Smith', 'Chicago', 'Illinois'],
    [524, 'Michael', 'Johnson', 'Miami', 'Florida'],
    [621, 'Jessica', 'Wilson', 'Denver', 'Colorado'],
    [853, 'William', 'Brown', 'Houston', 'Texas'],
    [437, 'Olivia', 'Martinez', 'San Francisco', 'California'],
    [309, 'David', 'Davis', 'Seattle', 'Washington'],
    [682, 'Matthew', 'Lopez', 'Austin', 'Texas'],
    [165, 'Sarah', 'Rodriguez', 'Portland', 'Oregon'],
    [789, 'Ella', 'Hernandez', 'San Diego', 'California'],
    [432, 'Liam', 'Gonzalez', 'Tucson', 'Arizona'],
    [598, 'Ava', 'Taylor', 'Dallas', 'Texas'],
    [723, 'Noah', 'White', 'Orlando', 'Florida'],
    [186, 'Mia', 'Johnson', 'Denver', 'Colorado'],
    [351, 'Oliver', 'Brown', 'San Antonio', 'Texas'],
    [962, 'Sophia', 'Smith', 'Las Vegas', 'Nevada'],
    [541, 'Ethan', 'Wilson', 'San Jose', 'California'],
    [874, 'Isabella', 'Martinez', 'Boston', 'Massachusetts']]

recordStrcutre = ["idNumber", "First Name", "Last Name", "City", "State"]

def linearSearch(searchparam, columnNumber):
    print("\nResults of search query: ")
    count = 0
    for i in records:
        if i[columnNumber] == searchparam:
            count += 1
            print(f"Result {count}: {i}")
        else:
            continue

    if count == 0:
        print("Sorry. No records found matching query.")

def main():
    while True:
        for i in range(len(recordStrcutre)):
            print(f"Press {i} to search by {recordStrcutre[i]}")

        choice = int(input("Your choice: "))

        if 0 <= choice <= 4:
            searchField = recordStrcutre[choice]
            break
        else:
            print("\nPlease enter a valid choice.")
            continue

    seachParam = input(f"Enter the {searchField} you want to look for: ")

    linearSearch(seachParam, choice)

main()