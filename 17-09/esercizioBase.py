from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data_iris = load_iris()
X = data_iris.data
y = data_iris.target

X_train,X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

model = KNeighborsClassifier(n_neighbors = 9)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuratezza del modello: {accuracy:.2f}")