import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
from xgboost import XGBClassifier  # Importing the XGBoost classifier

# Caricamento dei dati
df_train = pd.read_csv('03-10/loan/train.csv')
loan_status = df_train['loan_status']
df_train.drop(columns=['loan_status', 'id'], inplace=True)

# Dataset di inferenza
df_test = pd.read_csv('03-10/loan/test.csv')
ids = df_test['id']
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
X_train, X_test, y_train, y_test = train_test_split(values, loan_status, test_size=0.2, random_state=42)

# Definizione del modello XGBoost
model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')

# Definizione dello spazio di ricerca degli iperparametri
param_dist = {
    'n_estimators': [150],               # Numero di alberi
    'max_depth': [ 3,  10, 15],                    # Profondità massima
    'learning_rate': [0.01, 0.05, 0.1, 0.2],              # Tasso di apprendimento
    'subsample': [ 0.8],                          # Fractions of samples
    'colsample_bytree': [0.6, 0.8, 1.0],                  # Fractions of features
    'gamma': [0, 0.1, 0.5, 1]                             # Minimum loss reduction required
}

# RandomizedSearchCV con 10 iterazioni
random_search = RandomizedSearchCV(estimator=model, param_distributions=param_dist,
                                   n_iter=10, cv=5, verbose=1, random_state=42, n_jobs=-1)

# Fitting
random_search.fit(X_train, y_train)

# Migliori iperparametri trovati
print(f'Best parameters found: {random_search.best_params_}')

# Predizione e valutazione sul test set
best_model = random_search.best_estimator_
predictions = best_model.predict(X_test)

# Performance Evaluation
performances = classification_report(y_test, predictions)
print('Classification report:')
print(performances)

# Confusion Matrix
matrix = confusion_matrix(y_test, predictions)
print('Confusion Matrix:')
print(matrix)

# Visualizzazione matrice
visual = ConfusionMatrixDisplay(matrix)
visual.plot()
plt.show()

# Preparazione dei risultati per il test set
results = best_model.predict(test_values)
submission = pd.DataFrame({'id': ids,
                           'loan_status': results})
submission.to_csv('submission.csv', index=False)
