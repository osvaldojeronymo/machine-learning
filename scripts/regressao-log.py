# regressao-log.py

# Importando bibliotecas - warnings
import warnings
warnings.filterwarnings('ignore') # Suprime avisos gerados por bibliotecas (warnings).

# Importanto bibliotecas - manipulação de dados
import pandas as pd
import numpy as np

# Importando bibliotecas - visualização de dados
import matplotlib.pyplot as plt
import seaborn as sns

# Importando bibliotecas - regressão logística
from sklearn.linear_model import LogisticRegression #para aplicar a Regressão Logística.
from sklearn.model_selection import train_test_split #para dividir os dados.
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report # para avaliar o desempenho do modelo.

# Importando bibliotecas - pré-processamento
from sklearn.preprocessing import StandardScaler #Padroniza os dados para que tenham média 0 e desvio padrão 1.

# Carregando o dataset
df = pd.read_csv('ml-hands-on-caixa\dados_exemplo\creditcard_sampled.csv')

