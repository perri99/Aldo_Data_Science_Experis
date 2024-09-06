'''
Riassunto delle conoscenze
'''

def menu():
    modality = input('Benvenuto!!. Scegli cosa vuoi ripassare:\n 1. UML 2. Programmazione agli oggetti 3. Metodologie  4. Cicli 5. Liste  6. Uscire')
    return modality

def uml():
    print("L'UML è un linguaggio visuale standardizzato per la descrizione della struttura di un software, basato su\
          stereotipi comuni che possono essere modificati, risultando flessibile e adattabile")

def programmazione_a_oggetti():
    print("Le tre regole fondamentali della programmazione orientata agli oggetti sono: 1. Incapsulamento: permette al software di nascondere parti di codice che non si vogliono rendere pubbliche,è la proprietà meno in mano al programmatore; 2. Ereditarietà: permette la creazione di classi 'figlie' ereditando le caratteristiche delle classi 'madri',\
                questo permette il riutilizzo di codice e la creazione di gerarchie tra classi, \
                altamente controllabile dal programmatore");\
    print("3. Polimorfismo: è la proprietà che permette agli oggetti di cambiare forma ma non comportamento oppure\
                 di cambiare comportamento ma non forma \
               La presenza di queste 3 regole è garantita dall'ASTRAZIONE, anche detta REGOLA MADRE, che ci permette di \
                 descrivere le proprietà di un oggetto, andando ad esternare le sue caratteristiche e comportamenti principali")

def metodologie():
    print('Agile e Waterfall')

def cicli():
    choice = input('Scegli: 1. WHILE 2. FOR')
    if choice == '1':
        counter = 1
        while True:
            print('siamo in un ciclo While: iterazione numero', counter)
            exit = input('Premi q per uscire dal ciclo, altri tasti se vuoi rimanere nel while')
            if exit == 'q':
                break
            counter +=1
    elif choice == '2':
        print('Il for si usa per un numero finito di cicli')
        N = int(input('Inserisci un numero: '))
        for i in range(N):
            print(i)
        print('Con un ciclo FOR ho stampato questi numeri')

def liste():
    print('Le liste sono un dato aggregato. Ecco un esempio di lista')
    lista = [*range(10)]
    print(lista)

while True:
    choice = menu()
    if choice == '1':
        uml()
    elif choice == '2':
        programmazione_a_oggetti()
    elif choice == '3':
        metodologie()
    elif choice == '4':
        cicli()
    elif choice == '5':
        liste()
    elif choice == '6':
        break