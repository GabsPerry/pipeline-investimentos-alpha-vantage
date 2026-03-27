# Crypto Lakehouse Pipeline with Databricks

![Status](https://img.shields.io/badge/Status-Finalizado-success)
![GitHub last commit](https://img.shields.io/github/last-commit/GabsPerry/pipeline-investimentos-alpha-vantage)
![License](https://img.shields.io/badge/License-MIT-green)
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![PySpark](https://img.shields.io/badge/PySpark-Data%20Processing-orange?logo=apachespark)
![Databricks](https://img.shields.io/badge/Databricks-Lakehouse-red?logo=databricks)
![Delta Lake](https://img.shields.io/badge/Delta%20Lake-Storage-0A66C2)
![SQL](https://img.shields.io/badge/SQL-Analytics-lightgrey?logo=postgresql)

Pipeline completo de Engenharia de Dados para ingestão, transformação, qualidade e análise de dados de criptomoedas utilizando **Python, PySpark, Delta Lake e Databricks**.

Este projeto implementa uma arquitetura **Lakehouse**, seguindo a arquitetura **medalhão** (**Bronze / Silver / Gold**) consumindo dados da API da **Alpha Vantage**, salvando arquivos JSON no **Databricks Volume**, processando tudo em **PySpark**, gerando métricas analíticas e exibindo os resultados em um **dashboard no Databricks**.

---

## Objetivo do projeto

Construir um pipeline ponta a ponta de dados para praticar conceitos reais de Engenharia de Dados, incluindo:

- Ingestão de dados via API
- Armazenamento em data lake
- Modelagem em camadas
- Transformações em PySpark
- Data Quality Checks
- Logging estruturado
- Dashboard analítico
- Orquestração via Job ETL

---

## Arquitetura do projeto

<img width="1213" height="864" alt="image" src="https://github.com/user-attachments/assets/9923344d-de33-4a1e-be74-163159ccd61c" />

---

## Tecnologias utilizadas

- Python
- PySpark
- Spark SQL
- Databricks
- Delta Lake
- REST API
- JSON
- Databricks Volumes
- Databricks Jobs
- Databricks SQL Dashboard
- Git / GitHub

---

## Estrutura do projeto

```
crypto-lakehouse-pipeline/
│
├── src/
│   ├── ingestion/
│   │   ├── config.py
│   │   └── ingest_crypto.py
│   │
│   ├── transformations/
│   │   ├── bronze.py
│   │   └── ingest_crypto.py
│   │   └── gold.py
│   │
│   ├── data_quality/
│   │   ├── silver_checks.py
│   │   └── gold_checks.py
│   │
│   └── utils/
│       └── logger.py
│
├── .gitignore
├── LICENSE
└── README.md
```

---

## Fluxo do pipeline

### 1. Ingestão
Consumo da API Alpha Vantage

Extração diária de múltiplas criptomoedas:
- BTC
- ETH
- SOL
- ADA
- XRP
- BNB
- DOT
- DOGE
- TRX
- LTC

Salvamento dos dados em formato JSON no Databricks Volume

### 2. Bronze Layer
- Leitura dos arquivos RAW
- Padronização inicial
- Armazenamento da camada bruta em tabela Delta

### 3. Silver Layer
- Tratamento e tipagem de colunas
- Deduplicação dos dados
- Aplicação de regras de negócio
- MERGE incremental em Delta

### 4. Gold Layer
Criação de métricas analíticas, como:
- price_today
- price_yesterday
- perc_change
- spread
- spread_pct
- price_rank

### 5. Dashboard
Visualizações construídas diretamente no Databricks SQL

Análise de:
- Ranking por preço
- Variação diária
- Spread percentual
- Comparação financeira das criptomoedas

### 6. Orquestração
Criação de Job ETL no Databricks

Execução automatizada das etapas:
- Ingestão
- Bronze
- Silver
- Gold
- Atualização do Dashboard

---

## Data Quality Checks

Para aumentar a confiabilidade e simular um pipeline de dados mais próximo de um ambiente de produção, este projeto inclui validações de Data Quality tanto na camada Silver quanto na camada Gold.
O objetivo dessas verificações é garantir que os dados transformados permaneçam consistentes, válidos e confiáveis antes de serem consumidos pela camada analítica final.

## Como o Data Quality funciona

A lógica de Data Quality foi implementada por meio de funções de validação executadas durante o processo de transformação.
Essas verificações são acionadas automaticamente durante a execução das camadas Silver e Gold, antes que os dados finais sejam persistidos.

Se alguma validação falhar, o pipeline pode:
- Registrar o problema para fins de observabilidade
- Impedir que dados inválidos avancem para a próxima etapa
- Gerar um erro para interromper o job (dependendo da severidade da validação)

Isso ajuda a garantir que apenas dados limpos e prontos para análise cheguem à camada final consumida pelo dashboard.

## Exemplos atuais de validação

Validações da camada Silver: 
- Campos obrigatórios não podem ser nulos
- Campos numéricos devem ser convertidos corretamente
- Registros duplicados devem ser removidos
- Campos de data devem seguir o formato esperado

Validações da camada Gold: 
- Métricas agregadas não podem ser nulas
- Métricas de negócio devem seguir a lógica esperada
- Tabelas de saída devem conter registros válidos
- O dataset analítico final deve estar pronto para consumo no dashboard

---

## Logging

O projeto também conta com logging estruturado para rastrear a execução do pipeline.

Exemplos de eventos monitorados:
- Início e fim da ingestão
- Criptomoeda em processamento
- Arquivos salvos
- Início/fim das transformações Bronze / Silver / Gold
- Falhas de qualidade de dados
- Erros de API

---

## Métricas criadas na camada Gold

Algumas métricas analíticas implementadas:
- Preço atual
- Preço do dia anterior
- Variação percentual diária
- Spread absoluto
- Spread percentual
- Ranking por preço

Essas métricas foram usadas para alimentar o dashboard analítico.

---

## Principais aprendizados

Este projeto foi construído para consolidar conhecimentos práticos em:
- Engenharia de Dados
- Arquitetura Lakehouse
- PySpark
- Delta Lake
- Modelagem da arquitetura medalhão
- Data Quality
- Logging
- ETL / ELT
- Databricks Workflows
- Dashboards analíticos
