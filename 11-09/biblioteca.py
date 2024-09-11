import libro

class Biblioteca:
    archivio_libri = []
    def crea_libro(titolo, autore, pagine):
        Libro = libro.Libro(titolo, autore, pagine)
        return Libro
    
    def aggiungi_libro(self, Libro):
        self.archivio_libri.append(Libro)

    def mostra_archivio(self):
        for Libro in self.archivio_libri:
            Libro.descrivi_libro()


Biblioteca1 = Biblioteca()
Ulisse = Biblioteca.crea_libro('Ulisse', 'Joyce', 4000)
Zeno = Biblioteca.crea_libro('La coscienza di Zeno', 'Svevo', 400)
Biblioteca1.aggiungi_libro(Ulisse)
Biblioteca1.aggiungi_libro(Zeno)
Biblioteca1.mostra_archivio()