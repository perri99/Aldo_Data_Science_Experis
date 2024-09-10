def somma(*argomenti):
    return sum(argomenti)

def somma2(**argomenti):
    print(argomenti)

def is_even(number):
    if number % 2 == 0: return True
    else: return False

def triplica(number):
    return 3*number


print(somma(1,2,3,4,5,6))
somma2(nome = 'Aldo', età = 25) #crea un dizionario

lista = [1,2,3,4,5,6,7,8]

lista_pari = [n for n in lista if is_even(n)]
print(lista_pari)

lista_pari2 = list(filter(is_even, lista))
print(lista_pari2)

lista_triplicata = [triplica(n) for n in lista]
print(lista_triplicata)

lista_triplicata2 = list(map(triplica, lista))
print(lista_triplicata2)