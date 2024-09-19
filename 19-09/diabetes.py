from sklearn.datasets import load_diabetes
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso, Lars
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

def visualizza_dati(dati):
    df = pd.DataFrame(dati.data, columns=dati.feature_names)
    df['target'] = dati.target
    print(df)

def regressione(model, X_train, y_train, X_test):
    predictor = model
    predictor.fit(X_train, y_train)
    predictions = predictor.predict(X_test)
    return predictions, predictor.coef_, predictor.intercept_

diabetes = load_diabetes()
#visualizzo i dati 
visualizza_dati(diabetes)
#splitting dei dati
X_train, X_test, y_train, y_test = train_test_split(diabetes.data, diabetes.target, test_size=0.2, random_state=42)
models = [LinearRegression(), Ridge(), Lasso(), Lars(), ]

for model in models:
    print(f'{type(model).__name__}')
    predictions, coefficienti, intercetta = regressione(model, X_train, y_train, X_test)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    print('Errore quadratico = ',mse)
    print('Parametro r2 =', r2)
    print("Coefficienti: ", coefficienti)
    print("Intercetta: ", intercetta)
    plt.scatter(y_test, predictions, color='blue')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linewidth=2)  # Linea ideale (y_test == y_pred)

    plt.title(f'{type(model).__name__}')
    plt.show()