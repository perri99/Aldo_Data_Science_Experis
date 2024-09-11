#definizione di una Classe
class Automobile:
	numero_di_ruote = 4
	def __init__(self, marca, modello, anno = None):
		self.marca = marca
		self.modello = modello
		if anno is not None: self.anno = anno
        
		
	def stampa_info(self):
		'''
		Metodo della classe
		'''
		if self.anno is not None:
		    print("L'automobile è una", self.marca, self.modello, self.anno)
        else:
            print("L'automobile è una", self.marca, self.modello)
		
Panda = Automobile('Fiat', 'Panda', 2008)
Fiesta = Automobile('Ford', 'Fiesta')
Panda.stampa_info()
Fiesta.stampa_info()
lista_auto = [Panda, Fiesta]
print('Numero di ruote', Panda.numero_di_ruote)
print(lista_auto)