import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

# Dados de exemplo
x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 6, 14, 28, 45])  # Nota: claramente não-linear

# Criar um modelo de regressão polinomial de grau 2
grau = 2
modelo = make_pipeline(PolynomialFeatures(grau), LinearRegression())
modelo.fit(x, y)

# Previsão
x_plot = np.linspace(1, 5, 100).reshape(-1, 1)
y_plot = modelo.predict(x_plot)

# Visualizar
plt.scatter(x, y, color='blue', label='Dados reais')
plt.plot(x_plot, y_plot, color='red', label='Regressão polinomial (grau 2)')
plt.legend()
plt.title('Exemplo de Regressão Polinomial')
plt.show()
