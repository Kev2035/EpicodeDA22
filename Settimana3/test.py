import mysql.connector

user = 'root'
password = 'arm-sql-776-cr4ck'
host = '127.0.0.1'
database = 'discografia'

def connection_database (user, password, host, database):
    try:
        conn = mysql.connector.connect(user=user, password=password, host=host, database=database)
        return conn
    except  mysql.connector.errors.DatabaseError as db_error:
        print(db_error.msg)
        return None

def query_constructor(select, frm, join1=None, join2=None, where=None, groupby=None, orderby=None ):
    stmt = 'select %s from %s ' % (select,frm)
    if join1 is not None:
        stmt = stmt + 'join %s ' % join1
    if join2 is not None:
        stmt = stmt + 'join %s ' % join2
    if where is not None:
        stmt = stmt + 'where %s ' % where
    if groupby is not None:
        stmt = stmt + 'group by %s ' % groupby
    if orderby is not None:
        stmt = stmt + 'order by %s' % orderby
    stmt = stmt + ';'
    return stmt

def insert_new_values(insert,list1,list2):
    stm = 'insert into %s ' % (insert)
    stm = stm + '('
    for i in range(len(list1)):
        if i == len(list1)-1:
            stm = stm + "%s" %(list1[i])
        else:
            stm = stm + list1[i] + ','
    stm = stm + ') values ('
    for k in range(len(list2)):
        if k == len(list2)-1:
            stm = stm + '\'%s\'' %(list2[k])
        else:
            stm = stm + list2[k] + ','
    stm = stm + ')'
    return stm

def eliminazione(delete,where):
    stm = 'delete from %s ' % (delete)
    stm = stm + 'where %s ' % where
    return stm

#eseguo la connessione
conn = connection_database(user, password, host, database)
cursor = conn.cursor(buffered=True)

select = "NomeCantante"
frm = "canzone"
select = "NomeCantante"
frm = "canzone"
join1 = "esecuzione on canzone.CodiceReg=esecuzione.CodiceReg"
join2 = "autore on esecuzione.TitoloCanzone=autore.TitoloCanzone"
where = "nome=NomeCantante and nome like 'D%'"

prima_query = query_constructor(select,frm,join1,join2,where)
print(prima_query)

select = 'TitoloAlbum'
frm = 'disco'
join1 = 'contiene on disco.NroSerie=contiene.NroSerieDisco'
join2 = 'esecuzione on contiene.CodiceReg=esecuzione.CodiceReg'
where = 'esecuzione.Anno is NULL'

seconda_query = query_constructor(select,frm,join1,join2,where)
print(seconda_query)

select = 'distinct NomeCantante'
frm = 'cantante'
join1 = None
join2 = None
select2 = 'S1.NomeCantante'
frm2 = 'cantante as S1'
select3 = 'CodiceReg'
frm3 = 'cantante as S2'
where3 = 'S2.NomeCantante <> S1.NomeCantante ))'
where2 = 'CodiceReg not in ( ' + query_constructor(select3,frm3,where3)
where = 'NomeCantante not in ( ' + query_constructor(select2,frm2,where2)

terza_query = query_constructor(select,frm,join1,join2,where)
print(terza_query)

select = 'NomeCantante'
frm = 'cantante'
join1 = None
join2 = None
select2 = 'S1.NomeCantante'
frm2 = 'cantante as S1'
join3 = 'esecuzione on CodiceReg=S1.CodiceReg'
join4 = 'cantante as S2 on CodiceReg=S2.CodiceReg'
where2 = 'S1.NomeCantante <> S2.NomeCantante)'
where = 'NomeCantante not in (' + query_constructor(select2, frm2, join3, join2, where2)

quarta_query = query_constructor(select,frm,join1,join2,where)
print(quarta_query)

#Esegui la prima query
cursor.execute(prima_query)
result = cursor.fetchone()
print(result)

#Esegui la seconda query
cursor.execute(seconda_query)
result = cursor.fetchone()
print(result)

#Esegui la terza query
cursor.execute(terza_query)
result = cursor.fetchone()
print(result)

#Esegui la quarta query
cursor.execute(quarta_query)
result = cursor.fetchone()
print(result)


#INSERISCO UNA NUOVA RIGA
insert = 'autore'
list1 = ['nome','TitoloCanzone']
list2 = ['Salmo','1984']
new_values = insert_new_values(insert,list1,list2)
print(new_values)

cursor.execute(new_values)
conn.commit()
result = cursor.fetchall()
print(result)

#QUESTO CANCELLA UNA RIGA SOLO SE LA RIGA PRECEDENTE HA FUNZIONATO
delete= 'autore'
where = 'nome="Salmo"'
delete_1 = eliminazione(delete,where)
print(delete_1)

cursor.execute(delete_1)
conn.commit()
result=cursor.fetchall()
print(result)


conn.close()

