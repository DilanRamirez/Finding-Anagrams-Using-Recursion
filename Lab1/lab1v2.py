"""
CS 2302 - Data Structures
Instructor: Dr. Olac Fuentes
TA: Ismael Villanueva-Miranda
Laboratory 1 - Recursion
Author: Dilan Ramirez
Description: An anagram is a permutation of the letters of a word that produces another word. The task for this
lab consists of writing a program that asks a user to input a word and then prints all the anagrams of
that word.slee
Last Modification: Jun 17, 2019
"""

# keep track of the program's time
from datetime import datetime
start_time = datetime.now()

permList = []  # saves permutations from the "permutation" function
foundPermutations = []  # saves the permutations found in the English dictionary
perms2 = []
wordSet = []

f = open("words_alpha.txt", "r")
wordSet = [line.strip() for line in f]
set(wordSet)

# function that makes the permutations of the word
def permutations(word):
    if len(word) == 0:
        return [word]
    values = permutations(word[1:])
    first = word[0]
    final = []
    for i in values:
        for j in range(len(i) + 1):
            final.append(i[:j] + first + i[j:])
    permList.extend(final[:])
    return final

word = input("Enter a word or empty string to finish: ")
permutations(word)


# code that selects only the permutations equal to the word's length
# print("Word: ", word)
# for i in permList:
#     if len(i) == len(word):
#         perms2.append(i)
#         perms2.sort()

# code that finds the permutations in the English dictionary
for word in perms2:
    for wordAlpha in wordSet:
        if wordAlpha == word:
            foundPermutations.append(wordAlpha)

# function that prints the permutations found
count = 0
print("The word spot has the following anagrams:")
for i in foundPermutations:
    count = count + 1
    print(count, ".", i)

end_time = datetime.now() # finish time
print('Duration: {}'.format(end_time - start_time))
