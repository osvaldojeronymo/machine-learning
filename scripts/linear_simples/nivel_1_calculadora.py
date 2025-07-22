"""
Nível 1: Calculadora com Script
Regressão Linear Simples - Implementação manual dos cálculos (sem sklearn)
"""
import numpy as np

# Dados de exemplo (altura em cm, peso em kg)
x = np.array([160, 165, 170, 175, 180])
y = np.array([60, 65, 70, 75, 80])

# Cálculo dos coeficientes da reta (y = a*x + b)
def regressao_linear_manual(x, y):
    n = len(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    a = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean)**2)
    b = y_mean - a * x_mean
    return a, b

a, b = regressao_linear_manual(x, y)
print(f"Coeficiente angular (a): {a:.2f}")
print(f"Coeficiente linear (b): {b:.2f}")

# Previsão dos valores
y_pred = a * x + b

# Cálculo do erro quadrático médio (MSE)
mse = np.mean((y - y_pred)**2)
print(f"Erro quadrático médio (MSE): {mse:.2f}")

# Dica: Para visualizar, use matplotlib (opcional)
# import matplotlib.pyplot as plt
# plt.scatter(x, y, label='Dados reais')
# plt.plot(x, y_pred, color='red', label='Regressão Linear')
# plt.xlabel('Altura (cm)')
# plt.ylabel('Peso (kg)')
# plt.legend()
# plt.show()
