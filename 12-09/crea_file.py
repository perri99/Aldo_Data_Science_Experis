import random

# Creare 2 script:
# 1) genera 5 numeri casuali e li salva in un file;
# 2) Se l'utente avrà indovinato 2 numeri avrà vinto, altrimenti potrà arrendersi o ritentare 
# per altri 3 tentativi

def save_file(file):
    random.seed(42)
    numeri_casuali = [str(random.randint(1, 100)) for _ in range(5)]
    stringa = ','.join(numeri_casuali)
    with open(file,'w') as f:
        f.write(stringa)

save_file('file.txt')





