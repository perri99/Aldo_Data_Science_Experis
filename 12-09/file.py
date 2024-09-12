def leggi_righe(file):
    with open(file, 'r') as file:
        righe = file.read()
    return righe

def aggiungi_riga(file, contenuto):
    with open(file, 'a') as file:
        file.write('\n' + contenuto)
    

file = '12-09/prova.csv'
riga_da_aggiungere = ['Fedrico', 'Bertoia', '21/12/1999']
riga_da_aggiungere=', '.join(riga_da_aggiungere)
nome = 'Giuseppe'
cognome = 'Salvatore'
data = '12/03/1987'
aggiungi_riga(file, riga_da_aggiungere)
aggiungi_riga(file, nome + ', '+cognome+', ' + data )
contenuto = leggi_righe(file)
righe = contenuto.split('\n')

for riga in righe:
    print(riga)

lista_nomi = [righe[i].split(",")[0] for i in range(1, len(righe))]

print(lista_nomi)