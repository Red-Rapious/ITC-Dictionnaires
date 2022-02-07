import time

Dico = open("French.txt", 'r', encoding="UTF-8")
dictionnaire = []

for mot in Dico:
    mot = mot[:-1].lower()
    dictionnaire.append(mot)

def levenshtein(mot1, mot2):
    l1, l2 = len(mot1), len(mot2)
    d = [[0 for j in range(l2+1)] for i in range(l1+1)]
    for i in range(l1+1):
        d[i][0]=i
    for j in range(l2+1):
        d[0][j]=j
    for i in range(1, l1+1):
        for j in range(1, l2+1):
            cout = int(not mot1[i-1] == mot2[j-1])
            d[i][j] = min(d[i-1][j]+1, d[i][j-1]+1, d[i-1][j-1]+cout)
    return (d[l1][l2])

def plus_courte_distance(mot_input):
    t1 = time.time()
    if mot_input in dictionnaire:
        return [True, 0, [mot_input], time.time()-t1]

    dmin, liste = -1, []
    for mot in dictionnaire:
        d = levenshtein(mot_input, mot)
        if dmin==-1 or d<dmin:
            dmin=d
            liste = [mot]
        elif d==dmin:
            liste.append(mot)
    return [False, dmin, liste, time.time()-t1]

def trigrammes(mot, t=3):
    mot2 = "$"+mot+"$"
    l = []
    for i in range(len(mot2)-2):
        l.append(mot2[i:i+t])
    return l

bons_trigrammes = {}
for mot in dictionnaire:
    for trigr in trigrammes(mot):
        bons_trigrammes[trigr].append(mot)
        
