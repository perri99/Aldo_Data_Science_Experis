exit = False #variabile che controlla il while

while exit == False:
    number = int(input('Inserisci un numero: '))
    print('Ecco il conto alla rovescia')
    for i in range(number, -1, -1): #conto alla rovescia
        print(i)
    answer = int(input('Vuoi inserire un altro numero\n 1.Si 2.No\n'))
    if answer == 2:
        exit = True
                       
