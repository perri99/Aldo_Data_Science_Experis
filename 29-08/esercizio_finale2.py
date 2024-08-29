exit = False #variabile controllo while

while exit != True: #se exit è False continua a iterare
    number = int(input('Inserisci un numero: '))
    numbers_list = [] #lista vuota da riempire
    for num in range(number+1):
        numbers_list.append(number-num)
    print(numbers_list)
    answer = input('Premi q per uscire, altro tasto altrimenti\n')
    if answer == 'q':
        exit = True

    