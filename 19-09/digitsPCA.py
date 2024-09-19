import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

def visualizza_dati(dati):
    df = pd.DataFrame(dati.data, columns=dati.feature_names)
    df['target'] = dati.target
    print(df)
    return df

def pre_processing(dati):
    scaler = StandardScaler()
    return scaler.fit_transform(dati.data)

def principal_components(X, n_components = 2):
    pca = PCA(n_components=n_components)
    X_pca = pca.fit_transform(X)
    return X_pca

def scatter_plot_PCA(X1,X2, target):
    scatter = plt.scatter(X1, X2, c=target )#cmap='tab10', edgecolor='k', s=50
    plt.colorbar(scatter, label='Cifra')
    plt.title('Visualizzazione dei dati con PCA (2 componenti principali)')
    plt.xlabel('Prima componente principale')
    plt.ylabel('Seconda componente principale')
    plt.grid(True)
    plt.show()

def scatter_plot(X1,X2, target):
    scatter = plt.scatter(X1, X2, c=target )#cmap='tab10', edgecolor='k', s=50
    plt.colorbar(scatter, label='Cifra')
    plt.title('Visualizzazione dei dati')
    plt.xlabel('Vero')
    plt.ylabel('predetto')
    plt.grid(True)
    plt.show()

def prediction(model, X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = model
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    scatter_plot(y_test, y_pred, y_test)
    return accuracy

digits = load_digits()
visualizza_dati(digits) # ho 8x8 pixels per 1797 immagini

X = digits.data
#X = pre_processing(digits)
X_pca = principal_components(X)   #riduco con PCA
scatter_plot_PCA(X_pca[:,0],X_pca[:,1], digits.target)

#Logistic regression
original_accuracy = prediction(LogisticRegression(), X, digits.target)
accuracy_PCA = prediction(LogisticRegression(), X_pca, digits.target)
print('Accuratezza modello LogisticRegression sui dati originali:', original_accuracy)
print('Accuratezza modello LogisticRegression sui dati ridotti:', accuracy_PCA)

#SVC
original_accuracy = prediction(SVC(), X, digits.target)
accuracy_PCA = prediction(SVC(), X_pca, digits.target)
print('Accuratezza modello SVC sui dati originali:', original_accuracy)
print('Accuratezza modello SVC sui dati ridotti:', accuracy_PCA)