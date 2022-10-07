import json
import statistics

file='/Users/kevincloud/Documents/EPICODEpythonProjects/venv/datasets/owid-covid-data.json'


"""
ANALISI COVID-2019
//
//
Requisiti:

Si intende analizzare gli effetti del Corona Virus confrontando
le statistiche Finlaindia (codice paese FIN) e Bielorussia (codice paese BLR), 
due paesi dell'est Europa che hanno scelto di adottare politiche di contenimento
del corona virus rispettivamente più restrittive e più lascive.

Inoltre si intende fare una ricerca nei due continenti
Nord America e Sud America per confrontare l'impatto che ha avuto il corona virus.

Si richiedono le seguenti statistiche per ogni paese e continente analizzato:

- Media stringency_index
- totale vaccinazioni
- Mediana del tasso di riproduzione
- Deviazione standard del tasso di riproduzione
- Media e Mediana dei casi giornalieri per tutto il periodo
- Media e Mediana dei morti giornalieri per tutto il periodo

"""


#Creo funzione per leggere il file json e inserirlo come dizionario

def read_json(file_path):
    """
    Legge un file JSON e inserisce i dati in un dizionario
    :param file_path: file path of json
    :return: data read from file
    """
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

dataset = read_json(file)


#ISPEZIONE DEL DATASET

if False:
    # 1)Verifico che il file sia un json
    print(type(dataset))

    # 2)Quali sono le chiavi del primo dizionario?
    for k in dataset.keys():
        print(k)

    # 3)Accedo alla prima chiave ed esploro
    for k in dataset['AFG'].keys():
        print(k)

    print(dataset['AFG']["continent"])
    print(dataset['AFG']["location"])

    print(dataset['AFG']["data"])
    print(type(dataset['AFG']['data']))

    # 4) La chiave "data" contiene una lista. Esploro la lista

    for elem in range(100, 104):
        print(dataset['AFG']['data'][elem])

""" La lista ha come elementi dei dizionari, dove ogni dizionario rappresenta un giorno.
    All'interno del dizionario ci sono delle chiavi che rappresentano delle misure giornaliere.
    
    !! ATTENZIONE !!
    Se la misura è assente per un dato giorno, la chiave relativa a quella misura non compare
    nel dizionario.
"""


"""
Breve fotografia della struttura dati

{   codice_paese_1 : xxx      <--- primo livello 
    codice_paese_2 : {   continent: xxx,      <--- secondo livello ( informazioni generali )
                     location: xxx,
                     ...
                     ...
                     ...
                     data: [{ giorno: giorno1,        <--- terzo livello è una lista di dizionari
                            misura1_giornaliera: xxx,
                            misura2_giornaliera: xxx,
                            misura3_giornaliera: xxx, 
                            ...
                            },
                            { giorno: giorno2,
                            misura1_giornaliera: xxx,
                            misura2_giornaliera: xxx,
                            ...
                            ...
                            }]
                },
    ...
    ...
    ...
}
"""

#Inizio a creare le funzioni che ritorneranno le statistiche di cui ho bisogno

def media_per_paese(dataset,codice_paese,misura):
    """
    Questa funzione restituisce la media di una misura scelta all'interno di un dataset e per un
    paese specifico.

    :param dataset: inserire un dataset di tipo dizionario
    :param codice_paese: inserire il codice del paese
    :param misura: inseirire la misura di cui si vuole ottenere la media
    :return: media della misura scelta
    """
    lista = []
    for i in range(0, len(dataset[codice_paese]['data'])):
        if (dataset[codice_paese]['data'][i].get(misura, None)) != None:
            list_1.append(dataset[codice_paese]['data'][i].get(misura))
    media = statistics.mean(lista)
    return media


