from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

#carico i dati
iris_data = load_iris()
X = iris_data.data  # caratteristiche
y = iris_data.target  # target

# Rescaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#suddivisione dati
X_train,X_test, y_train, y_test = train_test_split(X_scaled, y, test_size = 0.3, random_state = 42)

#scelta del modello
model = DecisionTreeClassifier()

#Addestramento
model.fit(X_train, y_train)

#Prediction
y_pred = model.predict(X_test)

#Accuracy
performances = classification_report(y_test, y_pred)
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