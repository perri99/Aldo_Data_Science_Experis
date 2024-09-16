import numpy as np
import pandas as pd
import random as rd
import matplotlib.pyplot as plt

def genera_dati(media = 2000, dev_std = 500):
    data = np.random.normal(loc = media, scale = dev_std, size = 365) #distribuzione normale
    data = data.astype(int) #converto in intero per avere numero plausibile
    return data

def trend_crescente(data, incremento = 10): #trend lineare brutale
    for index in range(len(data)):
        data[index] += index * incremento #incremento i dati di 10 * numero di giorni passati da inizio anno
    return data

def serie_temporale(data):
    temporal_range = pd.date_range(start='2023-01-01', end = '2023-12-31')
    dizionario = {'Data':temporal_range,
                  'Visitatori':[]}
    for index in range(len(data)):
        dizionario['Visitatori'].append(data[index])
    df = pd.DataFrame(dizionario)
    df.set_index('Data', inplace=True)
    return df

def medie_mensili(dataframe):
    medie = dataframe.resample('M').mean()
    deviazioni = dataframe.resample('M').std()
    return medie.to_numpy(), deviazioni.to_numpy()

visitatori_giornalieri = genera_dati()
serie = serie_temporale(visitatori_giornalieri)
print(serie.describe())
visitatori_giornalieri = trend_crescente(visitatori_giornalieri)
serie = serie_temporale(visitatori_giornalieri)
print(serie.describe())
months = ['Jan','Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
days = np.arange(0,365)
medie, deviazioni = medie_mensili(serie)
plt.plot(months, medie)
plt.show()
plt.plot(days, visitatori_giornalieri)
plt.show()
