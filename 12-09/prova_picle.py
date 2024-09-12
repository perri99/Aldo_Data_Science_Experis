import pickle as pk

dizionario = {0:'Aldo', 1:'Perri'}

dizionario_binario = pk.dumps(dizionario)

with open('12-09/dizionario.bin', 'wb') as f:
    f.write(dizionario_binario)

with open('12-09/dizionario.bin', 'rb') as f:
    contenuto = f.read()

print(pk.loads(contenuto))