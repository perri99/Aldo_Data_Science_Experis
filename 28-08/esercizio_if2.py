stringa = input('Inserisci la stringa iniziale: ')
print('La stringa iniziale è: ', stringa)

scelta = input('Cosa vuoi fare? \n1. Aggiungere, 2. Sostituire, 3. Eliminare \n')

if scelta == '1':
    aggiunta = input('Inserisci la stringa che vuoi aggiungere ')
    stringa = stringa + aggiunta
elif scelta == '2': 
    parola_da_sostituire = input('Cosa vuoi sostituire? ') 
    if parola_da_sostituire in stringa:
        sostituzione = input('Con cosa sostituiamo? ')
        stringa = stringa.replace(parola_da_sostituire, sostituzione)   
    else:
        print('Non presente nella stringa')
elif scelta == '3':
    stringa = ''
    print('Ora la stringa è vuota')
else:
    print('Scelta non valida!!')
    
print(stringa)