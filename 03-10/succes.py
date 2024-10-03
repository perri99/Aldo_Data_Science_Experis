import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer
from keras.api.regularizers import l2
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization, LeakyReLU
import numpy as np
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
from keras.optimizers import Adam
# Caricamento dei dati
df_train = pd.read_csv('03-10/academysucces/train.csv')

target = df_train['Target']
print(target.value_counts())
df_train.drop(columns=['Target', 'id'], inplace=True)

#dataset di inferenza
df_test = pd.read_csv('03-10/academysucces/test.csv')
ids = df_test['id'].to_numpy()
df_test.drop(columns=[ 'id'], inplace=True)
# Codifica delle colonne categoriche
categorical_columns = df_train.select_dtypes(include=['object']).columns
for col in categorical_columns:
    encoder = LabelEncoder()
    encoder2 = LabelEncoder()
    df_train[col] = encoder.fit_transform(df_train[col])
    df_test[col] = encoder2.fit_transform(df_test[col])
# Normalizzazione delle feature numeriche
scaler = StandardScaler()
values = scaler.fit_transform(df_train)
test_values = scaler.transform(df_test)
lb = LabelBinarizer()
target = lb.fit_transform(target)

# Suddivisione train/test
X_train, X_test, y_train, y_test = train_test_split(values, target, test_size=0.2, random_state=42)
""" early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

model = Sequential()

model.add(Dense(128, input_dim=36, activation='relu'))
#model.add(BatchNormalization())

model.add(Dense(64, activation='relu', kernel_regularizer=l2(0.001)))
#model.add(BatchNormalization())

model.add(Dense(32, activation='relu', kernel_regularizer=l2(0.001)))

# Aggiungiamo un terzo strato nascosto con 16 neuroni e funzione di attivazione ReLU
model.add(Dense(16, activation='relu', kernel_regularizer=l2(0.001)))

model.add(Dense(8, activation='relu', kernel_regularizer=l2(0.001)))

# Strato finale di output, con 1 neurone e funzione di attivazione sigmoid per la classificazione binaria
model.add(Dense(3, activation='softmax'))

# Compilazione del modello, usando binary_crossentropy come loss per classificazione binaria
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Addestramento del modello
model.fit(X_train, y_train, epochs=30, batch_size=32, validation_split=0.2, callbacks = [early_stopping])

test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f'Perdita sul test set: {test_loss:.4f}')
print(f'Accuratezza sul test set: {test_accuracy:.4f}') """
model = Sequential()

# Primo strato
model.add(Dense(256, input_dim=36, kernel_regularizer=l2(0.0001)))
model.add(BatchNormalization())
model.add(LeakyReLU(alpha=0.1))
model.add(Dropout(0.4))

# Secondo strato
model.add(Dense(128, kernel_regularizer=l2(0.0001)))
model.add(BatchNormalization())
model.add(LeakyReLU(alpha=0.1))
model.add(Dropout(0.4))

# Terzo strato
model.add(Dense(64, kernel_regularizer=l2(0.0001)))
model.add(BatchNormalization())
model.add(LeakyReLU(alpha=0.1))
model.add(Dropout(0.4))

# Quarto strato
model.add(Dense(32, kernel_regularizer=l2(0.0001)))
model.add(BatchNormalization())
model.add(LeakyReLU(alpha=0.1))
model.add(Dropout(0.4))

# Strato finale di output
model.add(Dense(3, activation='softmax'))

# Compilazione
optimizer = Adam(learning_rate=0.0001)
model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

# Early stopping e riduzione del learning rate
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=3, min_lr=0.00001)

# Addestramento del modello
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2, callbacks=[early_stopping, reduce_lr])

# Valutazione
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f'Perdita sul test set: {test_loss:.4f}')
print(f'Accuratezza sul test set: {test_accuracy:.4f}')
predictions = np.argmax(model.predict(X_test), axis = 1)
true_classes = np.argmax(y_test, axis = 1)

conf_matrix = confusion_matrix(true_classes, predictions)
print(conf_matrix)

#results = np.argmax(model.predict(test_values))
results = model.predict(test_values)
#results = results.reshape(-1)
results = lb.inverse_transform(results)
results = results.reshape(-1)
submission = pd.DataFrame({'id': ids,
                           'Target':results })
submission.to_csv('submission_keras_academy.csv', index=False)