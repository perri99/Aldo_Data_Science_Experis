import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
import torchvision.transforms as transforms
import torch.optim as optim
from tqdm import tqdm
class CNN(nn.Module):
    def __init__(self):
        # Inizializziamo la classe base nn.Module
        super(CNN, self).__init__()

        # Primo strato convoluzionale: prende in input 1 canale (immagine in scala di grigi), 
        # genera 28 canali (filtri), kernel di dimensione 3x3 e padding=1 per mantenere la dimensione dell'immagine
        self.conv1 = nn.Conv2d(1, 32, 3, padding=1)
        
        # Secondo strato convoluzionale: prende 28 canali in input e genera 64 canali, 
        # kernel di dimensione 3x3 e padding=1 per mantenere la dimensione
        self.conv2 = nn.Conv2d(32, 64, 3, padding=1)

        # Strato di pooling (max pooling): riduce la dimensione dell'immagine di un fattore 2x2
        self.pool = nn.MaxPool2d(2, 2)

        # Primo strato completamente connesso (fully connected): input = 64 canali di feature map di dimensione 7x7,
        # output = 512 neuroni. Viene utilizzato dopo la convoluzione e il pooling
        self.fc1 = nn.Linear(64 * 7 * 7, 512)

        # Secondo strato completamente connesso (fully connected): input = 512 neuroni, output = 10 neuroni 
        # (corrispondenti alle 10 classi del FashionMNIST)
        self.fc2 = nn.Linear(512, 10)

    def forward(self, x):
        # Applicazione della prima convoluzione, seguita da funzione di attivazione ReLU e pooling
        x = self.pool(F.relu(self.conv1(x)))
        
        # Applicazione della seconda convoluzione, seguita da funzione di attivazione ReLU e pooling
        x = self.pool(F.relu(self.conv2(x)))

        # "Appiattimento" del tensore: converte la feature map 2D in un vettore 1D
        x = x.view(-1, 64 * 7 * 7)

        # Applicazione del primo strato fully connected con funzione di attivazione ReLU
        x = F.relu(self.fc1(x))

        # Applicazione del secondo strato fully connected, che genera le previsioni finali (logits) per le 10 classi
        x = self.fc2(x)
        
        # Restituisce l'output finale (senza softmax poiché il calcolo della loss la richiede separatamente)
        return x

# Definiamo le trasformazioni da applicare al dataset (normalizzare le immagini e convertirle in tensori)
transform = transforms.Compose(
    [
        # Convertiamo le immagini in tensori (vettori multidimensionali) con valori normalizzati tra 0 e 1
        transforms.ToTensor(), 
        
        # Normalizziamo le immagini per avere valori medi centrati a 0.5 con deviazione standard 0.5
        transforms.Normalize((0.5,), (0.5,)) 
    ])

# Scarica e carica il dataset FashionMNIST per il training
trainset = torchvision.datasets.FashionMNIST(root='./data', download=False, train=True, transform=transform)
testset = torchvision.datasets.FashionMNIST(root='./data', download=False, train=False, transform=transform)

trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)
testloader = torch.utils.data.DataLoader(testset, batch_size=64, shuffle=False)

# Le classi del dataset FashionMNIST
classes = ('T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
           'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot')


# Creiamo un'istanza del modello CNN precedentemente definito
# 'model' è ora la nostra rete convoluzionale che utilizzeremo per l'addestramento e la predizione
model = CNN()

