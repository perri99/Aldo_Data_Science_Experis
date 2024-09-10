
'''
if number.isdecimal():
    number = int(number)
else:
    print('Non è un numero')'''
try:
    number = int(input('Inserisci un numero '))
except ValueError as ve:
    print('Non valido errore', ve)

print('Il programma non si blocca')