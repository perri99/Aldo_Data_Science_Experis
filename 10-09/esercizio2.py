'''
Scrivete un programma che chiede un numero all’utente e
restituisce un dizionario con il quadrato del numero, se è pari o
dispari e quante cifre contiene.
Esempio:
Numero 12
Risultato
{‘quadrato’: 144,’pari o dispari’:’pari’, ‘n. cifre’: 2 }
'''
number = int(input('Inserisci intero positivo: '))

dizionario = {}

dizionario['Quadrato'] = number**2

if number % 2 == 0: dizionario['Pari o Dispari'] = 'Pari'
else: dizionario['Pari o dispari'] = 'Dispari'

dizionario['Cifre'] = len(str(number))

print('Hai inserito', number)
print(dizionario)