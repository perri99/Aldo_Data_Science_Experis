import libro

class Biblioteca:

    archivio_libri = []

    def crea_libro(self, titolo, autore, pagine):
        Libro = libro.Libro(titolo, autore, pagine)
        self.archivio_libri.append(Libro)
        return Libro
    
    def mostra_libro(self, Libro):
        Libro.descrivi_libro()

    def aggiungi_libro(self, Libro):
        self.archivio_libri.append(Libro)

    def mostra_archivio(self):
        for Libro in self.archivio_libri:
            #Libro.descrivi_libro()
            self.mostra_libro(Libro)

Biblioteca1 = Biblioteca()
while True:
    mod = int(input('Cosa vuoi fare? 1.Crea Libro 2.Mostra Archivio 3.Esci'))
    if mod == 1:
        titolo = input('Inserisci titolo: ')
        autore = input('inserisci autore: ')
        pagine = input('Inserisci numero pagine: ')
        Biblioteca1.crea_libro(titolo, autore, pagine)
    elif mod == 2:
        Biblioteca1.mostra_archivio()
    elif mod == 3:
        break
    else:
        print('Scelta non valida')