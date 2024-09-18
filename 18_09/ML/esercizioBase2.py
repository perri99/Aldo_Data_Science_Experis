from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import seaborn as sns

class PredictorDTC:

    def __init__(self, data_function):
        self.data = data_function
        self.X = self.data.data
        self.y = self.data.target
        self.model = DecisionTreeClassifier

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
        model = DecisionTreeClassifier()
        #Addestramento
        model.fit(self.X_train, self.y_train)
        return model

    def prediction(self):
        return self.model.predict(self.X_test)

my_model = PredictorDTC(load_iris())
my_model.train_DTC()
pred = my_model.prediction()
'''
#Accuracy
performances = classification_report(y_test, y_pred, target_names = labels)
print('Classification report:')
print(performances)

#Matrice di confusione
matrix = confusion_matrix(y_test, y_pred)
print('Confusion Matrix')
print(matrix)
#visualizzazione matrice
visual = ConfusionMatrixDisplay(matrix)
visual.plot()
plt.show()
'''
