while True: #ciclo principale
    numbers_list = []

    while True: #ciclo di inserimento, continua fino a risposta negativa dell'utente
        number = input('Inserisci un numero oppure s per uscire dall inserimento: ')
        if number == 's': 
            break #uscita dall'inserimento
        number = int(number)
        numbers_list.append(number) #aggiunta alla lista

    if len(numbers_list) == 0:
        print('Lista Vuota!')
    else:
        #ricerca del massimo con ciclo for
        max = numbers_list[0]
        for index in range(1, len(numbers_list)): #accesso agli elementi della lista
            if numbers_list[index] > max:
                max = numbers_list[index]
        print('Il massimo valore trovato con il ciclo for è', max)  

        #max con sorting
        numbers_list.sort()
        print('Il massimo trovato con il sorting è', numbers_list[len(numbers_list)-1])

        #conteggio numeri con while
        counter = 0
        index = 0
        while index < len(numbers_list):
            counter += 1
            index += 1
        print('Il ciclo while ha contato', counter, 'elementi')
        #check elementi con funzione len()
        print('La funzione len() restituisce', len(numbers_list))

        
    answer = input('Se vuoi terminare premi q, qualsiasi altro tasto se vuoi ripetere\n')
    if answer == 'q': #termina il programma
        break