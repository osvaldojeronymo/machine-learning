
# normal-with-MinMaxScaler.py

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Dados simulados: R, G, B, Temperatura
dados = np.array([
    [100, 150, 200, 35.0],
    [110, 140, 210, 36.5],
    [120, 130, 220, 37.8],
    [130, 120, 230, 38.6],
    [140, 110, 240, 39.2]
])

scaler = MinMaxScaler()
dados_normalizados = scaler.fit_transform(dados)

df_normalizado = pd.DataFrame(dados_normalizados, columns=['R', 'G', 'B', 'Temperatura'])
print("Dados Normalizados:")
print(df_normalizado)
