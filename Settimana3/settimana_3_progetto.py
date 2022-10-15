#Progetto della terza settimana

"""
Ideazione interrogazioni per base di dati di una web app relativa ad un e-commerce
di prodotti informatici, sviluppo applicazione in Python con connessione a DBMS
MySQL con Pandas e con il connettore, implementazione interrogazioni ideate
tramite funzioni ad-hoc. Vincolo: proporre almeno 10 interrogazioni identiche,
sia utilizzando i DataFrame di Pandas che utilizzando i cursori.
Il database è fornito in input.
"""

import mysql.connector
from sqlalchemy import create_engine
import pandas as pd

#Qui si trovano tutte le funzioni utilizzate in questo programma

def python_phone_sql (user, password, host, database):
    """
    Questa funzione permette di collegare python al database con le credenziali mysql
    """
    try:
        conn = mysql.connector.connect(user=user, password=password, host=host, database=database)
        return conn
    except  mysql.connector.errors.DatabaseError as db_error:
        print(db_error.msg)
        return None

def query_builder(slct, frm, join = None, where=None, groupby=None, having=None, orderby=None, inner_query=False ):
    """
    Questa funzione permette di costruire delle query sql.
    :param slct: specificare il valore dopo SELECT
    :param frm:  specificare il valore dopo FROM
    :param join: specificare il tipo di JOIN e il valore che ne sussegue, come una lista di JOIN.
    :param where: specificare il valore dopo WHERE
    :param groupby: specificare il valore dopo GROUP BY
    :param having: specificare il valore dopo HAVING
    :param orderby: specificare il valore dopo ORDER BY
    :param inner_query: la query si trova dentro un'annidamento? Se sì: True, se no:False
    :return: ritorna una stringa contentente la query
    """
    stmt = 'select %s from %s ' % (slct,frm)
    if join is not None:
        for i in join:
            stmt = stmt + i + ' '
    if where is not None:
        stmt = stmt + 'where %s ' % where
    if groupby is not None:
        stmt = stmt + 'group by %s ' % groupby
    if having is not None:
        stmt = stmt + 'having %s ' % having
    if orderby is not None:
        stmt = stmt + 'order by %s' % orderby
    if inner_query == False:
        stmt = stmt + ';'
    return stmt

def execute_query (cursor,query):
    """
    Questa funzione esegue una query tramite mysql connector
    :param cursor: cursore
    :param query: stringa della query che si desidera eseguire
    :return: La query viene eseguita nel cursore
    """
    return cursor.execute(query)

def show_query_results (cursor,fetch='one', fetchsize=None):
    """
    Questa funzione mostra il risultati di una query eseguita tramite mysql connector
    :param cursor: cursore
    :param fetch: tipo di visualizzazione tra "one" se 1 riga, "all" se tutte le righe, "many" se il numero di righe sono da specificare
    :param fetchsize: numero intero di righe da visualizzare, presente solo se fetch = 'many'
    :return:
    """
    if fetch == 'one':
        result = cursor.fetchone()
        return result
    elif fetch == 'all':
        result = cursor.fetchall()
        return result
    elif fetch == 'many':
        if fetchsize == None:
            print('errore: non hai definito il numero di righe che vuoi vedere')
            return None
        else:
            result = cursor.fetchmany(fetchsize)
            return result
    else:
        print("errore: il tipo di visualizzazione che hai richiesto non è contemplato, prova con: one, all o many")
        return None


def sql_phone_pandas(user,password,host,database):
    """
    Questa funzione connette pandas con il server mysql una volta fornite le credenziali.
    """
    db_connection_str = 'mysql+pymysql://'+user+':'+password+'@'+host+'/'+database
    db_connection = create_engine(db_connection_str)
    return db_connection

def sql_to_pandas (db_connection, query):
    """
    Questa funzione esegue una query sotto forma di stringa e riporta il risultato in un dataframe Pandas
    """
    return pd.read_sql(query, db_connection)


#Definisco le variabili per l'accesso alla connessione con mysql
user = 'root'
password = 'arm-sql-776-cr4ck'
host = '127.0.0.1'
database = 'ecommerce'

#inizio la connessione tra python e sql e inizializzo il cursore
conn = python_phone_sql(user, password, host, database)
cursor = conn.cursor(buffered=True)

#Inizio la connessione tra sql e pandas
db_connection = sql_phone_pandas(user,password,host,database)


#Inizio a definire le query

#1) Qual è il costo medio delle spedizioni?

slct = 'avg(spedizione.costo)'
frm = 'ordine'
join = ['join pasp01 on ordine.paspid = pasp01.paspid','join spedizione on pasp01.spid = spedizione.spid']

query_str = query_builder(slct,frm,join)
query=execute_query(cursor,query_str)
results = show_query_results(cursor,'one')
print('01) Il costo medio della spedizione è:')
print(results)

df01 = sql_to_pandas(db_connection,query_str)

#2) Qual è la spesa media delle aziende?
slct = 'avg(orpr01.prezzo)'
frm = 'utente'
join = ['join ordine on utente.uid = ordine.uid','join orpr01 on ordine.oid= orpr01.oid']
where = 'societa = 1'


query_str = query_builder(slct,frm,join,where)
query=execute_query(cursor,query_str)
results = show_query_results(cursor,'one')
print('02) La spesa media delle aziende è:')
print(results)

df02 = sql_to_pandas(db_connection,query_str)

#3) Qual è la percentuale di ordini conclusi sul totale?
inner_slct='count(ordine.oid)'
inner_frm='ordine'
sub_query = query_builder(inner_slct,inner_frm,inner_query=True)

