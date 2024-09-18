import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Configura Seaborn
sns.set_theme(style="dark")

# Crea alcuni dati
data = np.random.normal(size=100)
x = np.linspace(0,7,1000)
y = np.sin(x)
# Crea un grafico
sns.lineplot(x=x,y=y)
plt.title('Sin(x)')
plt.show()
#---------------grafico a barre--------------
categories = ['A', 'B', 'C', 'D', 'E']
values = [3, 7, 2, 5, 8]

plt.figure()
plt.bar(categories, values)
plt.title('Grafico a Barre')
plt.xlabel('Categorie')
plt.ylabel('Valori')
plt.show()
#-------------Istogramma--------------------
data = np.random.randn(1000)

plt.figure()
plt.hist(data, bins=30)
plt.title('Istogramma')
plt.xlabel('Valori')
plt.ylabel('Frequenza')
plt.show()
#-------------ScatterPlot-------------------
x = np.random.rand(50)
y = np.random.rand(50)

plt.figure()
plt.scatter(x, y)
plt.title('Scatter Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()