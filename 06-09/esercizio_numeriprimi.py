'''
Esercizio numeri primi
'''
def d_check_primality(function):
    def wrapper(*args, **kwargs):
        _, number = function()
        prime = True
        for div in range(2, int(number**0.5)+1): #controllo se il numero è primo, check sui possibili divisori
            if number % div == 0:
                prime = False
                print('Il numero inserito non è primo! Il più piccolo divisore è', div)
                break #esco dal for, so già che non è primo
        if prime == True:
            #prime_numbers.append(number) #aggiungo il numero primo alla lista
            print('Hai inserito un numero primo: ', number)
            div = 1
        return prime, div
    return wrapper
    
@d_check_primality
def results():
    name = input('Inserisci nome ')
    number = int(input('inserisci numero: '))
    
    return name, number

results()