import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    port = 8889,
    database = "esercpython"
)
#sql = "create table utenti(id int auto_increment primary key, nome varchar(255), cognome varchar(255))"

mycursor = mydb.cursor()
def inserisciDati():
    sql = "insert into utenti(nome, cognome) values(%s,%s)"
    val = ("mirko","antonioni")
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.lastrowid)

def selezione():
    sql = "select * from utenti where id > 3"

    mycursor.execute(sql)

    dati = mycursor.fetchone()

    print(dati)

    for dato in dati:
        print(dato)

def delete():
    sql = "delete from utenti where id = 4"

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "righe eliminate")



#delete()





        