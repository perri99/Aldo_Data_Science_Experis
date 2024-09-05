lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(lista[2:5]) #stampa da posizione 2 a 4

for number in lista[3:6]:
    print(number)

count = 1
while count < 11:
    print(3*count)
    count += 1 

for index in [1,2,3,4,5,6,7,8,9,10]:
    print(index*3)

for index in range(1,11):
    print(index*3)

lista = list(range(1,11, 2))
print(lista[::-1])
lista.append(19)
lista.insert(2, 17)
print(lista)
lista1 = [76, 54]
lista.extend(lista1)
lista.sort(reverse = True)
print(lista)
print(lista.index(17))