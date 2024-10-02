import pandas as pd
from sklearn.preprocessing import LabelEncoder
# One-hot encoding delle variabili categoriche
dataset_df = pd.get_dummies('02-10/train_house.csv', drop_first=True)



# Label encoding per le variabili categoriche ordinali
labelencoder = LabelEncoder()
dataset_df['MSZoning'] = labelencoder.fit_transform(dataset_df['MSZoning'])
print(dataset_df.head(1))
