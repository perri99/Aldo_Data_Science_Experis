from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class PredictorDTC:

    def __init__(self, data_function):
        self.data = data_function
        self.X = self.data.data
        self.y = self.data.target
        self.model = DecisionTreeClassifier()

    def scaling_data(self):
        scaler = StandardScaler()
        self.X_scaled = scaler.fit_transform(self.X)
        return self.X_scaled

    def split_data(self):
        self.scaling_data()
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X_scaled, self.y, test_size = 0.3, random_state = 42)

    def train_DTC(self):
        #scelta del modello
        self.split_data()
        #Addestramento
        self.model.fit(self.X_train, self.y_train)
        #return model

    def prediction(self):
        self.y_pred = self.model.predict(self.X_test)
        return self.y_pred

    def performances(self):
        performances = classification_report(self.y_test, self.y_pred, target_names = self.data.target_names)
        print('Classification report:')
        print(performances)

    def confusion_matrix(self):
        #Matrice di confusione
        matrix = confusion_matrix(self.y_test, self.y_pred)
        print('Confusion Matrix')
        print(matrix)
        #visualizzazione matrice
        visual = ConfusionMatrixDisplay(matrix, display_labels=self.data.target_names)
        visual.plot()
        plt.show()

    def plot_feature_importance(self):
        # Importanza delle feature
        importances = self.model.feature_importances_
        indices = np.argsort(importances)[-5::]
        names = [self.data.feature_names[i] for i in indices]
        plt.title("Feature Importance")
        plt.bar(names, importances[indices])
        plt.show()

    def plot_classification_report(self):
        # Otteniamo i risultati dal classification report
        report = classification_report(self.y_test, self.y_pred, output_dict=True)
        df = pd.DataFrame(report).transpose()

        # Selezioniamo precision, recall e f1-score
        metrics = df[['precision', 'recall', 'f1-score']].iloc[:-3]  # Escludiamo "accuracy", "macro avg", "weighted avg"

        # Creiamo il grafico
        metrics.plot(kind='bar')
        plt.title("Precision, Recall, and F1-Score per Class")
        plt.ylabel("Score")
        plt.xlabel("Class")
        plt.xticks(rotation=0)
        plt.ylim(0, 1)  # Per mantenere la scala tra 0 e 1
        plt.legend(loc="lower right")
        plt.show()


my_model = PredictorDTC(load_wine())
my_model.train_DTC()
pred = my_model.prediction()
my_model.performances()
my_model.confusion_matrix()
my_model.plot_feature_importance()
my_model.plot_classification_report()
