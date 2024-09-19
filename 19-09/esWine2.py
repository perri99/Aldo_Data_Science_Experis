from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, RandomizedSearchCV, StratifiedKFold
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class PredictorGBC:

    def __init__(self, data_function):
        self.data = data_function
        self.X = self.data.data
        self.y = self.data.target
        self.model = GradientBoostingClassifier()

    def scaling_data(self):
        scaler = StandardScaler()
        self.X_scaled = scaler.fit_transform(self.X)
        return self.X_scaled

    def reduction_PCA(self):
        pca = PCA()
        self.X_reduction = pca.fit_transform(self.X_scaled)
        return self.X_reduction

    def split_data(self, test_size = 0.3, random_state = 42):
        self.scaling_data()
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X_reduction, self.y, test_size = test_size, random_state=random_state)

    

    def find_best_model(self):
        parameters = {'n_estimators': [50, 100, 200],
                      'loss': ['log_loss', 'deviance', 'exponential'],
                        'learning_rate': [0.01, 0.1, 0.2],
                        'max_depth': [3, 4, 5],
                        'subsample': [0.8, 1.0]
                    }
        
        random_search = RandomizedSearchCV( self.model, 
                                            param_distributions=parameters, 
                                            n_iter=10,  
                                            scoring='accuracy', 
                                            random_state=42, 
                                            n_jobs=-1
                                        )
        random_search.fit(self.X_train, self.y_train)
        print(f'Migliori parametri:{random_search.best_params_}' )
        return random_search.best_estimator_
    
    def find_best_model_Kfold(self):
        parameters = {'n_estimators': [50, 100, 200],
                      'loss': ['log_loss', 'deviance', 'exponential'],
                        'learning_rate': [0.01, 0.1, 0.2],
                        'max_depth': [3, 4, 5],
                        'subsample': [0.8, 1.0]
                    }
        
        # Configurazione della validazione incrociata stratificata
        cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

        random_search = RandomizedSearchCV( self.model, 
                                            param_distributions=parameters, 
                                            n_iter=10,  
                                            cv = cv,
                                            scoring='accuracy', 
                                            random_state=42, 
                                            n_jobs=-1
                                        )
        random_search.fit(self.X_train, self.y_train)
        print(f'Migliori parametri:{random_search.best_params_}' )
        return random_search.best_estimator_


    def prediction(self, model):
        self.y_pred = model.predict(self.X_test)
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

    def plot_feature_importance(self, model):
        # Importanza delle feature
        importances = model.feature_importances_
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
        print('Precision:  Indica la proporzione di predizioni corrette tra tutte le predizioni positive')
        print('Recall  (Sensibilità): Indica la proporzione di veri positivi che il modello è riuscito a identificare correttamente. ')
        print('F1-Score: È una media armonica tra precision e recall, e fornisce un bilanciamento tra le due metriche')
        # Creiamo il grafico
        metrics.plot(kind='bar')
        plt.title("Precision, Recall, and F1-Score per Class")
        plt.ylabel("Score")
        plt.xlabel("Class")
        plt.xticks(rotation=0)
        plt.ylim(0, 1)  # Per mantenere la scala tra 0 e 1
        plt.legend(loc="lower right")
        plt.show()

MyModel = PredictorGBC(load_wine())
MyModel.scaling_data()
MyModel.reduction_PCA()
MyModel.split_data()
my_best_model = MyModel.find_best_model()
predictions = MyModel.prediction(my_best_model)
MyModel.performances()
MyModel.confusion_matrix()
MyModel.plot_feature_importance(my_best_model)
MyModel.plot_classification_report()
#provo con l'implemetazione k-Fold
my_best_model = MyModel.find_best_model_Kfold()
predictions = MyModel.prediction(my_best_model)
MyModel.performances()
MyModel.confusion_matrix()
MyModel.plot_feature_importance(my_best_model)
MyModel.plot_classification_report()