import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

temperatures = np.random.randint(20, 30, 30)
df = pd.DataFrame({'Temperatures': temperatures})

temperatura_massima = [df['Temperatures'].max()]*30
temperatura_minima = [df['Temperatures'].min()]*30
temperatura_media = [df['Temperatures'].mean()]*30
temperatura_mediana = [df['Temperatures'].median()]*30

days = np.arange(1,31)

plt.bar(days, df['Temperatures'], label = 'Temperatura Giornaliera')
plt.plot(days, temperatura_massima, label = 'Temperatura massima')
plt.plot(days, temperatura_minima, label = 'Temperatura minima')
plt.plot(days, temperatura_media, label = 'Temperatura media')
plt.plot(days, temperatura_mediana, label = 'Temperatura mediana')
plt.legend()
plt.title('Temperatura mensile')
plt.ylim(18,30)
plt.xlabel('Giorni')
plt.ylabel('Temperatura °C')
plt.show()