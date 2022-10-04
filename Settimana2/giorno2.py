#Esercizio 1
"""Esercizio 1: Scrivi un programma che trasforma in maiuscolo tutte le
 consonanti di una stringa in input da tastiera (le vocali sono a e i o u)"""

stringa  = input('Inserisci una frase:')
stringa=stringa.upper()
stringa=stringa.replace("A","a")
stringa=stringa.replace("E","e")
stringa=stringa.replace("I","i")
stringa=stringa.replace("O","o")
stringa=stringa.replace("U","u")
print(stringa)








#Esercizio 2
"""Esercizio 2: Una persona brilla è all'interno di una griglia di strade 
(al centro di un incrocio), e in modo del tutto casuale prende una delle 4 
direzioni (nord è +, sud è -, est è +, ovest è -) e si muoverà di un numero 
casuale di passi (da 1 a 10) che lo porterà al centro di un nuovo incrocio.

Rappresenta la posizione della persona con la coppia di interi (x, y). 

Immagina che la persona sia all'interno di un piano cartesiano 
(x asse delle ordinate, y asse delle ascisse), implementa il cammino della 
persona brilla per 100 intersezioni a partire dalla posizione (0, 0),
visualizza la posizione finale. 

Esempio, alla prima iterazione se la persona
si sposta verso sud di 7 passi la sua nuova posizione sarà (0, -7), se alla
successiva si muove verso nord di 3 passi la sua nuova posizione sarà (0, -4)
"""
"""#importo libreria random
import random

#definisco le coordinate della posizione iniziale
i=0
posizione_x=0
posizione_y=0

#computo la posizione finale per 100 iterazioni
while i<100:
    posizione_x=posizione_x+random.randint(-10,10)
    posizione_y=posizione_y+random.randint(-10,10)
    print("iterazione: ",i," ","posizione x: ",posizione_x," ","posizione y: ",posizione_y)
    i=i+1

if posizione_x>0 and posizione_y>0:
    print("programma finito, la posizione finale è formata dalla coppia:","(",posizione_y,"N",";",posizione_x,"E",")")
elif posizione_x>0 and posizione_y<0:
    print("programma finito, la posizione finale è formata dalla coppia:","(",(-1)*posizione_y,"S",";",posizione_x,"E",")")
elif posizione_x<0 and posizione_y>0:
    print("programma finito, la posizione finale è formata dalla coppia:","(",posizione_y,"N",";",(-1)*posizione_x,"O",")")
else:
    print("programma finito, la posizione finale è formata dalla coppia:","(",(-1)*posizione_y,"S",";",(-1)*posizione_x,"O",")")
"""






#esercizio 3
"""Esercizio 3: Scrivi un programma che chiede all'utente in input:
1) i litri di benzina nel serbatoio
2) L'efficienza espressa in km per litro
3) Il prezzo della benzina per litro
Quindi visualizza il costo per 100 km e quanta distanza può percorrere l'auto con la benzina nel serbatoio 
"""

"""#Richiedo gli input
litri_serbatoio = int(input("Inserire litri di benzina nel tuo serbatoio: "))
efficienza = int(input("Inserisci l'efficienza della tua auto espressa in Km per Litro: "))
prezzo= int(input("Inserisci il prezzo attuale della benzina: "))

#Calcolo costo benzina per 100km
km_percorsi= 100
costo = (km_percorsi / efficienza) *prezzo
print("Il costo della benzina per percorrere 100km è di: ",costo,"€")

#Calcolo distanza che posso percorrere con l'attuale serbatoio
distanza= efficienza*litri_serbatoio
print("La distanza che può percorrere l'auto con la benzina nel serbatoio è di: ",distanza,"km")

#Calcolo prezzo benzina considerando anche i litri già disponibili nel serbatoio

km_mancanti = km_percorsi-distanza
if km_mancanti < 0 :
    print("Considerando i litri già disponibili nel serbatoio, dovrò spendere 0€ in benzina")
else :
    costo_mancanti = (km_mancanti / efficienza) * prezzo
    print("Considerando i litri già disponibili nel serbatoio, dovrò spendere", costo_mancanti, "€ in benzina")

"""






#Esercizio 4
"""Esercizio 4: Scrivi un programma che chiede in input all'utente una misura in metri e 
la converte in miglia, piedi e pollici"""

"""misura = int(input('Dammi una misurra in metri: '))

#creo le variabili fattore di conversione nelle rispettive misure
fattore_miglia=0.000621
fattore_piedi= 3.28084
fattore_pollici = 39.3701

#calcolo la conversione
misura_miglia= misura*fattore_miglia
misura_piedi= misura*fattore_piedi
misura_pollici= misura*fattore_pollici

print(misura,"m corrispondono a: ",misura_miglia,"miglia")
print(misura,"m corrispondono a: ",misura_piedi,"piedi")
print(misura,"m corrispondono a: ",misura_pollici,"pollici")
print("Fine programma")"""







#Esercizio 5
"""Esercizio 5: Scrivi un programma che chiede in input all'utente una stringa
e visualizza i primi 3 caratteri, seguiti da 3 punti di sospensione e quindi gli ultimi 3 caratteri."""

"""stringa = input("Inserisci una frase: ")

#controllo che la stringa sia di almeno 3 caratteri
while len(stringa) <3 :
    print("Occorre inserire un valore di almeno 3 caratteri")
    stringa = input("Inserisci una frase: ")

print(stringa[:3],"...",stringa[-3:])
print("fine programma")
"""







