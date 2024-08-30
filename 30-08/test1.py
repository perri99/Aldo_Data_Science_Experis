while True: #ciclo principale ripetizione programma
    words_list = []

    #ciclo di inserimento
    while True:
        word = input('Inserisci la parola che vuoi aggiungere, premi s per terminare inserimento\n')
        if word == 's':
            break #esco dall'inserimento se utente inserisce 's'
        words_list.append(word) #aggiungo parola alla lista
    #stampa lista
    print('Hai inserito le seguenti parole\n', words_list)
    #stampa elemento per elemento
    print('In successione hai inserito:')
    for word in words_list:
        print(word)
    #richiesta uscita
    answer = input('Premi q se vuoi terminare, qualsiasi altro tasto per continuare ')
    if answer == 'q':
        break
