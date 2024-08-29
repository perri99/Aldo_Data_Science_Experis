num1 = float(input('inserisci il primo numero\n'))
num2 = float(input('inserisci il secondo numero\n'))

operation = input('Scegli operazione: Addizione: +\n Sottrazione: -\n Moltiplicazione:* \n Divisione: /\n')

if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1*num2)
elif operation == '/':
    if num2 == 0:
        print('Impossibile dividere per zero!')
    else:
        print(num1 / num2)
else:
    print('Operazione non disponibile')

