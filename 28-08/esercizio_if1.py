nome = input('Inserisci il nome che sto pensando: ')
if nome == 'Salvatore' or nome == 'salvatore':
    numero = int(input('Nome corretto, ora dimmi il numero che sto pensando '))
    if numero == 10:
        città = input('Numero corretto, ora dimmi una città ')
        if città == 'Roma' or città == 'roma':
            print('Città corretta! Hai vinto!')
        else:
            print('Città sbagliata')
    else:
        print('Numero errato')
else:
    print('Nome errato')