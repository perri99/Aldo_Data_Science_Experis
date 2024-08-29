exit = False

while exit != True:
    number = int(input('Inserisci un numero: '))
    numbers_list = []
    for num in range(number+1):
        numbers_list.append(number-num)
    print(numbers_list)
    answer = input('Premi q per uscire, altro tasto altrimenti\n')
    if answer == 'q':
        exit = True

    