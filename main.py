#import os
voyelles = ['a', 'e', 'i', 'o', 'u', 'y']

def toutes_voyelles(mot):
    return 'a' in mot and 'e' in mot and 'i' in mot and 'o' in mot and 'u' in mot

def plusieurs_fois_lettre(lettre, mot):
    mot2 = mot
    if lettre not in mot2:
        return False
    a = mot2.find(lettre)
    mot2 = mot2[:a] + mot2[a+1:]
    return lettre in mot2

def une_seule_fois(lettre, mot):
    mot2 = mot
    if lettre not in mot2:
        return False
    a = mot2.find(lettre)
    mot2 = mot2[:a] + mot2[a+1:]
    return lettre not in mot2

def une_seule_fois_chaque_voyelle(mot):
    b=True
    for v in voyelles:
        b = b and une_seule_fois(v, mot)
    return b


Dico = open('French.txt', 'r', encoding='utf-8')
scooby = []
for mot in Dico:
    mot = mot[:-1] # enlève le \n
    if une_seule_fois_chaque_voyelle(mot):
        scooby.append(mot)
print(scooby)
print(len(scooby))