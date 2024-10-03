import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
# Caricamento dei dati
df_train = pd.read_csv('03-10/loan/train.csv')
loan_status = df_train['loan_status']
df_train.drop(columns=['loan_status', 'id'], inplace=True)
#dataset di inferenza
df_test = pd.read_csv('03-10/loan/test.csv')
ids = df_test['id']
df_test.drop(columns=[ 'id'], inplace=True)
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
X_train, X_test, y_train, y_test = train_test_split(values, loan_status, test_size=0.2, random_state=42)

# Definizione del modello RandomForestClassifier
# model = RandomForestClassifier(n_estimators=250,
                            #    min_samples_split=10,
                            #    min_samples_leaf=2,
                            #    bootstrap=False)
model = RandomForestClassifier()
# Definizione dello spazio di ricerca degli iperparametri
param_dist = {
    'criterion': ['gini', 'entropy', 'log_loss'],
    'n_estimators': np.arange(50, 500, 50),            # Numero di alberi nella foresta
    'max_depth': [None, 10, 20, 30, 40, 50],           # Profondità massima di ogni albero
    'min_samples_split': [2, 5, 10],                   # Numero minimo di campioni per suddividere un nodo
    'min_samples_leaf': [1, 2, 4],                     # Numero minimo di campioni in un nodo foglia
    'bootstrap': [True, False]                         # Utilizzo del bootstrapping
}

# RandomizedSearchCV con 10 iterazioni
random_search = RandomizedSearchCV(estimator=model, param_distributions=param_dist,
                                   n_iter=10, cv=5, verbose=1, random_state=42, n_jobs=-1)

#Fitting
random_search.fit(X_train, y_train)

# Migliori iperparametri trovati
print(f'Best parameters found: {random_search.best_params_}')

# Predizione e valutazione sul test set
model = random_search.best_estimator_
model.fit(X_train, y_train)
predictions = model.predict(X_test)
performances = classification_report(y_test, predictions)

print('Classification report:')
print(performances)
matrix = confusion_matrix(y_test, predictions)
print('Confusion Matrix')
print(matrix)
#visualizzazione matrice
visual = ConfusionMatrixDisplay(matrix)
visual.plot()
plt.show()

results = model.predict(test_values)
submission = pd.DataFrame({'id': ids,
                           'loan_status':results })
submission.to_csv('submission.csv', index=False)