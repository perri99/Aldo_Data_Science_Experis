while True: #ciclo principale
    numbers_list = []
    while True: #ciclo di inserimento, continua fino a risposta negativa dell'utente
        number = int(input('Inserisci un numero: '))
        numbers_list.append(number) #aggiunta alla lista
        answer = input('Premi n se non vuoi aggiungere altri numeri, qualsiasi altro tasto altrimenti')
        if answer == 'n' or answer == 'N': #uscita dall'inserimento
            break
    for index in range(len(numbers_list)): #accesso agli elementi della lista
        numbers_list[index] = numbers_list[index]**2 #sostituzione degli elementi con il loro quadrato
    print(numbers_list)
    answer = input('Se vuoi terminare premi q, qualsiasi altro tasto se vuoi ripetere\n')
    if answer == 'q': #termina il programma
        break
