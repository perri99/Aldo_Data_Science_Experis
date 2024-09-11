'''
Scrivete un programma che prenda i nomi degli alunni di una
classe e i loro voti, quando l’utente scrive media il programma
andrà a stampare i nomi di tutti gli alunni e per ogni alunno la
media dei voti.
Esempio:
Nome: Giovanni , Media: 7.5
Nome: Alfredo , Media: 9
Nome: Michela, Media 10
'''
def assegna_ID(archivio_studenti):
    ids = list(archivio_studenti.keys())
    if len(ids) == 0:
        id = 0
    else:
        id = max(ids) +1 
    return id

def inserisci_studente(archivio_studenti, materie):
    studente = {}

    id = assegna_ID(archivio_studenti)

    nome = input('Inserisci nome: ')
    studente['Nome'] = nome

    for materia in materie:
        voto = int(input(f'Inserisci voto {materia}: '))
        studente[materia] = voto
    archivio_studenti[id] = studente

def calcolo_media(dizionario, materie):
    
    for element in dizionario:
        votes = [dizionario[element][key] for key in materie]
        media = sum(votes) / len(votes)
        print(f"{dizionario[element]['Nome']} media = {media}")

studenti = {}
materie = ['Storia', 'Matematica', 'Italiano', 'Latino', 'Geografia', 'Fisica']

while True:
    mod = input('Scegli cosa fare: 1.Inserire Studente, 2. Visualizzare Archivio, 3. Calcolo Media, 4.Uscire\n')
    if mod == '1':
        inserisci_studente(studenti, materie)
    elif mod == '2':
        print(studenti)
    elif mod == '3':
        calcolo_media(studenti, materie)
    elif mod == '4':
        break
    else:
        print('Scelta non valida')