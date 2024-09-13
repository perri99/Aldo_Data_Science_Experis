

#lista.append(12)

#lista.insert(0,"primo")

#lista.extend(lista2)

#lista2.sort(reverse=True)

#print(lista.index("ciao"))

#print(lista2)
"""
lista = ["ciao","a","tutti", 8, 8.88, [1,2,3]]

lista2 = [1,2,3,11,7,8,10]

elemento = list(enumerate(lista))

for indice, valore in enumerate(lista):
    print(f"indice: {indice}, valore: {valore}")
"""
#print(elemento)

#lista.remove("tutti")

#del lista[2]

#lista.pop(2)

#lista[2] = "qualcuno"

#print(lista)

#stringa = "111ciia"

#print(stringa.endswith("tutti"))

#print(stringa.isdecimal())

#print(stringa.lower())

#print(stringa.count("11"))

#lista = stringa.split("-")

#stringa2 =stringa.replace("ciao", "arrivederci")

#print(stringa2)

#print(lista[0])

"""lista = ["ciao","a","tutti"]

stringa = "-".join(lista)

print(stringa)"""

"""lista = ["ciao","a","tutti"]

stringa ="ciao a tutti"

print("ci"in lista)"""

"""lista = [1,2,3, "ciao"]

lista2 = []
for element in lista: lista2.append(str(element))

lista3 = [str(el) for el in lista]

print(lista3)"""

"""stringa = str(lista)

print(stringa[1])"""


"""lista = [1,2,3,4,5]

tupla = (1,2,3,4,5)

set = {1,2,3,4,5, 5,5}


tommaso = {"nome":"tommaso","cognome":"muraca","ruolo":"formatore"}
mirko = {"nome":"mirko","ruolo":"formatore"}

utenti = {}

utenti[0] = tommaso
utenti[1] = mirko"""

"""utenti = {0: {'nome': 'tommaso', 'cognome': 'muraca', 'ruolo': 'formatore'}, 
          1: {'nome': 'mirko', 'ruolo': 'formatore'}}


utente1 = utenti[0]

#print(utente1.get("indirizzo","indirizzo non presente"))

print(utente1.setdefault("indirizzo","indirizzo non presente"))

print(utente1)"""

"""tupla = (5,1,12,11,4)

print(sorted(tupla))

print(tupla)

dizionario = {"a":1,"b":13,"c":11, "d":5}

lista_valori =list(dizionario.values())

lista_chiavi = list(dizionario.keys())

dizionario2 = dict(zip(lista_valori,lista_chiavi))

dizionario3 = {}

for element in sorted(dizionario2, reverse=True): dizionario3[dizionario2[element]] =element

#print(dizionario3)

dizionario4 = {dizionario2[element]:element for element in sorted(dizionario2, reverse=True) }

print(dizionario4)


def funz1(*argomenti):
    print(argomenti[0])
    

#funz1("ciao","a","tutti" )


def funz2(**argomenti):
    print(argomenti["nome"])
    

#funz2(nome="Tommaso",cognome = "Muraca",via ="via di qui", eta = 37 )


def pari_dispari(n):
    if n%2==0:
        return True
    else:
        return False

lista = [1,2,3,4,5,6]

listapari = [n for n in lista if pari_dispari(n)]

listapari2 = list(filter(pari_dispari, lista))

#print(listapari2)

def triplica(n):
    return n*3

listaT = [triplica(n) for n in lista]

listaT2 = list(map(triplica, lista))

#print(listaT2)


stringa1 = "i topi non avevano nipoti"

stringa2 =""

caratteri =" .,:-"

for char in caratteri:
    stringa1 = stringa1.replace(char,"")

print(stringa1)

dizionario = {0:False, 1:True}

if stringa1 == "ciao":
    print("questo") 
elif stringa1 == "ciao2":
    print("quello") 
"""



#import random

#print(random.random())

#print(random.randint(5,100))

#print(random.randrange(1,100,5))
#lista = ["tommaso", "mirko", "alessandro","antonio","michele","ecc"]

#print(random.choice(lista))

"""import datetime

var =datetime.datetime(2024,9,10,8,10,10)

print(datetime.datetime.now())



a = 10

b = 0
try:
    print(a/b)
    print("codice eseguito")

except TypeError as e:
    print(f"codice alternativo, errore: {e}")



print("vai avanti")
"""
def lettura_file(file):
    with open(file,"r") as myfile:
        contenuto = myfile.read()
        return contenuto



"""contenuto =lettura_file("testCsv.txt")

righe = contenuto.split("\n")

print(righe)

for i in range(1,len(righe)):
    print(righe[i].split(",")[0])"""

def scrittura_file(file, stringa):
    with open(file,"a") as myfile:
        myfile.write(stringa)

"""nome = "alfredo"
cognome = "verdi"
via = "via milano"

stringa ="\n"+nome+","+cognome+","+via

scrittura_file("testCsv.txt", stringa)
for i in range(10):
    with open("prova.txt","a") as myfile:
        myfile.write(f"\n{i}")"""
"""i = 0

while i < 5:
    print(i)
    valore = input("vuoi uscire: ")
    if valore== "si":
        break
    i+=1
else:
    print("finito ciclo")"""

import pickle

"""dizionario = {1:"tommaso",2:"mirko"}

dizB = pickle.dumps(dizionario)

with open("binario.bin","wb") as myfile:
    myfile.write(dizB)"""


with open("binario.bin","rb") as myfile:
    contenuto = myfile.read()

contenuto = pickle.loads(contenuto)
print(contenuto)




