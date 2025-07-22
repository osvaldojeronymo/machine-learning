"""
Análise de Emissões de CO₂ de Veículos
Responde às perguntas:
 a. Existe uma relação linear entre Engine Size e CO₂?
 b. O número de Cylinders impacta linearmente as emissões?
 c. Quais variáveis explicam melhor as emissões em regressão linear múltipla?
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Carregar o dataset
colunas = ['Engine Size(L)', 'Cylinders', 'Fuel Consumption Comb (L/100 km)', 'CO2 Emissions(g/km)']
df = pd.read_csv("C:\\Users\\osval\\OneDrive\\Área de Trabalho\\Ano2025\\Python\\hands-on-ML\\ml-hands-on-caixa\\datasets\\co2.csv", usecols=colunas)
# Para salvar resultados
relatorio = []
def add_md(text):
    print(text)
    relatorio.append(text + '\n')

add_md("# Análise de Emissões de CO₂ de Veículos\n")
add_md("## a) Engine Size vs CO₂")
# a. Relação linear entre Engine Size e CO₂
X_engine = df[['Engine Size(L)']].values
y_co2 = df['CO2 Emissions(g/km)'].values
modelo_engine = LinearRegression().fit(X_engine, y_co2)
add_md(f"Coeficiente angular: **{modelo_engine.coef_[0]:.2f}**  ")
add_md(f"Intercepto: **{modelo_engine.intercept_:.2f}**  ")
add_md(f"R²: **{modelo_engine.score(X_engine, y_co2):.2f}**  ")
add_md("**Interpretação:** Cada aumento de 1 litro no motor aumenta, em média, {:.2f} g/km de CO₂. O modelo explica {:.0f}% da variação das emissões apenas pelo tamanho do motor.".format(modelo_engine.coef_[0], modelo_engine.score(X_engine, y_co2)*100))
plt.figure()
plt.scatter(X_engine, y_co2, alpha=0.3, label='Dados')
plt.plot(X_engine, modelo_engine.predict(X_engine), color='red', label='Regressão Linear')
plt.xlabel('Engine Size (L)')
plt.ylabel('CO2 Emissions (g/km)')
plt.title('Engine Size vs CO2 Emissions')
plt.legend()
plt.tight_layout()
plt.savefig(r'C:\\Users\\osval\\OneDrive\\Área de Trabalho\\Ano2025\\Python\\hands-on-ML\\ml-hands-on-caixa\\visuais\\grafico_engine_vs_co2.png')
add_md('![Engine Size vs CO2 Emissions](../visuais/grafico_engine_vs_co2.png)')
plt.close()

# b. Impacto de Cylinders nas emissões
X_cyl = df[['Cylinders']].values
modelo_cyl = LinearRegression().fit(X_cyl, y_co2)
add_md("\n## b) Cylinders vs CO₂")
add_md(f"Coeficiente angular: **{modelo_cyl.coef_[0]:.2f}**  ")
add_md(f"Intercepto: **{modelo_cyl.intercept_:.2f}**  ")
add_md(f"R²: **{modelo_cyl.score(X_cyl, y_co2):.2f}**  ")
add_md("**Interpretação:** Cada cilindro a mais aumenta, em média, {:.2f} g/km de CO₂. O modelo explica {:.0f}% da variação das emissões apenas pelo número de cilindros.".format(modelo_cyl.coef_[0], modelo_cyl.score(X_cyl, y_co2)*100))
plt.figure()
plt.scatter(X_cyl, y_co2, alpha=0.3, label='Dados')
plt.plot(X_cyl, modelo_cyl.predict(X_cyl), color='green', label='Regressão Linear')
plt.xlabel('Cylinders')
plt.ylabel('CO2 Emissions (g/km)')
plt.title('Cylinders vs CO2 Emissions')
plt.legend()
plt.tight_layout()
plt.savefig(r'C:\\Users\\osval\\OneDrive\\Área de Trabalho\\Ano2025\\Python\\hands-on-ML\\ml-hands-on-caixa\\visuais\\grafico_cylinders_vs_co2.png')
add_md('![Cylinders vs CO2 Emissions](../visuais/grafico_cylinders_vs_co2.png)')
plt.close()

# c. Regressão linear múltipla
X_multi = df[['Engine Size(L)', 'Cylinders', 'Fuel Consumption Comb (L/100 km)']].values
modelo_multi = LinearRegression().fit(X_multi, y_co2)
add_md("\n## c) Regressão Linear Múltipla")
add_md("Coeficientes:")
for nome, coef in zip(['Engine Size(L)', 'Cylinders', 'Fuel Consumption Comb (L/100 km)'], modelo_multi.coef_):
    add_md(f"- {nome}: **{coef:.2f}**  ")
add_md(f"Intercepto: **{modelo_multi.intercept_:.2f}**  ")
add_md(f"R²: **{modelo_multi.score(X_multi, y_co2):.2f}**  ")
add_md("**Resumo:** O modelo múltiplo explica {:.0f}% da variação das emissões. O consumo de combustível é a variável mais relevante para prever CO₂.".format(modelo_multi.score(X_multi, y_co2)*100))

# Importância das variáveis
importances = pd.Series(np.abs(modelo_multi.coef_), index=['Engine Size(L)', 'Cylinders', 'Fuel Consumption Comb (L/100 km)'])
plt.figure()
importances.sort_values().plot(kind='barh')
plt.title('Importância das Variáveis na R.L.M.')
plt.xlabel('Valor absoluto do coeficiente')
plt.tight_layout()
plt.savefig(r'C:\\Users\\osval\\OneDrive\\Área de Trabalho\\Ano2025\\Python\\hands-on-ML\\ml-hands-on-caixa\\visuais\\grafico_importancia_variaveis.png')
add_md('![Importância das Variáveis](../visuais/grafico_importancia_variaveis.png)')
plt.close()

# Salvar relatório em arquivo .md
with open(r'C:\\Users\\osval\\OneDrive\\Área de Trabalho\Ano2025\\Python\\hands-on-ML\\ml-hands-on-caixa\docs\\relatorio_co2.md', "w", encoding="utf-8") as f:
    f.writelines(relatorio)
print("Relatório salvo em docs/relatorio_co2.md e gráficos salvos em visuais/.")
