'''
Create un gestionale scolastico in cui l'utente può inserire, modificare o eliminare, 
alunni voti e medie e naturalmente anche solo visualizzare i dati in database, 
questo programma utilizzerà un db sql come archivio
'''
import mysql.connector as sql

mydb = sql.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    port = 3306,
)
mycursor = mydb.cursor()

def apri_database(mycursor):
    
    mycursor.execute("USE scuola")
    

def crea_database(mycursor):
    query = 'CREATE DATABaSE scuola'
    mycursor.execute(query)
    print('Creato DATABASE scuola')
    
    #return mycursor

def crea_tabella(mycursor):
    query = 'CREATE TABLE studenti(ID INT  PRIMARY KEY, nome VARCHAR(255), cognome VARCHAR(255),\
    media_voti FLOAT)'
    mycursor.execute(query)
    #mydb.commit()
    print('Creata tabella studenti')

def show_table(mycursor):
    query = 'select * from studenti' 
    mycursor.execute(query)
    dati = mycursor.fetchall()
    for dato in dati:
        print(dato)
    print('Tabella esistente')
    
def check_id(mycursor, id):
    query = 'SELECT id from studenti where id = %s'
    mycursor.execute(query, (id,))
    lista_id = mycursor.fetchall()
    #print(lista_id)
    return len(lista_id)

def aggiungi_studente(mycursor):
    query = 'INSERT INTO studenti(id, nome, cognome, media_voti) \
        VALUES (%s, %s, %s, %s)'
    id = int(input('Inserisci ID '))
    #lista_id = restituisci_id(mycursor)
    if check_id(mycursor, id) == 0:
        nome = input('Inserisci nome: ')
        cognome = input('Inserisci cognome: ')
        media = float(input('Inserisci media: '))
        values = (id, nome, cognome, media)
        mycursor.execute(query, values)
        mydb.commit()
    else:
        print('Id già presente')
    

def modifica_studente(mycursor):
    id = int(input('Inserire ID dello studente da modificare: '))
    choice = input('Cosa vuoi modificare? 1.Nome, 2.Cognome, 3.Media Voto')
    if choice == '1':
        nome_nuovo = input('Inserisci nome nuovo ')
        query = 'UPDATE studenti SET nome = %s where id = %s'
        values = (nome_nuovo, id)
    elif choice == '2':
        cognome_nuovo = input('Inserisci cognome nuovo ')
        query = 'UPDATE studenti SET cognome = %s where id = %s'
        values = (cognome_nuovo, id)
    elif choice == '3':
        media_nuova = float(input('Inserisci media nuova '))
        query = 'UPDATE studenti SET media_voti = %s where id = %s'
        values = (media_nuova, id)
    try:
        mycursor.execute(query, values)
        mydb.commit()
    except:
        print('Scelta non valida')

def elimina_studente(mycursor):
    id = int(input('Inserire ID dello studente da eliminare: '))
    query = 'DELETE from studenti where id = %s'
    value = (id,)
    mycursor.execute(query, value)
    mydb.commit()


while True:
    try:
        apri_database(mycursor)
    except:
        crea_database(mycursor)
    try:

        choice = input('Scegli cosa fare: 1.mostra 2.aggiungi studente 3.modifica studente 4. elimina studente 5. Esci')
        if choice == '1':
            show_table(mycursor)
        elif choice == '2':
            aggiungi_studente(mycursor)
        elif choice == '3':
            modifica_studente(mycursor)
        elif choice == '4':
            elimina_studente(mycursor)
        elif choice == '5':
            break
    except:
        crea_tabella(mycursor)


