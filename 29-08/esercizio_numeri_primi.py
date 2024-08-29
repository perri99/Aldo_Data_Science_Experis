prime_numbers = []

while len(prime_numbers) < 5:
    prime = True
    number = int(input('Inserisci un numero intero: '))
    for div in range(2, number): #controllo se il numero è primo, check sui possibili divisori
        if number % div == 0:
            prime = False
    if prime == True:
        prime_numbers.append(number)
        print('Hai inserito un numero primo: ', number)
    else:
        print('Il numero inserito non è primo!')
print('Hai inserito 5 numeri primi:')
print(prime_numbers)