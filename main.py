#import os
Dico = open('French.txt', 'r', encoding='utf-8')
scooby = []
for mot in Dico:
    if 'a' in mot and 'e' in mot and 'i' in mot and 'o' in mot and 'u' in mot:
        scooby.append(mot)
print(len(scooby))