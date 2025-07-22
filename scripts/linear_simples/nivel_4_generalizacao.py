"""
Nível 4: Generalização
Comparação entre modelos de regressão: linear, polinomial e logarítmica
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error

# Dados de exemplo (altura em cm, peso em kg)
x = np.array([160, 165, 170, 175, 180, 185, 190, 195, 200]).reshape(-1, 1)
y = np.array([60, 65, 70, 75, 80, 85, 90, 95, 100])

# Modelo Linear
modelo_linear = LinearRegression()
modelo_linear.fit(x, y)
y_pred_linear = modelo_linear.predict(x)
mse_linear = mean_squared_error(y, y_pred_linear)

# Modelo Polinomial (grau 2)
poly = PolynomialFeatures(degree=2)
x_poly = poly.fit_transform(x)
modelo_poly = LinearRegression()
modelo_poly.fit(x_poly, y)
y_pred_poly = modelo_poly.predict(x_poly)
mse_poly = mean_squared_error(y, y_pred_poly)

# Modelo Logarítmico
x_log = np.log(x)
modelo_log = LinearRegression()
modelo_log.fit(x_log, y)
y_pred_log = modelo_log.predict(x_log)
mse_log = mean_squared_error(y, y_pred_log)

# Gráficos de comparação
plt.figure(figsize=(10,6))
plt.scatter(x, y, label='Dados reais')
plt.plot(x, y_pred_linear, label='Linear', color='blue')
plt.plot(x, y_pred_poly, label='Polinomial (grau 2)', color='green')
plt.plot(x, y_pred_log, label='Logarítmico', color='orange')
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.title('Comparação de Modelos de Regressão')
plt.legend()
plt.show()

print(f"MSE Linear: {mse_linear:.2f}")
print(f"MSE Polinomial: {mse_poly:.2f}")
print(f"MSE Logarítmico: {mse_log:.2f}")

# Interpretação
print("\nO modelo com menor MSE representa melhor os dados. Visualize os gráficos para analisar o ajuste de cada modelo.")
