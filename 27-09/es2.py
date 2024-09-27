from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
import pandas as pd
import matplotlib.pyplot as plt

def esplora_dati(func):
    '''
    Esplora dati e etichette e le restituisce
    '''
    X = func.data
    y = func.target

    df = pd.DataFrame(X, columns=func.feature_names)
    df['target'] = y

    #df_data = pd.DataFrame(X)
    print('Dati:')
    print(df)
    print('Etichette: ')
    print(y)
    return X, y, func.target_names

def splitting_data(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)
    return X_train, X_test, y_train, y_test

def train_model(model, X_test, y_test):
    model.fit(X_test, y_test)
    return model

def predictions(model, X_train):
    return model.predict(X_train)

def evaluation(prediction, true_val):
    performances = classification_report(true_val, prediction)
    print('Classification report:')
    print(performances)

def visualizza_matrice(y_test, y_pred, targets):
    #Matrice di confusione
    matrix = confusion_matrix(y_test, y_pred)
    print('Confusion Matrix')
    print(matrix)
    #visualizzazione matrice
    visual = ConfusionMatrixDisplay(matrix, display_labels=targets)
    visual.plot()
    plt.show()

X, y, targets = esplora_dati(load_iris())

X_train, X_test, y_train, y_test = splitting_data(X, y)
model = KNeighborsClassifier()
trained_model = train_model(model, X_test, y_test)
predict = predictions(trained_model, X_test)
evaluation(predict, y_test)
visualizza_matrice(y_test, predict, targets)