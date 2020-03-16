# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 14:09:46 2019

@author: Dilan Ramirez
"""

from datetime import datetime
start_time = datetime.now()

permList = []
perms = []
new2 = []

f = open("words_alpha.txt", "r")
wordSet = [line.strip() for line in f]


def permutations(word):
    if len(word) == 1:
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

# print("Word: ",word)
# for i in permList:
#     if len(i) == len(word):
#         new2.append(i)
#         new2.sort()
# print(new2)

for word in new2:
    for wordAlpha in wordSet:
        if wordAlpha == word:
            perms.append(wordAlpha)

print("The word spot has the following anagrams:")
for i in perms:
    print(i)

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