def mediana_per_paese(dataset,codice_paese,misura):
    """
    Questa funzione restituisce la mediana di una misura scelta all'interno di un dataset e per un
    paese specifico.

    :param dataset: inserire un dataset di tipo dizionario
    :param codice_paese: inserire il codice del paese
    :param misura: inseirire la misura di cui si vuole ottenere la media
    :return: mediana della misura scelta
    """
    lista = []
    for i in range(0, len(dataset[codice_paese]['data'])):
        if (dataset[codice_paese]['data'][i].get(misura, None)) != None:
            lista.append(dataset[codice_paese]['data'][i].get(misura))
    mediana = statistics.median(lista)
    return mediana


def statistica_per_paese(dataset, codice_paese, misura, statistica):
    """
    Questa funzione restituisce una statistica di una misura scelta all'interno di un dataset e per un
    paese specifico.
    Le statistiche possibili sono: media, mediana, deviazione_standard

    :param dataset: inserire un dataset di tipo dizionario
    :param codice_paese: inserire il codice del paese
    :param misura: inseirire la misura di cui si vuole ottenere la media
    :param statistica: inserire in formato stringa la statistica che si vuole ottenere
    :return: media della misura scelta
    """
    lista = []
    for i in range(0, len(dataset[codice_paese]['data'])):
        if (dataset[codice_paese]['data'][i].get(misura, None)) != None:
            lista.append(dataset[codice_paese]['data'][i].get(misura))

    if statistica == "media":
        media = statistics.mean(lista)
        return media
    if statistica == "mediana":
        mediana = statistics.median(lista)
        return mediana
    if statistica == "deviazione_standard":
        deviazione_standard = statistics.stdev(lista)
        return deviazione_standard
    if statistica == "somma":
        somma = 0
        for i in range(len(lista)):
            somma = somma+lista[i]
        return somma
    else:
        return None
        print("Errore, la statistica ricercata non è stata inserita correttamente o non è presente in questa funzione")

#Definisco le funizoni per continente



def statistica_per_continente(dataset,continente,misura,statistica):
    lista = []
    for i in dataset:
        if dataset[i].get('continent', 'errore') == continente:
            for g in range(0, len(dataset[i]['data'])):
                if (dataset[i]['data'][g].get(misura, None)) != None:
                    lista.append(dataset[i]['data'][g].get(misura))
    if statistica == "media":
        media = statistics.mean(lista)
        return media
    if statistica == "mediana":
        mediana = statistics.median(lista)
        return mediana
    if statistica == "deviazione_standard":
        deviazione_standard = statistics.stdev(lista)
        return deviazione_standard
    if statistica == "somma":
        somma = 0
        for i in range(len(lista)):
            somma = somma + lista[i]
        return somma
    else:
        return None
        print("Errore, la statistica ricercata non è stata inserita correttamente o non è presente in questa funzione")



#Calcolo tutte le statistiche richieste per l'analisi

#Inizio dall'analisi per i paesi Finlandia e Bielorussia

lista_stats = ["media","mediana","deviazione_standard","somma"]
lista_misure = ["new_cases","new_deaths","reproduction_rate","new_vaccinations_smoothed","stringency_index"]

codice_finlandia ='FIN'
codice_bielorussia = 'BLR'

media_nuovi_casi_FIN = statistica_per_paese(dataset,codice_finlandia,lista_misure[0],lista_stats[0])
mediana_nuovi_casi_FIN = statistica_per_paese(dataset,codice_finlandia,lista_misure[0],lista_stats[1])
totale_vaccinazioni_FIN = statistica_per_paese(dataset,codice_finlandia,lista_misure[3],lista_stats[3])
media_stringency_FIN = statistica_per_paese(dataset,codice_finlandia,lista_misure[4],lista_stats[0])
mediana_tasso_riproduzione_FIN = statistica_per_paese(dataset,codice_finlandia,lista_misure[2],lista_stats[1])
devstd_tasso_riproduzione_FIN = statistica_per_paese(dataset,codice_finlandia,lista_misure[4],lista_stats[2])

