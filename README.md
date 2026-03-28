# Crypto Lakehouse Pipeline com Databricks (Free Edition)

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

Construir um pipeline end-to-end de dados para praticar conceitos de Engenharia de Dados, incluindo:

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

<img width="1033" height="655" alt="image" src="https://github.com/user-attachments/assets/13388dde-3a37-41f4-adc3-33ef9f216aae" />

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
│   │   ├── config.py   #secrets (privado)
│   │   └── ingest_crypto.py
│   │
│   ├── transformations/
│   │   ├── bronze.py
│   │   └── silver.py
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

## Fluxo da pipeline

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

### 6. Orquestração e Automação

O pipeline é executado automaticamente por meio de um **Job do Databricks**, simulando um fluxo mais próximo de um ambiente de produção real de engenharia de dados.

Durante a execução, o job percorre todas as etapas do pipeline:
- Ingestão
- Bronze
- Silver
- Gold
- Atualização do Dashboard

Quando a execução termina com sucesso:
- A camada **Gold** é atualizada  
- O **Dashboard do Databricks** é atualizado automaticamente  
- Um e-mail é enviado confirmando que o pipeline rodou corretamente  

Isso adiciona uma camada básica de automação e feedback operacional ao projeto, tornando o fluxo mais próximo do que é visto em pipelines reais de dados.

<img width="640" height="720" alt="image" src="https://github.com/user-attachments/assets/bc685e7f-df74-4dc1-9974-1198cf1e005d" />


---

## Arquitetura Medalhão

Para organizar melhor o fluxo dos dados, este projeto segue a arquitetura **Medalhão**, dividindo o pipeline em três camadas principais: **Bronze, Silver e Gold**.

Essa separação ajuda a manter os dados mais organizados, facilita o tratamento das informações e deixa o processo mais confiável ao longo das etapas.

### Bronze
Aqui ficam os **dados brutos** vindos diretamente da API, praticamente da forma como foram coletados.

Essa camada é importante para manter o histórico original dos dados e servir como base para as próximas transformações.

### Silver
Nesta etapa, os dados passam por **tratamentos e padronizações**.

É aqui que acontecem processos como:
- Ajuste para converter os tipos de dados
- Limpeza de colunas
- Remoção de duplicidades
- Aplicação de regras de qualidade

O objetivo dessa camada é garantir que os dados estejam **consistentes, confiáveis e bem estruturados**.

### Gold
Na camada Gold, os dados já estão **limpos e estruturados**, e passam a ser **transformados em métricas e indicadores analíticos**, prontos para serem consumidos em análises, métricas e dashboards.

É a camada mais próxima da visão de negócio, onde a informação já começa a fazer mais sentido para interpretação e tomada de decisão.

---

## Dicionários dos dados

Aqui vou descrever as principais colunas utilizadas ao longo das camadas Bronze, Silver e Gold do pipeline.

### Colunas Principais

| Coluna | Descrição |
|---|---|
| `crypto_code` | Código/símbolo da criptomoeda (ex: `BTC`, `ETH`, `SOL`). |
| `converted_code` | Moeda de conversão utilizada como referência (ex: `USD`). |
| `exchange_rate` | Valor de conversão de 1 unidade da criptomoeda para a moeda de destino no momento da coleta dos dados. |
| `bid_price` | Preço de compra do mercado, representando quanto o mercado está disposto a pagar pela criptomoeda. |
| `ask_price` | Preço de venda do mercado, representando quanto o mercado está cobrando pela criptomoeda. |
| `spread` | Diferença entre `ask_price` e `bid_price`, utilizada como indicador de liquidez e custo de transação. |
| `perc_change` | Variação percentual do preço da criptomoeda em relação ao valor de referência fornecido pela API. |
| `last_refreshed_date` | Data de referência da cotação retornada pela API. |
| `upload_date` | Data/hora em que o dado foi ingerido no Data Lake / Databricks. |

### Interpretação de Negócio

- **`exchange_rate`** é a principal métrica do dataset, representando o preço atual da criptomoeda.
- **`perc_change`** indica se o ativo valorizou ou desvalorizou em termos percentuais.
- **`spread`** representa a diferença entre preço de compra e venda, sendo um indicador importante de liquidez e custo de negociação.

---

## Data Quality Checks

Para aumentar a confiabilidade e simular um pipeline de dados mais próximo de um ambiente de produção, este projeto inclui validações de Data Quality tanto na camada Silver quanto na camada Gold.
O objetivo dessas verificações é garantir que os dados transformados permaneçam consistentes, válidos e confiáveis antes de serem consumidos pela camada analítica final.

### Como o Data Quality funciona

A lógica de Data Quality foi implementada por meio de funções de validação executadas durante o processo de transformação.
Essas verificações são acionadas automaticamente durante a execução das camadas Silver e Gold, antes que os dados finais sejam persistidos.

Se alguma validação falhar, o pipeline pode:
- Registrar o problema para fins de observabilidade
- Impedir que dados inválidos avancem para a próxima etapa
- Gerar um erro para interromper o job (dependendo da severidade da validação)

Isso ajuda a garantir que apenas dados limpos e prontos para análise cheguem à camada final consumida pelo dashboard.

### Exemplos atuais de validação

Validações da camada Silver: 
- Campos obrigatórios não podem ser nulos
- Valor da conversão (exchange_rate) não pode ser negativo
- Registros duplicados devem ser removidos
- Campos numéricos devem ser convertidos corretamente 

Exemplo:

<img width="800" height="600" alt="image" src="https://github.com/user-attachments/assets/afc8ccfb-3858-474d-93b6-ae126293b649" />


Validações da camada Gold: 
- Métricas agregadas não podem ser nulas
- O dataset analítico final deve estar pronto para consumo no dashboard
- O spread não pode ser negativo, pois o preço de venda no mercado não deveria ser menor que o preço de compra 

Exemplo:

<img width="800" height="600" alt="image" src="https://github.com/user-attachments/assets/7b19830e-3293-4d7e-8701-371476d54f9f" />


### Testes de falha e comportamento do pipeline

Para validar se as regras de Data Quality estavam funcionando corretamente, também foram realizados testes forçando erros de propósito nas camadas **Silver** e **Gold**.

A ideia desses testes foi simular cenários reais em que dados inválidos ou inconsistentes poderiam entrar no pipeline, garantindo que o processo reagisse da forma esperada.

Durante esses testes, o pipeline foi validado para:
- Identificar registros inválidos
- Interromper a execução quando necessário
- Registrar mensagens de erro nos logs
- Impedir que dados problemáticos avançassem para as próximas camadas
- Garantir que o dashboard só seja atualizado com dados válidos e prontos para análise

Esse tipo de validação ajuda a aumentar a confiabilidade do projeto e demonstra como o pipeline se comporta em cenários de falha, algo muito importante em ambientes reais de dados.

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
