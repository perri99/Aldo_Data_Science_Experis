import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import adjusted_rand_score, homogeneity_score
from sklearn.preprocessing import StandardScaler
import seaborn as sns

def visualizza_dati(dati):
    df = pd.DataFrame(dati.data, columns=dati.feature_names)
    df['target'] = dati.target
    print(df)
    return df

def pre_processing(dati):
    scaler = StandardScaler()
    return scaler.fit_transform(dati.data)

def clustering(X, n = 3, rs = 42):
    kmeans = KMeans(n_clusters = n, random_state = rs)
    kmeans.fit(X)
    y_kmeans = kmeans.predict(X)
    return y_kmeans

def principal_components(X, n_components = 4):
    pca = PCA(n_components=n_components)
    X_pca = pca.fit_transform(X)
    return X_pca, pca 

iris = load_iris()
df = visualizza_dati(iris)
X = pre_processing(iris)
y_kmeans = clustering(X)
X_pca, pca = principal_components(X)


sns.pairplot(df, hue='target', palette='Set2')
plt.show()


plt.subplot(1, 2, 1)  # 1 riga, 2 colonne, 1° grafico
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y_kmeans, cmap='viridis', s=50)

plt.title('Clustering K-Means (ridotto con PCA)')
plt.xlabel('Prima componente principale')
plt.ylabel('Seconda componente principale')
plt.legend()
plt.grid(True)

# Grafico 2: Etichette reali
plt.subplot(1, 2, 2)  # 1 riga, 2 colonne, 2° grafico
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=iris.target, cmap='viridis', s=50)
plt.title('Etichette reali (ridotto con PCA)')
plt.xlabel('Prima componente principale')
plt.ylabel('Seconda componente principale')
plt.grid(True)

# Mostrare entrambi i grafici
plt.tight_layout()
plt.show()


ari = adjusted_rand_score(iris.target, y_kmeans)
homogeneity = homogeneity_score(iris.target, y_kmeans)
print(f'Adjusted Rand Index (ARI): {ari:.2f}')
print(f'Homogeneity Score: {homogeneity:.2f}')
