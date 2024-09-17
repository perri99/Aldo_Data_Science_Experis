import pandas as pd
import numpy as np

anno = 2024
mese = 3

cities = ['Roma', 'Bologna', 'Milano']
products = ['Chitarra', 'Basso', 'Batteria']
dates = pd.date_range(start=f'{anno}-{mese:02d}-01', end=f'{anno}-{mese:02d}-30')

vendite = np.random.randint(50,100,30)
data_cities = [np.random.choice(cities) for _ in range(30)]
data_prducts= [np.random.choice(products) for _ in range(30)]

df = pd.DataFrame({'Data': dates,
                  'Città': data_cities,
                  'Prodotto': data_prducts,
                  'Vendite': vendite})

print('dataframe originale')
print(df)

#creazione tabella pivot mostrante la media 
pivot_df = df.pivot_table(values='Vendite', index='Prodotto', columns='Città', aggfunc='mean')
print('Tabella Pivot')
print(pivot_df)

#metodo groupby
df = df.drop_duplicates()
df_senzadata = df.drop(columns = 'Data')
grouped_df  = df_senzadata.groupby('Prodotto')['Vendite'].sum()

#grouped_df.drop_duplicates()
print('Risultato di groupby:')
print(grouped_df)

