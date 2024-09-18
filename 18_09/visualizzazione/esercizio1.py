import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

temperatures = np.random.randint(20, 30, 30)
df = pd.DataFrame({'Temperatures': temperatures})
print(df.describe())

temperatura_massima = [df['Temperatures'].max()]*30
temperatura_minima = [df['Temperatures'].min()]*30
temperatura_media = [df['Temperatures'].mean()]*30
temperatura_mediana = [df['Temperatures'].median()]*30

days = np.arange(1,31)

plt.bar(days, df['Temperatures'])
plt.plot(days, temperatura_massima, label='Temperatura massima', color='red')
plt.plot(days, temperatura_minima, label='Temperatura minima', color='yellow')
plt.plot(days, temperatura_media, label='Temperatura media', color='green', linestyle='--')
plt.plot(days, temperatura_mediana, label='Temperatura mediana', color='orange', linestyle='--')
plt.legend()
plt.title('Temperatura mensile')
plt.ylim(19,30)
plt.xlabel('Giorni')
plt.ylabel('Temperatura °C')
plt.show()
plt.scatter(days, df['Temperatures'], marker = '*')
plt.plot(days, temperatura_media, label='Temperatura media', color='green', linestyle='-')
plt.plot(days, temperatura_mediana, label='Temperatura mediana', color='orange', linestyle='-')
plt.title('Temperatura Mensile')
plt.xlabel('Giorni')
plt.ylabel('Temperatura °C')
plt.legend()
plt.show()

