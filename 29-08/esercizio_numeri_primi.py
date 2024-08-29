prime_numbers = [] #inizializzazione lista di numeri primi

while len(prime_numbers) < 5: #continuo il ciclo finchè non ho 5 elementi in prime_numbers
    prime = True #variabile di controllo di primalità
    number = int(input('Inserisci un numero intero: '))
    if number in prime_numbers: #se è un primo già inserito non lo accetto
        print('Hai già inserito questo numero primo')
    else:
        for div in range(2, number): #controllo se il numero è primo, check sui possibili divisori, si potrebbe diminuire il numero di iterazioni
            if number % div == 0:
                prime = False #se ottengo una divisione esatta allora number non è primo
        if prime == True:
            prime_numbers.append(number) #aggiungo il numero primo alla lista
            print('Hai inserito un numero primo: ', number)
        else:
            print('Il numero inserito non è primo!')

prime_numbers.sort()
print('Hai inserito 5 numeri primi:')
print(prime_numbers)