set_numbers = {1, 3, 5, 7}
#Il set non è indicizzato, NO ORDINE
#Il set non può avere elementi duplicati
#non restituisce errore se aggungiamo elementi già presenti
'''
set_numbers.add(9)
print(set_numbers)

lista_duplicati = [1,1,1,3,4,4,1,5,4,5,5,5,5]
set_list = set(lista_duplicati)
print(set_list)
'''
#DIZIONARIO: archiviare dati
#key and values
clienti = {1: {"nome": 'Aldo', 'cognome': 'Baglio'},
              2: {"nome": 'Giovanni', 'cognome': 'Storti'},
                3: {"nome": 'Giacomo', 'cognome': 'Poretti'}
            }
cliente = {"nome": 'Aldo', 'cognome': 'Perri'}
for element in cliente:
    print(element)

for key, value in clienti.items():
    print(value['nome'])


print(cliente.get('Phone', 'Phone not present')) #non aggiiunge la chiave 'Phone'
print(cliente.setdefault('Indirizzo', 'Indirizzo  non presente')) #aggiunge la chiave 'Indirizzo'
print(cliente)