# Definiamo la funzione di perdita (loss function) per il compito di classificazione.
# Utilizziamo 'CrossEntropyLoss', che è comunemente usata nei problemi di classificazione multi-classe.
# Questa funzione calcola la differenza tra le previsioni del modello (logits) e le etichette reali (classi corrette).
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Addestramento del modello CNN
# 'epoch' indica una passata completa sul dataset di addestramento
# In questo ciclo, eseguiamo l'addestramento per 10 epoche (iterazioni sull'intero dataset)
for epoch in tqdm(range(2)):  # ciclo sul dataset più volte
    running_loss = 0.0  # Variabile per tracciare la perdita media durante l'epoca

    # Enumeriamo i dati presenti nel 'trainloader', che contiene i batch di immagini e le rispettive etichette
    # 'i' è l'indice del batch, 'data' è una lista che contiene gli input (immagini) e le etichette (classi corrette)
    for i, data in enumerate(trainloader, 0):
        # Otteniamo gli input e le etichette dal batch corrente. 'data' è una lista [inputs, labels]
        inputs, labels = data

        # Azzeriamo i gradienti dei parametri del modello (pesi e bias)
        # Questo è necessario perché PyTorch accumula i gradienti ad ogni iterazione,
        # quindi dobbiamo resettarli prima di ogni passo di ottimizzazione.
        optimizer.zero_grad()

        # **Forward pass**: Passiamo gli input attraverso il modello per ottenere le previsioni (output)
        outputs = model(inputs)

        # Calcoliamo la perdita (loss) confrontando le previsioni del modello (outputs) con le etichette reali (labels)
        # La funzione di perdita 'criterion' (CrossEntropyLoss) misura quanto le previsioni sono lontane dalle etichette corrette.
        loss = criterion(outputs, labels)

        # **Backward pass**: Calcoliamo i gradienti della perdita rispetto ai parametri del modello
        # Questo passaggio calcola il gradiente per ciascun parametro in base all'errore commesso.
        loss.backward()

        # **Ottimizzazione**: Aggiorniamo i pesi del modello utilizzando l'ottimizzatore Adam,
        # che utilizza i gradienti calcolati nel backward pass per modificare i parametri e ridurre la perdita.
        optimizer.step()

        # Tracciamo la perdita accumulata per ogni batch per poter monitorare l'addestramento
        running_loss += loss.item()

        # Ogni 100 batch, stampiamo le statistiche (ad esempio, la perdita media per gli ultimi 100 batch)
        if i % 100 == 99:    # Stampiamo ogni 100 batch
            # La perdita media per ogni 100 batch viene stampata su schermo per monitorare il progresso
            print(f'Epoch {epoch + 1}, Batch {i + 1}: Loss {running_loss / 100:.3f}')
            running_loss = 0.0  # Reset della variabile running_loss per il prossimo gruppo di batch

# Dopo aver completato tutte le epoche, l'addestramento è finito
print('Training completed.')

# Inizializziamo le variabili per tenere traccia del numero totale di predizioni corrette e del numero totale di immagini
correct = 0  # Numero di predizioni corrette
total = 0    # Numero totale di immagini testate

# Disabilitiamo il calcolo del gradiente durante il testing.
# Questo è importante perché durante il testing non aggiorniamo i pesi, quindi non è necessario calcolare i gradienti,
# risparmiando memoria e velocizzando il processo.
with torch.no_grad():
    # Iteriamo attraverso i batch del test loader (testloader), che contiene i dati di test
    for data in testloader:
        # Estraiamo le immagini e le etichette reali (labels) dal batch corrente
        images, labels = data

        # Passiamo le immagini attraverso il modello per ottenere le previsioni
        outputs = model(images)

        # Otteniamo le predizioni dal modello.
        # torch.max(outputs, 1) restituisce il valore massimo e l'indice della classe con il valore più alto
        # lungo la dimensione 1 (le classi). Non ci interessa il valore massimo in sé, ma solo l'indice (classe predetta).
        _, predicted = torch.max(outputs, 1)

        # Aggiorniamo il conteggio del totale delle immagini testate
        total += labels.size(0)  # labels.size(0) restituisce il numero di immagini nel batch (batch size)

        # Sommiamo il numero di predizioni corrette.
        # (predicted == labels) restituisce un tensore booleano con True per ogni predizione corretta,
        # sommiamo quindi tutti i True (che valgono 1) usando .sum().item() per ottenere il numero totale di corrette.
        correct += (predicted == labels).sum().item()

# Calcoliamo e stampiamo l'accuratezza del modello sulle immagini di test.
# L'accuratezza è la percentuale di predizioni corrette rispetto al totale delle immagini testate.
# Viene moltiplicata per 100 per ottenere la percentuale.
print(f'Accuracy of the network on the test images: {100 * correct / total:.2f}%')

# Save the trained model
torch.save(model.state_dict(), '03-10/cnn_fashionMNIST.pth')

