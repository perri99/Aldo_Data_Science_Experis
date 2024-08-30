while True: #ciclo principale
    numbers_list1 = []
    numbers_list2 = []
    sum_list = []
    number_of_elements = 5

    #riempimento prima lista
    while len(numbers_list1) < number_of_elements:
        number = int(input('Inserisci numero intero per la prima lista: '))
        numbers_list1.append(number)

    #riempimento seconda lista
    while len(numbers_list2) < number_of_elements:
        number = int(input('Inserisci numero intero per la seconda lista: '))
        numbers_list2.append(number)
    
    #somma puntuale
    for index in range(number_of_elements):
        sum_list.append(numbers_list1[index] + numbers_list2[index])
    
    #stampa risultato
    print('La somma delle due liste è\n', sum_list)

    #richiesta uscita
    answer = input('Premi q se vuoi terminare, qualsiasi altro tasto per continuare ')
    if answer == 'q':
        break