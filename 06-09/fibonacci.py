'''
Fibonacci
'''
def fibonacci_number(number): #https://www.valcon.it/python/numeri-di-fibonacci/ leggera modifica
    if number == 0:
        return 0
    elif number <=2:
        return 1
    else:
        return fibonacci_number(number-1) + fibonacci_number(number-2)

def find_fibonacci(number):
    fibonacci_numbers = []
    for index in range(number+1):
        fibonacci = fibonacci_number(index)
        if fibonacci <= number:
            fibonacci_numbers.append(fibonacci_number(index))
    return fibonacci_numbers

input_number = int(input('Inserisce un numero: '))
print('Ecco i numeri di Fibonacci minori di', input_number)
print(find_fibonacci(input_number))
