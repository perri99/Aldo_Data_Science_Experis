'''
Scrivete un programma che utilizza una funzione che accetta
come parametro una stringa passata dall’utente e restituisce in
risposta se è palindroma o no.
Esempio:
‘I topi non avevano nipoti’ è palindroma
'ciao' non è palindroma
'''
def clear_string(stringa):
    disturbi = [' ', ',', '.', ';', ':', '!', '?', "'"]
    for element in disturbi:
        stringa = stringa.replace(element, '')
    return stringa

def is_palindromo(stringa):
    if stringa.isalpha() == False: stringa = clear_string(stringa)
    stringa = stringa.upper()
    stringa_reversed = stringa[::-1]
    if stringa == stringa_reversed:
        print('Stringa palindroma!')
        return True
    else:
        print('Stringa non palindroma!')
        return False

string_test = "Ai lati d'Italia"
is_palindromo(string_test)
print(string_test)