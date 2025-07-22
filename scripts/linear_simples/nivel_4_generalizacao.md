# Nível 4: Generalização

## Quando aplicar o modelo linear simples e como compará-lo com outros

### Limites da regressão linear simples
- Funciona bem quando a relação entre as variáveis é aproximadamente linear.
- Não é adequada para dados com curvaturas, saturações ou crescimento exponencial.

### Comparação com outros modelos

| Modelo              | Quando usar                                      | Exemplo prático           |
|---------------------|--------------------------------------------------|---------------------------|
| Linear Simples      | Relação linear clara                             | Altura vs. peso           |
| Polinomial          | Relação curva suave, não linear                  | Idade vs. renda           |
| Logarítmica         | Crescimento rápido, depois saturação             | Popularidade no tempo     |
| Exponencial         | Crescimento acelerado                            | População, juros          |
| Logística           | Classificação binária, probabilidade             | Doença (sim/não)          |

### Exemplo prático de comparação

- Utilize scripts dos níveis anteriores para ajustar modelos linear, polinomial e logarítmico aos mesmos dados.
- Compare os gráficos e os valores de erro (MSE) para cada modelo.
- Analise qual modelo representa melhor os dados e por quê.

### Dicas para generalização
- Sempre visualize os dados antes de escolher o modelo.
- Teste diferentes abordagens e compare os resultados.
- Use métricas como MSE, R² e gráficos de resíduos para avaliar o ajuste.

---

**Próximo nível:** Aplicação em projeto real com dataset aberto.
