import os

def mystere(mot1, mot2):
    """
    Vérifie si les lettres de mot2 sont contenues dans mot1
    Elles doivent être dans le bon ordre mais d'autres lettres peuvent
    être insérées.
    """
    compt = 0
    for lettre in mot1:
        if lettre == mot2[compt]:
            compt+=1
            if compt==len(mot2):
                return True
    return compt==len(mot2)

dico = open("French.txt", 'r', encoding="UTF-8")
c=0
for mot in dico:
    mot.lower()
    if mystere(mot, "solene"):
        print(mot)
        c+=1
print("Fini")
print(c)
dico.close()