slct ='count(ordine.oid)/'+'('+sub_query+')'
frm ='ordine'
join = ['join stato on ordine.stid = stato.stid']
where = "stato.nome='concluso'"

query_str = query_builder(slct,frm,join,where)
print(query_str)
query=execute_query(cursor,query_str)
results = show_query_results(cursor,'one')
print("03) La percentuale di ordini conclusi sul totale è:")
print(results)

df03 = sql_to_pandas(db_connection,query_str)

#4) Qual è la città alla quale si fanno più spedizioni?
slct='indirizzo.citta, count(ordine.oid) as numero_ordini'
frm = 'ordine join indirizzo on ordine.inid = indirizzo.inid'
grpb = 'indirizzo.citta'
ordrb = 'numero_ordini desc'

query_str= query_builder(slct,frm,groupby=grpb,orderby=ordrb)
query=execute_query(cursor,query_str)
results = show_query_results(cursor,'one')
print("04) La città dalla quale si fanno più spedizioni è:")
print(results)

df04 = sql_to_pandas(db_connection,query_str)

#5) Qual è la categoria merceologica che fattura di più
inner_slct= 'sum(prezzo)'
inner_frm = 'orpr01'
sub_query = query_builder(inner_slct,inner_frm,inner_query=True)

slct = 'categoria.nome, sum(prezzo) as totale_fatturato, (sum(prezzo)/ ('+ sub_query +')*100) as percentuale_su_fatturato'
frm = 'categoria'
join =['left join prodotto on categoria.cid = prodotto.cid', 'join orpr01 on prodotto.pid = orpr01.pid']
grpb = 'categoria.cid'
ordb = 'totale_fatturato desc'

query_str= query_builder(slct,frm,join,groupby=grpb,orderby=ordb)
query=execute_query(cursor,query_str)
results = show_query_results(cursor,'many',3)
print("05) la categoria merceologica che fattura di più è: ")
print(results)

df05 = sql_to_pandas(db_connection,query_str)

#06 Qual è il fatturato medio degli utenti iscritti alla newsletter
slct = 'avg(prezzo) as Media_fatturato'
frm = 'utente'
join = ['join ordine on utente.uid=ordine.uid','join orpr01 on ordine.oid=orpr01.oid']
where = 'utente.newsletter = 1'

query_str = query_builder(slct,frm,join,where=where)
query=execute_query(cursor,query_str)
results = show_query_results(cursor,'all')
print("06) Il fatturato medio degli utenti iscritti alla newsletter è:")
print(results)

df06 = sql_to_pandas(db_connection,query_str)

#07 Qual è il fatturato medio degli utenti non iscritti alla newsletter
slct = 'avg(prezzo) as Media_fatturato'
frm = 'utente'
join = ['join ordine on utente.uid=ordine.uid','join orpr01 on ordine.oid=orpr01.oid']
where = 'utente.newsletter = 0'

query_str = query_builder(slct,frm,join,where=where)
query=execute_query(cursor,query_str)
results = show_query_results(cursor,'one')
print("07) Il fatturato medio degli utenti non iscritti alla newsletter è:")
print(results)

df07 = sql_to_pandas(db_connection,query_str)
#08 Totale ordini rivenditori e totale utenti standard
slct = 'listino.nome, count(orpr01.lsid)'
frm = 'orpr01 join listino on orpr01.lsid=listino.lsid'
grpb = 'listino.nome'

query_str = query_builder(slct,frm,groupby=grpb)
query=execute_query(cursor,query_str)
results = show_query_results(cursor,'all')
print("08) Totale ordini rivenditori e totale ordini utenti standard:")
print(results)

df08 = sql_to_pandas(db_connection,query_str)
#09 Categoria merceologica con più disponibilità
slct= 'categoria.nome as nome_categoria,sum(prodotto.quantita) as quantita_disponibile'
frm='categoria'
join=['left join prodotto on categoria.cid=prodotto.cid']
grpb='categoria.nome'
having='quantita_disponibile is not null and quantita_disponibile >0'
order_by='quantita_disponibile desc'

query_str = query_builder(slct,frm,join,groupby=grpb,having=having,orderby=order_by)
query=execute_query(cursor,query_str)
results = show_query_results(cursor,'many',3)
print("09) Categoria merceologica con più disponibilità:")
print(results)

df09 = sql_to_pandas(db_connection,query_str)

#10 Rapporto tra velore ordini conclusi e valore ordini in esecuzione
inner_slct = 'sum(prezzo)'
inner_frm = 'ordine'
inner_join = ["join stato on ordine.stid = stato.stid","join orpr01 on ordine.oid = orpr01.oid where stato.nome ='in elabora-zione'"]

sub_query = query_builder(inner_slct,inner_frm,inner_join,inner_query=True)

slct= 'sum(prezzo)/ '+'('+sub_query+')'
frm = 'ordine'
join = ['join stato on ordine.stid = stato.stid', 'join orpr01 on ordine.oid=orpr01.oid']
where = "stato.nome='concluso'"

query_str=query_builder(slct,frm,join,where)
query=execute_query(cursor,query_str)
results = show_query_results(cursor,'all')
print("10) Rapporto tra valore ordini conclusi e valore ordini in esecuzoine:")
print(results)

df10 = sql_to_pandas(db_connection,query_str)


conn.close()


print('Infine mostrare i risultati come df pandas')
print(df01.head())
print(df02.head())
print(df03.head())
print(df04.head())
print(df05.head())
print(df06.head())
print(df07.head())
print(df08.head())
print(df09.head())
print(df10.head())





