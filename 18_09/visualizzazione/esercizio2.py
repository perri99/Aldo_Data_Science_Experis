import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def genera_dati(media = 2000, dev_std = 500, giorni = 365):
    data = np.random.normal(loc = media, scale = dev_std, size = giorni) #distribuzione normale
    data = data.astype(int) #converto in intero per avere numero plausibile
    return data

def modifica_trend(data, incremento = 1, giorni = 365): #trend lineare brutale
    increments = np.linspace(0,giorni*incremento, giorni)
    data = np.add(data, increments) #incremento i dati di incremento * numero di giorni passati da inizio anno
    data = np.maximum(data, 0)
    data = data.astype(int)
    return data

def genera_patologie(giorni):
    patologie = ['ossa', 'cuore', 'testa']
    lista_patologie = [np.random.choice(patologie) for _ in range(giorni)]
    return lista_patologie

def serie_temporale(data):
    temporal_range = pd.date_range(start='2024-01-01', end = '2024-10-31')
    dizionario = {'Data':temporal_range,
                  'Visitatori':data,
                  'Patologia':genera_patologie(giorni = 305)}
    df = pd.DataFrame(dizionario)
    df.set_index('Data', inplace=True)
    return df

def medie_mensili(dataframe):
    df = dataframe.drop(columns = 'Patologia')
    medie = df.resample('M').mean()
    deviazioni = df.resample('M').std()
    return medie.to_numpy(), deviazioni.to_numpy()

#creo array con visitatori giornalieri distribuiti normalmente
visitatori_giornalieri = genera_dati(media = 1200, dev_std = 900, giorni=305)
#modifico il trend dei dati
visitatori_giornalieri = modifica_trend(visitatori_giornalieri, incremento=-3, giorni = 305)
#creo il dataframe
df = serie_temporale(visitatori_giornalieri)
#------calcolo le medie mensili-------------
medie_mens, deviazioni_mens = medie_mensili(df)
months = ['Jan','Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug', 'Sep', 'Oct']
for month in months:
    print(f'Media visitatori mese {month} =', medie_mens[months.index(month)], '+-', deviazioni_mens[months.index(month)])
#------Cerco la patologia più e meno frequente---------
print(df['Patologia'].value_counts())
print('Patologia più frequente:', df['Patologia'].value_counts().idxmax())
print('Patologia meno frequente:', df['Patologia'].value_counts().idxmin())
#------Media Settimanale-----------------------
df1 = df.drop(columns='Patologia')
df1['Media Mobile Settimanale'] = df1['Visitatori'].rolling(window=7).mean()
#grafici
days = np.arange(0,305)
# Grafico delle medie mensili
plt.plot(months, medie_mens, marker = 'o')
plt.title('Medie mensili')
plt.show()

# Grafico visitatori giornalieri con media mobile settimanale
plt.plot(days, visitatori_giornalieri, label='Visitatori Giornalieri', alpha=0.5)
plt.plot(days, df1['Media Mobile Settimanale'], label='Media Mobile Settimanale (7 giorni)', color='red', linewidth=2)
plt.title('Visitatori Giornalieri con Media Mobile Settimanale')
plt.legend()
plt.show()
#grafico_patologie
patologie_counts = df['Patologia'].value_counts()  # Ottieni i valori delle patologie
plt.bar(patologie_counts.index, patologie_counts.values, color=['blue', 'green', 'orange'])
plt.title('Distribuzione delle Patologie')
plt.xlabel('Tipo di Patologia')
plt.ylabel('Numero di Casi')
plt.show()
