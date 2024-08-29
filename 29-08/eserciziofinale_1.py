stop = False #variabile di controllo del while

while stop == False:
    number = int(input('Inserisci un numero intero:'))
    if number % 2 == 0:
        print('Il numero è pari')
    else:
        print('il numero è dispari')
    answer = input('Inserisci q per uscire, qualsiasi altro tasto per continuare\n')
    if answer == 'q':
        stop = True