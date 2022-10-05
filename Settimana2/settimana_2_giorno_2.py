#esercizio1

"""stringa = input ("Inserisci una lista di parole:").upper()
stringanuova = stringa.replace('A','a').replace('E','e').replace('O','o').replace('U','u').replace('I','i')
l=stringanuova.split(' ')

#versione breve
a = tuple([elem for elem in l if "a" in elem])
e = tuple([elem for elem in l if "e" in elem])
i = tuple([elem for elem in l if "i" in elem])
o = tuple([elem for elem in l if "o" in elem])
u = tuple([elem for elem in l if "u" in elem])
dizionario2={'a':a,'e':e,'i':i,'o':o,'u':u}
print(dizionario2)
"""
#Versione Lunga
"""a = []
e = []
i = []
o = []
u =[]
for elem in l:
    if "a" in elem:
        a.append(elem)
    if "e" in elem:
        e.append(elem)
    if "i" in elem:
        i.append(elem)
    if "o" in elem:
        o.append(elem)
    if "u" in elem:
        u.append(elem)
    else:
        pass
a = tuple(a)
e = tuple(e)
i = tuple(i)
o = tuple(o)
u = tuple(u)

dizionario ={'a':a, 'e':e, 'i':i, 'o':o,'u':u}
print(dizionario)"""

#esercizio2

continuare = True
lista=[[],[]]

while continuare == True:
    lista[0].append(input("Nome cliente?"))
    lista[1].append(float(input("Ammontare spesa?")))
    continuare = bool(int(input("Vuoi continuare? Se sì inserisci 1, se no inserisci 0")))


indice_max= lista[1].index(max(lista[1]))
print("Nome del cliente che ha speso di più è {} per un valore di {}€".format(lista[0][indice_max],lista[1][indice_max]))

indice_min= lista[1].index(min(lista[1]))
print("Nome del cliente che ha speso di meno è {} per un valore di {}€".format(lista[0][indice_min],lista[1][indice_min]))

#Trovo la media
somma = 0
for i in lista[1]:
    somma = somma + i
media = somma/len(lista[1])
print("la media è:{}".format(media))

#Trovo la mediana
print(lista[1])
lista[1].sort()
print(lista[1])

if len(lista[1])%2 != 0 :
    indice_mediana=int(len(lista[1])/2)+1
    mediana = lista[1][indice_mediana]
else :
    indice_mediana=len(lista[1])/2
    mediana = lista[1][indice_mediana]

print("Infine la mediana è {}".format(mediana))









