import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.utils import to_categorical
from sklearn.metrics import classification_report

def view_images(X_train, y_train):
        for index in range(5):
            plt.imshow(X_train[index], cmap='gray')
            plt.colorbar()
            plt.title(f"Immagine generata dalla matrice di grigi label {y_train[index]}")
            plt.show()

def preprocessing(X_train, y_train, X_test, y_test):
    # Normalizzazione dei pixel
    X_train = X_train.astype('float32') / 255
    X_test = X_test.astype('float32') / 255

    # Conversione delle etichette in one-hot encoding
    y_train = to_categorical(y_train, num_classes=10)
    y_test = to_categorical(y_test, num_classes=10)

    return X_train, y_train, X_test, y_test

def sequential_model():
    model = Sequential()
    model.add(Flatten(input_shape=(28, 28)))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(10, activation='softmax'))
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    model.summary()
    return model

def train_model(model, X_train, y_train, n_epochs=5, b_size=32):
    fitted_model = model.fit(X_train, y_train,
                             epochs=n_epochs,
                             batch_size=b_size,
                             validation_split=0.1)
    return fitted_model

def plot_accuracy(trained_model):
    plt.plot(trained_model.history['accuracy'],
    label='Accuratezza Training')
    plt.plot(trained_model.history['val_accuracy'],
    label='Accuratezza Validazione')
    plt.xlabel('Epoca')
    plt.ylabel('Accuratezza')
    plt.legend()
    plt.title('Andamento dell\'Accuratezza')
    plt.show()

def plot_loss(trained_model):
    plt.plot(trained_model.history['loss'],
    label='Loss Training')
    plt.plot(trained_model.history['val_loss'],
    label='Loss Validazione')
    plt.xlabel('Epoca')
    plt.ylabel('Loss')
    plt.legend()
    plt.title('Andamento della perdita')
    plt.show()
# Caricamento del dataset MNIST
(X_train, y_train), (X_test, y_test) = mnist.load_data()
view_images(X_train, y_train)
# Preprocessing dei dati
X_train, y_train, X_test, y_test = preprocessing(X_train, y_train, X_test, y_test)


# Creazione del modello sequenziale
my_model = sequential_model()

# Addestramento del modello
trained_model = train_model(my_model, X_train, y_train, n_epochs= 10)

# Valutazione del modello sul set di test
test_loss, test_acc = my_model.evaluate(X_test, y_test)
print('\nAccuratezza sul set di test:', test_acc)

# Fare predizioni sul set di test
predictions = my_model.predict(X_test)

# Conversione delle predizioni in etichette
predicted_classes = np.argmax(predictions, axis=1)
true_classes = np.argmax(y_test, axis=1)

print(classification_report(true_classes, predicted_classes))

plot_accuracy(trained_model)
plot_loss(trained_model)

