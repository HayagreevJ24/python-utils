# Algorithm for Linear search on a 1D array

arr = ['Serendipity', 'Mellifluous', 'Ephemeral','Nebulous', 'Quixotic', 'Effervescent', 'Perseverance', 'Ephemeral', 'Labyrinthine', 'Resplendent', 'Vivacious', 'Pernicious', 'Ineffable', 'Scintillating', 'Surreptitious', 'Ebullient']

def linearSearch(searchParam):
    count = 0
    for i in arr:
        if searchParam == i:
            count += 1

    return count


searchParam = input("Enter a word to find in the array: ").capitalize()
print(f"The word {searchParam} was found {linearSearch(searchParam)} time(s) in the array.")

