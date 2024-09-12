import crea_file

# Creare 2 script:
# 1) genera 5 numeri casuali e li salva in un file;
# 2) Se l'utente avrà indovinato 2 numeri avrà vinto, altrimenti potrà arrendersi o ritentare 
# per altri 3 tentativi

def lettura(file):
    with open(file,'r') as f:
        contenuto = f.read().split(',')

    return contenuto

def main():
    count = 0
    tentativo = 0
    l = lettura('file.txt')
    while count < 2:
        x = input("Indovina un numero oppure digita q per arrenderti: ")
        if x == 'q':
            break
        if x in l:
            count+=1
            tentativo += 1
            print("Hai indovinato un numero")
        else:
            tentativo += 1
            print("Numero errato")
        if tentativo == 3:
            print("Hai perso")
            break
    
    else:
        print("Hai vinto")
        

main()

