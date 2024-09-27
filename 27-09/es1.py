import pandas as pd 

class Libro:
    def __init__(self, autore, titolo, anno):
       self.titolo = titolo
       self.autore = autore
       self.anno = anno
    
    def get_titolo(self):
        return self.titolo
    
    def get_autore(self):
        return self.autore
    
    def get_anno(self):
        return self.anno
    


class Libreria:

    def __init__(self):
        self.archivio_libri = {'Autore':[],
                                            'Titolo': [],
                                            'Anno':[],
                                            'Qauntità':[]}


    def aggiungi_libro(self, Libro, quantità):
        self.archivio_libri['Autore'].append(Libro.get_autore())
        self.archivio_libri['Titolo'].append(Libro.get_titolo())
        self.archivio_libri['Anno'].append(Libro.get_anno())
        self.archivio_libri['Quantità'].append(quantità)
        return Libro
    
    def mostra_libro(self, Libro):
        Libro.descrivi_libro()

    def aggiungi_libro(self, Libro):
        self.archivio_libri.append(Libro)

    def mostra_archivio(self):
        print(self.archivio_libri)


Ulisse = Libro('Joyce', 'Ulisse', '1960')
print(Ulisse)
Lib = Libreria()
Lib.aggiungi_libro(Ulisse, 7)
Lib.aggiungi_libro(Ulisse, 7)
Lib.mostra_archivio()