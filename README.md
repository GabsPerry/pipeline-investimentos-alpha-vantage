## Investimentos – Alpha Vantage

Projeto pessoal de engenharia de dados para estudo e prática de ingestão, armazenamento, transformação e análise de dados financeiros.  
A aplicação consome dados da **Alpha Vantage**, salva em um *data lake* (volume) integrado ao **Databricks**, e CI/CD.

---

## Arquitetura do Projeto

O diagrama abaixo representa a arquitetura completa (presente + futura) do pipeline, incluindo ingestão, armazenamento e transformação:

> **API → Python → Data Lake RAW → Bronze → Silver → Gold → Dashboards / Análises**

Job no Databricks:
<img width="1604" height="516" alt="image" src="https://github.com/user-attachments/assets/376f4283-28d5-4aa6-9180-1712775eef5a" />

---

## Objetivo do Projeto

Criar um pipeline realista de engenharia de dados que:

- Conecta em APIs de dados financeiros (cripto, ações, câmbio)
- Extrai e armazena dados brutos no data lake do Databricks (volumes)
- Constrói camadas Bronze, Silver e Gold no Databricks
- Aplica boas práticas reais de engenharia: versionamento, modularização, logs, data quality, estrutura de pastas e ambientes

---

## Estrutura do Projeto

```
pipeline-investimentos-alpha-vantage/
│
├── src/
│ └── ingestao/
│ └── ingest_crypto.py # Script atual de ingestão (versão simples)
│
├── data_lake/
│ ├── raw/ # Dados brutos extraídos da API
│ ├── silver/ # (futuro) Dados limpos e normalizados
│ └── gold/ # (futuro) Dados prontos para análise
│
├── .gitignore
└── README.md
```

---

## Tecnologias Utilizadas

- **Python**
- **Requests** (requisições HTTP)
- **JSON** (armazenamento bruto)
- **Pathlib** (manipulação de arquivos e diretórios)
- **Datetime** (timestamp dos arquivos)
- **Git/GitHub** (versionamento e PRs)
- **Databricks Community Edition** (tabelas Bronze/Silver/Gold, armazenamento em volumes e orquestração do job)*
- **Apache Spark / PySpark** 

---

## Funcionalidade Atual

Atualmente o projeto:

1. Conecta na API da Alpha Vantage  
2. Extrai o câmbio de criptomoeda → USD  
3. Gera um arquivo JSON contendo a resposta  
4. Salva no caminho: data_lake/raw/<CRIPTO>/<AAAA-MM-DD>.json
5. Mantém histórico de execuções diárias
  Exemplo real: data_lake/raw/BTC/2024-02-29.json

--- 

## Licença

Este projeto está sob a licença MIT.
