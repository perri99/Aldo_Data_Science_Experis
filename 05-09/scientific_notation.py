print(0.4E-10)
fstringa = f"la mia età è {37+1} anni"
print(fstringa)
#operatore ternario
eta = 20
patente = 'si'
usoDiAlcool = 'si'
#semplifichiamo il seguete if
if eta < 18:
    print('Sei MInorenne')
elif patente != 'si':
    print('Non hai la patente')
elif usoDiAlcool == 'si':
    print('Sei Ubriaco')
else:
    print('Puoi guidare')

#stessa riga
if eta < 18: print('Sei MInorenne') 
elif patente != 'si': print('Non hai la patente')
elif usoDiAlcool == 'si': print('Sei Ubriaco')
else: print('Puoi guidare')

patente = 'si'
guida = '' 
if patente != 'si': guida = 'Non hai la patente'
else: guida = 'Puoi guidare'
#operatore ternario
guida2 = 'non hai la patente' if patente != 'si' else 'Puoi guidare'