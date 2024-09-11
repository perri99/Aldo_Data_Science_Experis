class Ristorante:

    def __init__(self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.menu = {0:{'Nome Piatto':'Coperto', 'Prezzo':'2.50 euro'}}
        self.aperto = False

    def descrivi_ristorante(self):
        print('Nome ristorante: ', self.nome, '\nTipologia cucina: ', self.tipo_cucina)

    def stato_apertura(self):
        if self.aperto:
            print('Il ristorante è aperto')
        else:
            print('Il ristorante è chiuso')

    def apri_ristorante(self):
        self.aperto = True
        print('Il ristorante è stato appena aperto!')

    def chiudi_ristorante(self):
        self.aperto = False
        print('Il ristorante ora è stato appena chiuso!')
    
    def assegna_numero_piatto(self, dizionario):
        ids = list(dizionario.keys())
        if len(ids) == 0:
            id = 0
        else:
            id = max(ids) +1 
        return id

    def aggiungi_al_menu(self):
        piatto = {}
        keys = ['Nome Piatto', 'Prezzo']
        numero_piatto = self.assegna_numero_piatto(self.menu)
        for key in keys:
            val = input(f'Inserisci {key} \n')
            piatto[key] = val
        self.menu[numero_piatto] = piatto

    def aggiungi_al_menu_inline(self, nome, prezzo):
        piatto = {}
        numero_piatto = self.assegna_numero_piatto(self.menu)
        piatto['Nome Piatto'] = nome
        piatto['Prezzo'] = str(prezzo)+' euro'
        self.menu[numero_piatto] = piatto

    def mostra_menu(self):
        print('Codice', '    Nome Piatto', '    Prezzo')
        for cod in self.menu:
            print(cod,"      ", self.menu[cod]['Nome Piatto'], '          ', self.menu[cod]['Prezzo'])

    def elimina_piatto(self):
        try:
            self.mostra_menu()
            number = int(input('Inserisci il codice del piatto che vuoi eliminare: '))
        except:
            print('Inserisci un numero')
        if number <= len(self.menu)-1:
            del self.menu[number]
        else:
            print('inserisci numero esistente')

Peng = Ristorante('Cucina di Peng', 'cinese')
Peng.descrivi_ristorante()
Peng.stato_apertura()
Peng.apri_ristorante()
Peng.stato_apertura()
Peng.chiudi_ristorante()
Peng.stato_apertura()
Peng.aggiungi_al_menu_inline('Ravioli', 5)
Peng.aggiungi_al_menu_inline('Involtini', 2)
Peng.aggiungi_al_menu()
Peng.mostra_menu()
Peng.elimina_piatto()
Peng.mostra_menu()