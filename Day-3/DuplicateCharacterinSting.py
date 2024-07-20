def printDuplicateCharacters(s):
    char_count = {}

    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    duplicates = [char for char , count in char_count.items() if count > 1]

    if duplicates:
        print("Duplicate characters",",".join(duplicates))
    else:
        print("No duplicates characters found")

s= "programming"
printDuplicateCharacters(s)