
# standard-with-StandardScaler.py

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Dados simulados: R, G, B, Temperatura
dados = np.array([
    [100, 150, 200, 35.0],
    [110, 140, 210, 36.5],
    [120, 130, 220, 37.8],
    [130, 120, 230, 38.6],
    [140, 110, 240, 39.2]
])

scaler = StandardScaler()
dados_padronizados = scaler.fit_transform(dados)

df_padronizado = pd.DataFrame(dados_padronizados, columns=['R', 'G', 'B', 'Temperatura'])
print("Dados Padronizados:")
print(df_padronizado)
