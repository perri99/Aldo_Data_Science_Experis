class Libro:
    def __init__(self, titolo, autore, pagine):
        '''
        Costruttore della classe
        '''
        try:
            if type(titolo == str) and type(autore == str):
                self.titolo = titolo
                self.autore = autore
        except:
            print('Titolo e autore devono essere stringhe')
        try:
                
            self.pagine = int(pagine)
        except:
            print('Pagine deve essere un intero')
             
    
    def descrivi_libro(self):
        '''
        Stampa
        '''
        try:
            print('Il titolo del libro è', self.titolo, 'scritto da', self.autore, 'e ha', self.pagine, 'pagine')
        except:
            print("Errore nella costruzione dell'oggetto")
        

Ulisse = Libro('Ulisse', 'James Joyce', 'n')
Zeno = Libro('La Coscienza di Zeno', 3, 400)
Ulisse.descrivi_libro()
Zeno.descrivi_libro()