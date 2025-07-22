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

# Importando bibliotecas - regressão polionomial
from sklearn.preprocessing import PolynomialFeatures #para aplicar a Regressão Polinomial.
from sklearn.linear_model import LinearRegression #para aplicar a Regressão Linear.

from sklearn.metrics import mean_absolute_error, mean_squared_error #para avaliar o desempenho do modelo.
from sklearn.model_selection import train_test_split

# Importando bibliotecas - pré-processamento
from sklearn.preprocessing import StandardScaler #Padroniza os dados para que tenham média 0 e desvio padrão 1.


# Carregando o dataset
df = pd.read_csv('ml-hands-on-caixa\dados_exemplo\dados.txt')
# Separando variáveis independentes (X) e dependente (y)
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# Separando em treino e teste (80% treino, 20% teste)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Padronizando os dados
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Regressão Polinomial Grau 2
poly2 = PolynomialFeatures(degree=2)
X_train_poly2 = poly2.fit_transform(X_train_scaled)
X_test_poly2 = poly2.transform(X_test_scaled)
model2 = LinearRegression()
model2.fit(X_train_poly2, y_train)
y_pred2_train = model2.predict(X_train_poly2)
y_pred2_test = model2.predict(X_test_poly2)
mse_poly2_train = mean_squared_error(y_train, y_pred2_train)
mse_poly2_test = mean_squared_error(y_test, y_pred2_test)
print(f"MSE (Regressão Polinomial Grau 2, treino): {mse_poly2_train}")
print(f"MSE (Regressão Polinomial Grau 2, teste): {mse_poly2_test}")

# Regressão Polinomial Grau 3
poly3 = PolynomialFeatures(degree=3)
X_train_poly3 = poly3.fit_transform(X_train_scaled)
X_test_poly3 = poly3.transform(X_test_scaled)
model3 = LinearRegression()
model3.fit(X_train_poly3, y_train)
y_pred3_train = model3.predict(X_train_poly3)
y_pred3_test = model3.predict(X_test_poly3)
mse_poly3_train = mean_squared_error(y_train, y_pred3_train)
mse_poly3_test = mean_squared_error(y_test, y_pred3_test)
print(f"MSE (Regressão Polinomial Grau 3, treino): {mse_poly3_train}")
print(f"MSE (Regressão Polinomial Grau 3, teste): {mse_poly3_test}")

# Visualização dos resultados
import matplotlib.pyplot as plt
import numpy as np

# Para visualização, vamos assumir que X tem apenas uma feature
if X.shape[1] == 1:
    # Ordenar os dados de teste para visualização mais clara
    idx = np.argsort(X_test.values.flatten())
    X_test_sorted = X_test.values.flatten()[idx]
    y_test_sorted = y_test.values.flatten()[idx]
    # Previsões ordenadas
    y_pred2_sorted = y_pred2_test[idx]
    y_pred3_sorted = y_pred3_test[idx]

    plt.figure(figsize=(10,6))
    plt.scatter(X_train, y_train, color='gray', alpha=0.5, label='Treino')
    plt.scatter(X_test_sorted, y_test_sorted, color='red', label='Teste')
    plt.plot(X_test_sorted, y_pred2_sorted, color='blue', label='Reg. Polinomial Grau 2')
    plt.plot(X_test_sorted, y_pred3_sorted, color='green', label='Reg. Polinomial Grau 3')
    plt.xlabel('X')
    plt.ylabel('y')
    plt.title('Ajuste dos Modelos Polinomiais')
    plt.legend()
    plt.show()
else:
    print('Visualização automática disponível apenas para 1 feature. Exibindo gráfico de resíduos para múltiplas features:')
    plt.figure(figsize=(10,5))
    plt.subplot(1,2,1)
    plt.scatter(y_test, y_pred2_test, color='blue', alpha=0.7)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
    plt.xlabel('y real')
    plt.ylabel('y previsto')
    plt.title('Grau 2: y real vs y previsto')

    plt.subplot(1,2,2)
    plt.scatter(y_test, y_pred3_test, color='green', alpha=0.7)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
    plt.xlabel('y real')
    plt.ylabel('y previsto')
    plt.title('Grau 3: y real vs y previsto')

    plt.tight_layout()
    plt.show()
