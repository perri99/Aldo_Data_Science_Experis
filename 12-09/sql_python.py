import mysql.connector as sql

mydb = sql.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    port = 3306,
    database = 'esercitazionepython'
)

mycursor = mydb.cursor()

#sql1 = "CREATE DATABASE esercitazionepython"
#mycursor.execute(sql1)
#mycursor.execute('ALTER TABLE utenti\
 #                ADD cognome VARCHAR(255)')
#mycursor.execute("")
#mycursor.execute("SHOW TABLES")
def inserisci_dati():
    inserisci = "INSERT INTO utenti(nome, cognome) VALUES(%s,%s)"

    #values = ('Aldo', 'Perri')
    values_list = [('Giuseppe','Rossi'), ('Tommaso', 'Verdi')]
    mycursor.executemany(inserisci, values_list)

    #commit
    mydb.commit()
    print(mycursor.rowcount, "record inseriti")
    print('Ultimo ID', mycursor.lastrowid)

def selezione():
    seleziona = "select * from utenti where id > 2" 
    mycursor.execute(seleziona)

    dati = mycursor.fetchall()
    for dato in dati:
        print(dato)

def delete():
    query = 'delete from utenti where id = 2'
    mycursor.execute(query)
    mydb.commit()
    print('Righe eliminate:', mycursor.rowcount)

delete()