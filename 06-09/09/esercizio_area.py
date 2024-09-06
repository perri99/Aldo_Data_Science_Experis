def area_triangolo(base, altezza):
    return 0.5 * base * altezza

def area_quadrato(lato):
    return lato ** 2

def area_rettangolo(base, altezza):
    return base * altezza

def base_altezza():
    base = int(input('Inserisci base: '))
    altezza = int(input('Inserisci altezza: '))
    return base, altezza

def inserisci_lato():
    lato = int(input('Inserisci lato: '))
    return lato

def quadrato():
    lato = inserisci_lato()
    area = area_quadrato(lato)
    return area

def triangolo():
    base, altezza = base_altezza()
    area = area_triangolo(base, altezza)
    return area

def rettangolo():
    base, altezza = base_altezza()
    area = area_rettangolo(base, altezza)

area_lists = []
while True:
    
    figure_type = input('Scegli la figura geometrica:\n 1.Triangolo 2.Quadrato 3.Rettangolo 4. Uscire ')
    if figure_type == '1':
        area = triangolo()
    elif figure_type == '2':
        area = quadrato()
    elif figure_type == '3':
        area = rettangolo()
    elif figure_type == '4':
        break
    else:
        print('Scelta Non Valida')
        continue
    print("L'area calcolata è", area)
    area_lists.append(area)
print(area_lists)