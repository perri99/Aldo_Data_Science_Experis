import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.metrics import classification_report,  confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
from tensorflow.keras.layers import BatchNormalization, Dropout
from tensorflow.keras.regularizers import l2
from tensorflow.keras.callbacks import EarlyStopping



# Caricamento dei dati
df_train = pd.read_csv('03-10/loan/train.csv')
loan_status = df_train['loan_status']
df_train.drop(columns=['loan_status', 'id'], inplace=True)

#dataset di inferenza
df_test = pd.read_csv('03-10/loan/test.csv')
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

# Suddivisione train/test
X_train, X_test, y_train, y_test = train_test_split(values, loan_status, test_size=0.2, random_state=42)

early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

# Definizione della rete neurale
model = Sequential()

# Aggiungiamo un primo strato denso con 64 neuroni e una funzione di attivazione ReLU

model.add(Dense(128, input_dim=11, activation='relu'))
#model.add(BatchNormalization())

model.add(Dense(64, activation='relu', kernel_regularizer=l2(0.001)))
#model.add(BatchNormalization())

model.add(Dense(32, activation='relu', kernel_regularizer=l2(0.001)))

# Aggiungiamo un terzo strato nascosto con 16 neuroni e funzione di attivazione ReLU
model.add(Dense(16, activation='relu', kernel_regularizer=l2(0.001)))

model.add(Dense(8, activation='relu', kernel_regularizer=l2(0.001)))

# Strato finale di output, con 1 neurone e funzione di attivazione sigmoid per la classificazione binaria
model.add(Dense(1, activation='sigmoid'))

# Compilazione del modello, usando binary_crossentropy come loss per classificazione binaria
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Addestramento del modello
model.fit(X_train, y_train, epochs=40, batch_size=32, validation_split=0.2,  callbacks=[early_stopping])

# Predizione sul test set
predictions = (model.predict(X_test) > 0.5).astype(int)

# Valutazione delle performance
print(classification_report(y_test, predictions))

matrix = confusion_matrix(y_test, predictions)
print('Confusion Matrix')
print(matrix)
#visualizzazione matrice
visual = ConfusionMatrixDisplay(matrix)
visual.plot()
plt.show()

results = (model.predict(test_values) > 0.5).astype(int)
results = results.reshape(-1)
submission = pd.DataFrame({'id': ids,
                           'loan_status':results })
submission.to_csv('submission_keras.csv', index=False)