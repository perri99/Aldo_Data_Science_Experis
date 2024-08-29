#account di default
default_user = 'admin'
default_password = 'password'
answer1 = ''
answer2 = ''
#login
user = input('Inserisci nome utente \n')
if user == default_user: #controllo utente registrato
    password = input('Inserisci password\n')
    if password == default_password: #controllo password
        choice = int(input('Benvenuto! Cosa vuoi fare?\n \
                           1. Cambiare nome utente 2. Cambiare password 3.Impostare domande segrete\n'))
        if choice == 1: #cambio nome utente
            new_user = input('Inserisci nuovo nome utente:\n')
            default_user = new_user
            print('Il tuo nuovo nome utente è', default_user)
        elif choice == 2: #cambio password
            password = input('Inserisci vecchia password\n') #richiesta password vecchia
            if password == default_password:
                new_password = input('Inserisci nuova password:\n')
                new_password_check = input('Conferma password\n')
                if new_password == new_password_check: #conferma password nuova, deve essere inserita 2 volte
                    default_password = new_password
                    print('Cambio password avvenuto con successo!')
                else:
                    print('Le due password non coincidono')
            else:
                print('Hai inserito la password errata')
        elif choice == 3: #imposta domande segrete
            choice_question = int(input('Quale domanda vuoi impostare?\n 1. Città 2. Animale\n'))#scelta domanda da impostare
            if choice_question == 1:
                answer1 = input('Dove sei nato?\n')
                print('Hai correttamente impostato la domanda di sicurezza')
            elif choice_question == 2:
                answer2 = input('Qual è il tuo animale preferito?\n')
                print('Hai correttamente impostato la domanda di sicurezza')
            else:
                print('scelta non consentita')
        else: #scelta non consentita
            print('Scelta non consentita!')
    else:
        print('La password è errata!')
else:
    print('Nome utente non registrato!')