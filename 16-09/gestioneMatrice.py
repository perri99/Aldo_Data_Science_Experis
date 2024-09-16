import numpy as np

def genera_matrice(dims = (2,2)):
    matrix = np.random.random(dims)
    return matrix

def estrai_matrice_centrale(matrix, dim):
    if matrix.shape[0] % 2 == 0:
        inizio_righe = (matrix.shape[0] - dim) // 2
        inizio_colonne = (matrix.shape[1] - dim) // 2
    else:
        dim +=1
        inizio_righe = (matrix.shape[0]-dim) //2
        inizio_colonne = (matrix.shape[1] - dim) //2
    # Estrai la matrice centrale
    return matrix[inizio_righe:inizio_righe + dim, inizio_colonne:inizio_colonne + dim]

def moltiplica(matrix):
    matrix2 = genera_matrice((matrix.shape[0], matrix.shape[1]))
    print('Seconda matrice')
    print(matrix2)
    return matrix * matrix2

def matrice_da_input():
    righe = int(input('Inserisci numero righe: '))
    colonne = int(input('Inserisci numero colonne: '))
    matrix = genera_matrice((righe, colonne))
    print('Ecco la matrice generata')
    print(matrix)
    return matrix

def trasponi(matrix):
    try:
        transpose = matrix.T
        print(transpose)
    except:
        print('Matrice non creata')

def somma(matrix):
    try:
        print('La somma degli elementi della matrice è ', matrix.sum())
    except: 
        print('Matrice non creata')

def prodotto_puntuale(matrix):
    try:
        prodotto = moltiplica(matrix)
        print('Il risultato è')
        print(prodotto)
    except:
        print('Matrice non generata')

def media(matrix):
    try:
        print('La media degli elementi è', matrix.mean())
    except:
        print('Matrice non generata')


while True:
    choice = input('Scegli cosa fare: 1. Genera nuova Matrice 2.Estrarre la sotto-matrice centrale 3.Trasponi\
    4. Somma elementi 5. Prodotto Puntuale 6. Media 7. Esci')
    if choice == '1':
        matrix = matrice_da_input()
    elif choice == '2':
        print(estrai_matrice_centrale(matrix, 2))
    elif choice == '3':
        trasponi(matrix)
    elif choice == '4':
        somma(matrix)
    elif choice == '5':
        prodotto_puntuale(matrix)
    elif choice == '6':
        media(matrix)
    elif choice == '7':
        break
    else:
        print('Scelta non valida')