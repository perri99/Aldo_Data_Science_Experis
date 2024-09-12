class Studente:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
        self.lista_voti = []
    def aggiungi_voti(self):
        while True:
            voto = input('Inserisci voto o q per uscire: ')
            if voto == 'q':
                break
            self.lista_voti.append(int(voto))
    
    def mostra_studente(self):
        print('Nome: ', self.nome, 'Cognome: ', self.cognome, 'Voti:', self.lista_voti)

class Scuola:
    def __init__(self, nome):
        self.nome = nome
        self.archivio_studenti = {}

    def assegna_ID(self, archivio_studenti):
        ids = list(archivio_studenti.keys())
        if len(ids) == 0:
            id = 0
        else:
            id = max(ids) +1 
        return id

    def aggiungi_studente(self, nome, cognome):
        Studente1 = Studente(nome, cognome)
        Studente1.aggiungi_voti()
        id = self.assegna_ID(self.archivio_studenti)
        self.archivio_studenti[id] = Studente1

    def mostra_archivio(self):
        for Studente1 in self.archivio_studenti.values():
            Studente1.mostra_studente()


Scuola1 = Scuola('Experis')
Scuola1.aggiungi_studente('Aldo', 'Perri')
Scuola1.aggiungi_studente('Mirco', 'Perri')
Scuola1.mostra_archivio()