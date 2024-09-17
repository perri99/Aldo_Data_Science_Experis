from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = load_iris()
X = data.data  # caratteristiche
y = data.target  # target

# È essenziale normalizzare e ridimensionare i dati
# prima di applicare algoritmi di machine learning.
#Esempio di ridimensionamento dei dati, ora non utile
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Suddividere il dataset in set di training e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Regressione lineare
model = LinearRegression()
model.fit(X_train, y_train)
predictions_linear = model.predict(X_test)

#K-Nearest Neighbors (KNN)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
predictions_knn = knn.predict(X_test)

print('Accuracy linear regression:', accuracy_score(y_test, predictions_linear))
print('Accuracy KNN:', accuracy_score(y_test, predictions_knn))