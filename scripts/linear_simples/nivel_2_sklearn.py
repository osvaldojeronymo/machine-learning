"""
Nível 2: Ferramental Pronto
Regressão Linear usando sklearn
"""
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
"""
Objetivo: Estimar ou entender o impacto das características do veículo 
sobre as emissões de CO₂.
Perguntas orientadoras:
a.Existe uma relação linear entre o tamanho do motor (Engine Size) e as emissões
de CO₂?
b.O número de cilindros (Cylinders) impacta linearmente as emissões?
c.Quais variáveis explicam melhor as emissões em um modelo de regressão linear
múltipla?
"""
# Dados de exemplo (altura em cm, peso em kg)
x = np.array([160, 165, 170, 175, 180]).reshape(-1, 1)
y = np.array([60, 65, 70, 75, 80])

# Criação e ajuste do modelo
modelo = LinearRegression()
modelo.fit(x, y)

# Coeficientes
print(f"Coeficiente angular (a): {modelo.coef_[0]:.2f}")
print(f"Coeficiente linear (b): {modelo.intercept_:.2f}")

# Previsão dos valores
y_pred = modelo.predict(x)

# Erro quadrático médio (MSE)
mse = np.mean((y - y_pred)**2)
print(f"Erro quadrático médio (MSE): {mse:.2f}")

# Visualização
plt.scatter(x, y, label='Dados reais')
plt.plot(x, y_pred, color='red', label='Regressão Linear (sklearn)')
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.legend()
plt.show()
