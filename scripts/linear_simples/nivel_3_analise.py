"""
Nível 3: Análise Crítica
Diagnóstico de erros, limites do modelo, testes estatísticos
"""
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Dados de exemplo (altura em cm, peso em kg)
x = np.array([160, 165, 170, 175, 180]).reshape(-1, 1)
y = np.array([60, 65, 70, 75, 80])

# Ajuste do modelo
modelo = LinearRegression()
modelo.fit(x, y)
y_pred = modelo.predict(x)

# Gráfico de resíduos
residuos = y - y_pred
plt.scatter(x, residuos)
plt.axhline(0, color='red', linestyle='--')
plt.xlabel('Altura (cm)')
plt.ylabel('Resíduo (Peso real - Peso previsto)')
plt.title('Gráfico de Resíduos')
plt.show()

# Curva de aprendizado (simulação)
from sklearn.model_selection import learning_curve
train_sizes = [2, 3, 4, 5]
train_scores = []
test_scores = []
for size in train_sizes:
    modelo = LinearRegression()
    modelo.fit(x[:size], y[:size])
    train_pred = modelo.predict(x[:size])
    test_pred = modelo.predict(x)
    train_scores.append(np.mean((y[:size] - train_pred)**2))
    test_scores.append(np.mean((y - test_pred)**2))
plt.plot(train_sizes, train_scores, label='Erro de treino')
plt.plot(train_sizes, test_scores, label='Erro de teste')
plt.xlabel('Tamanho do conjunto de treino')
plt.ylabel('Erro quadrático médio (MSE)')
plt.title('Curva de Aprendizado')
plt.legend()
plt.show()

# Limites do modelo
print('Limites: O modelo linear simples só funciona bem para relações aproximadamente lineares.')
print('Teste estatístico: O gráfico de resíduos deve mostrar dispersão aleatória em torno de zero.')
