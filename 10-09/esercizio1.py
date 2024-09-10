'''
Scrivete un programma che chiede una stringa all’utente e
restituisce un dizionario rappresentante la "frequenza di
comparsa" di ciascun carattere componente la stringa.
Esempio:
Stringa "ababcc",
Risultato
{"a": 2, "b": 2, "c": 2}
'''
test_string = 'abbacdeddzzzzz'
characters = {} #inizializzo dizionario vuoto

for element in test_string: #iter su tutti i caratteri della stringa
    if element not in characters: #controllo se il carattere è una chiave del dizionario
        characters[element] = 1 #se non è già chiave aggiungo la chiave e conto 1 elemento
    else:
        characters[element] += 1 #se è già presente la chiave aumento di 1 il conteggio

lista_valori = list(characters.values())
lista_chiavi = list(characters.keys())
ordered_characters = list(zip(lista_valori,lista_chiavi))
print(ordered_characters)
ordered_characters.sort(reverse = True)
ordered_characters = dict(ordered_characters)

ordered_characters2 = {ordered_characters[element]:element for element in ordered_characters}
print(ordered_characters2)
