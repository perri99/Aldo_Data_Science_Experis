def lettura(file):
    with open(file,'r') as f:
        contenuto = f.read()

    return contenuto

def lettura_righe(file):
    with open(file,'r') as f:
        righe = f.readlines()

    return righe

file = '12-09/testo.txt'
contenuto = lettura(file)
contenuto1 = contenuto.replace('\n', ' ')
contenuto1 = contenuto.replace("'", ' ')
lista_parole = contenuto1.split()
lista_righe = lettura_righe(file)
lista_caratteri = ''.join(lista_parole)

print('Ho contato ', len(lista_parole), 'parole')
print('Ho contato ', len(lista_righe), 'righe')
print('Ho contato', len(contenuto), 'caratteri inclusi gli spazi')
print('Ho contato', len(lista_caratteri), 'caratteri esclusi gli spazi')