import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Caricamento dei dati
df_train = pd.read_csv('03-10/academysucces/train.csv')

# Codifica delle classi target
encoder_target = LabelEncoder()
target = encoder_target.fit_transform(df_train['Target'])  # Con LabelEncoder

print(pd.Series(target).value_counts())
df_train.drop(columns=['Target', 'id'], inplace=True)

# dataset di inferenza
df_test = pd.read_csv('03-10/academysucces/test.csv')
ids = df_test['id'].to_numpy()
df_test.drop(columns=['id'], inplace=True)

# Codifica delle colonne categoriche
categorical_columns = df_train.select_dtypes(include=['object']).columns
for col in categorical_columns:
    encoder = LabelEncoder()
    df_train[col] = encoder.fit_transform(df_train[col])
    df_test[col] = encoder.transform(df_test[col])

# Normalizzazione delle feature numeriche
scaler = StandardScaler()
values = scaler.fit_transform(df_train)
test_values = scaler.transform(df_test)

# Suddivisione train/test
X_train, X_test, y_train, y_test = train_test_split(values, target, test_size=0.2, random_state=42)

# Modello Random Forest
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)  # Il target è già codificato come etichette intere

# Valutazione
predictions = model.predict(X_test)
print(classification_report(y_test, predictions))

# Matrice di confusione
conf_matrix = confusion_matrix(y_test, predictions)
print(conf_matrix)

# Visualizzazione della matrice di confusione
ConfusionMatrixDisplay(conf_matrix).plot()

# Predizioni sul dataset di test
results = model.predict(test_values)

# Decodifica delle predizioni usando le classi originali
results = encoder_target.inverse_transform(results)

# Creazione del file di submission
submission = pd.DataFrame({'id': ids, 'Target': results})
submission.to_csv('submission_random_forest_encoder.csv', index=False)
