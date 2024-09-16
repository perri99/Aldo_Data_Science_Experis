import numpy as np
import pandas as pd
import random as rd
import matplotlib.pyplot as plt

def genera_dati(media = 2000, dev_std = 500):
    data = np.random.normal(loc = media, scale = dev_std, size = 365) #distribuzione normale
    data = data.astype(int) #converto in intero per avere numero plausibile
    return data

def trend_crescente(data, incremento = 10): #trend lineare brutale
    increments = np.linspace(0,365*incremento, 365)
    data = np.add(data, increments) #incremento i dati di incremento * numero di giorni passati da inizio anno
    return data

def serie_temporale(data):
    temporal_range = pd.date_range(start='2023-01-01', end = '2023-12-31')
    dizionario = {'Data':temporal_range,
                  'Visitatori':data}
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
visitatori_giornalieri = trend_crescente(visitatori_giornalieri, incremento = 1)
serie = serie_temporale(visitatori_giornalieri)
medie, deviazioni = medie_mensili(serie)
print(serie.describe())

# Calcolo della media mobile settimanale
serie['Media Mobile Settimanale'] = serie['Visitatori'].rolling(window=7).mean()
print(serie.head(14))
#-------Plotting data---------------------
months = ['Jan','Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
days = np.arange(0,365)
# Grafico delle medie mensili
plt.scatter(months, medie, marker='*', linewidths=0.5)
plt.title('Medie mensili')
plt.show()

# Grafico visitatori giornalieri con media mobile settimanale
plt.plot(days, visitatori_giornalieri, label='Visitatori Giornalieri', alpha=0.5)
plt.plot(days, serie['Media Mobile Settimanale'], label='Media Mobile Settimanale (7 giorni)', color='red', linewidth=2)
plt.title('Visitatori Giornalieri con Media Mobile Settimanale')
plt.legend()
plt.show()
