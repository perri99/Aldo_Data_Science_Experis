numbers_list = []
sum = 0
numbers_of_input = 10 

for index in range(numbers_of_input):
    number = int(input('Inserisci un numero: '))
    numbers_list.append(number)
    sum += number

numbers_list.sort()
print('Il minimo inserito è', numbers_list[0], 'Il massimo inserito è', numbers_list[numbers_of_input-1])
print('Il numero in mezzo è', numbers_list[int(numbers_of_input/2) - 1])
print('La media dei numeri inseriti è', sum/numbers_of_input)