'''
Scrivete una programma che richiede una lista di numeri all’utente e
fornisce in output un istogramma basato su questi numeri, usando asterischi
per disegnarlo
'''
number_of_inputs = 7
numbers_list = []
mark = '*'

for index in range(number_of_inputs):
    number = int(input('Inserisci un numero: '))
    numbers_list.append(number)

print('Ecco la distribuzione:')
for number in numbers_list:
    print(mark*number)