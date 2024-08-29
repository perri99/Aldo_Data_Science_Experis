nome_utente = input('Benvenuto! Inserisci nome utente:\n')

if nome_utente != 'Aldo': #Controllo se account presente: account non presente
    password = input('Account non presente nel sistema! Scegli una passsword:\n')
    password_check = input('Conferma password\n')
    if password == password_check: #doppio check password
        print('Account creato con successo!!')
        print('Le tue credenziali sono:\n Nome utente:', nome_utente, '\n Password:', password)
    else:
        print('Non hai confermato correttamente la password')
else: #controllo presenza account: acccount prresente
    password = input('Inserisci password\n')
    if password == 'password':
        scelta = int(input('Accesso eseguito con successo! Cosa vuoi fare?\n 1.Cambio credenziali 2. Exit\n'))
        if scelta == 1: #modifica credenziali
            nome_utente = input('Inserisci nuovo nome utenete\n')
            password_vecchia = input('Inserisci password vecchia\n')
            if password_vecchia == password:
                password = input('Inserisci nuova password\n')
                print('Le tue nuove credenziali sono:\n Nome utente:', nome_utente, '\n Password:', password)
            else:
                print('Password errata')
        else:
            print('Arrivederci!')
    else:
        print('Password errata!!')
