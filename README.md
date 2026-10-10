# dados-financeiros 📊🤖

Este projeto implementa uma Inteligência Artificial utilizando o algoritmo **Random Forest Regressor** para analisar e prever o volume de investimentos e ativos financeiros com base em dados históricos de preços (OHLC).

## 🚀 Tecnologias Utilizadas
* **Python** (Linguagem principal)
* **Pandas** (Manipulação e limpeza de dados)
* **Scikit-Learn** (Criação e treino do modelo de Machine Learning)
* **Joblib** (Salvamento do modelo treinado)

## 📋 Como Funciona o Código
1. **Carregamento:** Lê a base de dados contida no arquivo `train.csv`.
2. **Tratamento:** Remove linhas duplicadas e preenche valores ausentes.
3. **Treinamento:** Utiliza o `RandomForestRegressor` com as colunas `open`, `high`, `low` e `close` para prever a coluna `volume`.
4. **Exportação:** Salva o resultado final pronto em um arquivo `.pkl`.

## 🛠️ Como Executar
1. Certifique-se de ter o arquivo `train.csv` na raiz do projeto.
2. Instale as dependências:
   ```bash
   pip install pandas scikit-learn joblib
   ```
3. Execute o script principal:
   ```bash
   python ia.py
   ```
