import os
alphabet = "abcdefghijklmnopqrstuvwxyz"

def my_count(lettre, mot):
    c=0
    for l in mot:
        if l==lettre:
            c+=1
    return c

fichier = open("French.txt", 'r', encoding="utf-8")
scooby, record = ' ', 0

for mot in fichier:
    for lettre in alphabet:
        compt = my_count(lettre, mot)
        if compt > record:
            scooby = mot
            record = compt

print("Record :", record, scooby)