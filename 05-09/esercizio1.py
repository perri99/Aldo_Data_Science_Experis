'''
Scrivete un programma che chiede all'utente una
frase e restituisce solo le vocali e l indice della
vocale all interno della frase.
'''
vocali = ['a', 'e', 'i', 'o', 'u']

vocali_nella_frase = []
frase = input('Inserisci un frase: \n')

index = 0
for element in frase:
    if element in vocali:
        print('Vocale', element, ' in posizione', index)
        vocali_nella_frase.append(element)
        index += 1

print('Lista di vocali nella frase')
print(vocali_nella_frase)