media_nuovi_casi_BLR = statistica_per_paese(dataset,codice_bielorussia,lista_misure[0],lista_stats[0])
mediana_nuovi_casi_BLR = statistica_per_paese(dataset,codice_bielorussia,lista_misure[0],lista_stats[1])
totale_vaccinazioni_BLR = statistica_per_paese(dataset,codice_bielorussia,lista_misure[3],lista_stats[3])
media_stringency_BLR = statistica_per_paese(dataset,codice_bielorussia,lista_misure[4],lista_stats[0])
mediana_tasso_riproduzione_BLR = statistica_per_paese(dataset,codice_bielorussia,lista_misure[2],lista_stats[1])
devstd_tasso_riproduzione_BLR = statistica_per_paese(dataset,codice_bielorussia,lista_misure[4],lista_stats[2])



print("Paese:",codice_finlandia)
print("Stringency Index:", media_stringency_FIN)
print("Media nuovi casi:",media_nuovi_casi_FIN)
print("Mediana nuovi casi:",mediana_nuovi_casi_FIN)
print("Mediana tasso di riproduzione:",mediana_tasso_riproduzione_FIN)
print("Deviazione standard tasso di riproduzione:",devstd_tasso_riproduzione_FIN)
print("\n\n")

print("Paese:",codice_bielorussia)
print("Stringency Index:", media_stringency_BLR)
print("Media nuovi casi:",media_nuovi_casi_BLR)
print("Mediana nuovi casi:",mediana_nuovi_casi_BLR)
print("Mediana tasso di riproduzione:",mediana_tasso_riproduzione_BLR)
print("Deviazione standard tasso di riproduzione:",devstd_tasso_riproduzione_BLR)
print("\n\n")

#Continuo con l'analisi per tra i continenti

continente_1 ='North America'
continente_2 = 'South America'


media_nuovi_casi_CONT1 = statistica_per_continente(dataset,continente_1,lista_misure[0],lista_stats[0])
mediana_nuovi_casi_CONT1 = statistica_per_continente(dataset,continente_1,lista_misure[0],lista_stats[1])
totale_vaccinazioni_CONT1 = statistica_per_continente(dataset,continente_1,lista_misure[3],lista_stats[3])
media_stringency_CONT1 = statistica_per_continente(dataset,continente_1,lista_misure[4],lista_stats[0])
mediana_tasso_riproduzione_CONT1 = statistica_per_continente(dataset,continente_1,lista_misure[2],lista_stats[1])
devstd_tasso_riproduzione_CONT1 = statistica_per_continente(dataset,continente_1,lista_misure[4],lista_stats[2])

media_nuovi_casi_CONT2 = statistica_per_continente(dataset,continente_2,lista_misure[0],lista_stats[0])
mediana_nuovi_casi_CONT2 = statistica_per_continente(dataset,continente_2,lista_misure[0],lista_stats[1])
totale_vaccinazioni_CONT2 = statistica_per_continente(dataset,continente_2,lista_misure[3],lista_stats[3])
media_stringency_CONT2 = statistica_per_continente(dataset,continente_2,lista_misure[4],lista_stats[0])
mediana_tasso_riproduzione_CONT2 = statistica_per_continente(dataset,continente_2,lista_misure[2],lista_stats[1])
devstd_tasso_riproduzione_CONT2 = statistica_per_continente(dataset,continente_2,lista_misure[4],lista_stats[2])


print("Continente:",continente_1)
print("Stringency Index:", media_stringency_CONT1)
print("Media nuovi casi:",media_nuovi_casi_CONT1)
print("Mediana nuovi casi:",mediana_nuovi_casi_CONT1)
print("Mediana tasso di riproduzione:",mediana_tasso_riproduzione_CONT1)
print("Deviazione standard tasso di riproduzione:",devstd_tasso_riproduzione_CONT1)
print("\n\n")

print("Continente:",continente_2)
print("Stringency Index:", media_stringency_CONT2)
print("Media nuovi casi:",media_nuovi_casi_CONT2)
print("Mediana nuovi casi:",mediana_nuovi_casi_CONT2)
print("Mediana tasso di riproduzione:",mediana_tasso_riproduzione_CONT2)
print("Deviazione standard tasso di riproduzione:",devstd_tasso_riproduzione_CONT2)
print("\n\n")










