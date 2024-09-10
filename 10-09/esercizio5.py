'''
Scrivete un programma che utilizza il cifrario di Cesare per criptare una
parola o decriptarla.
Il Cifrario di Cesare è un algoritmo di crittografia che consiste nello spostare
ciascuna lettera di una certa quantità di posti nell'alfabeto. Per utilizzarlo, si
sceglie una chiave (scelta dall’utente) che rappresenta il numero di posti
di cui ogni lettera dell'alfabeto verrà spostata: ad esempio, se si sceglie
una chiave di 3, la lettera A diventerà D, la lettera B diventerà E e così via.
Per decifrare un messaggio cifrato con il cifrario di Cesare bisogna
conoscere la chiave utilizzata e spostare ogni lettera indietro di un numero
di posti corrispondente alla chiave.
'''

def range_char(start='a', stop='z'):
    return [chr(n) for n in range(ord(start), ord(stop) + 1)]

def encoding(stringa, key):
    stringa = stringa.lower()
    substrings = stringa.split(' ')
    alphabet = range_char()
    encoded_string = ''
    for substring in substrings:
        lista = [alphabet[((alphabet.index(i)+key) % 26)] for i in substring]
        substring = ''.join(lista)
        encoded_string = encoded_string + substring+' '
    
    return encoded_string

def decoding(stringa, key):
    return encoding(stringa, -key)

string_test = "ciao mi chiamo aldo"
encoded_string = encoding(string_test, 4)
print(encoded_string)
print(decoding(encoded_string,4))