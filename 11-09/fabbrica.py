class Elettronica:
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        self.garanzia = garanzia

    def restituisci_nome(self):
        return self.nome

    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione
    
class Abbigliamento:
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale, colore):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        self.materiale = materiale
        self.colore = colore

    def restituisci_nome(self):
        return self.nome
    
    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione   
    
class Giocattolo:
    def __init__(self, nome, costo_produzione, prezzo_vendita, eta_minima):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        self.eta_minima = eta_minima

    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione
    
class Fabbrica:
    
    def __init__(self, nome):
        self.nome = nome
        self.inventario = {}

    def assegna_ID(self):
        ids = list(self.inventario.keys())
        if len(ids) == 0:
            id = 0
        else:
            id = max(ids) +1 
        return id

    def aggiungi_prodotto(self, Prodotto, numero):
        
        if Prodotto.restituisci_nome() not in [self.inventario[code]['Prodotto'] for code in range(len(self.inventario)) ]:
            item = {}
            codice_prodotto = self.assegna_ID()
            item['Prodotto'] = Prodotto.restituisci_nome()
            item['Numero'] = numero
            self.inventario[codice_prodotto] = item
        else:
            print('Prodotto già esistente, aggiorno il numero di elementi')
            self.aumenta_prodotto(Prodotto, numero)
            
            

    def vendi_prodotto(self, Prodotto, quantità):
        check_vendita = False
        for cod in self.inventario:
            if self.inventario[cod]['Prodotto'] == Prodotto.restituisci_nome():
                check_vendita = True
                self.inventario[cod]['Numero'] -= quantità
                if quantità > 0:
                    print('Vendita di', quantità,Prodotto.restituisci_nome(),'Gaudagno:', Prodotto.calcola_profitto()*quantità)
        if check_vendita == False:
            print(f'Prodotto non trovato: vendita di {Prodotto.restituisci_nome()} impossibile')

    def aumenta_prodotto(self, Prodotto, quantità): 
        self.vendi_prodotto(Prodotto, -quantità)
        print('Aggiunti', quantità, Prodotto.restituisci_nome())   

    def mostra_inventario(self):
        print(self.inventario)


Laptop = Elettronica('Laptop', 200, 400, '2 anni')
Maglietta_nera = Abbigliamento('Maglietta Nera', 10, 70, 'Lino', 'Nera')
Maglietta_bianca = Abbigliamento('Maglietta Bianca', 10, 70, 'Lino', 'Bianca')
Aldo_SRL = Fabbrica('Aldo SRL')
Aldo_SRL.aggiungi_prodotto(Laptop, 43)
Aldo_SRL.aggiungi_prodotto(Maglietta_nera, 24)
Aldo_SRL.aggiungi_prodotto(Maglietta_nera, 2)
Aldo_SRL.mostra_inventario()
Aldo_SRL.vendi_prodotto(Maglietta_nera, 10)
Aldo_SRL.vendi_prodotto(Laptop, 40)
Aldo_SRL.vendi_prodotto(Maglietta_bianca, 50)
Aldo_SRL.mostra_inventario()
Aldo_SRL.aumenta_prodotto(Laptop, 4)
Aldo_SRL.mostra_inventario()