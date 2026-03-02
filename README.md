# Pipeline de Investimentos – Alpha Vantage

Projeto pessoal de engenharia de dados para estudo e prática de ingestão, armazenamento, transformação e análise de dados financeiros.  
A aplicação consome dados da **Alpha Vantage**, salva localmente em um *data lake* estruturado e futuramente será integrada ao **Databricks**, Airflow e CI/CD.

---

## 📊 Arquitetura do Projeto

O diagrama abaixo representa a arquitetura completa (presente + futura) do pipeline, incluindo ingestão, armazenamento e transformação:

> **API → Python → Data Lake RAW → Bronze → Silver → Gold → Dashboards / Análises**

---

## 🧠 Objetivo do Projeto

Criar um pipeline realista de engenharia de dados que:

- Conecta em APIs de dados financeiros (cripto, ações, câmbio)
- Extrai e armazena dados brutos no *data lake local*
- Constrói camadas Bronze, Silver e Gold no Databricks
- Evolui para ter Airflow e CI/CD futuramente
- Aplica boas práticas reais de engenharia: versionamento, modularização, logs, estrutura de pastas e ambientes

Este projeto serve tanto para **aprendizado** quanto para **portfólio profissional**.

---

## 📁 Estrutura do Projeto

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

## 🔌 Tecnologias Utilizadas

- **Python**
- **Requests** (requisições HTTP)
- **JSON** (armazenamento bruto)
- **Pathlib** (manipulação de arquivos e diretórios)
- **Datetime** (timestamp dos arquivos)
- **Git/GitHub** (versionamento e PRs)
- **Databricks Community Edition** *(update futuro – Bronze/Silver/Gold)*
- **Apache Spark / PySpark** *(update futuro)*
- **Airflow** *(update futuro)*

---

## 🚀 Funcionalidade Atual

Atualmente o projeto:

1. Conecta na API da Alpha Vantage  
2. Extrai o câmbio de criptomoeda → USD  
3. Gera um arquivo JSON contendo a resposta  
4. Salva no caminho: data_lake/raw/<CRIPTO>/<AAAA-MM-DD>.json
5. Mantém histórico de execuções diárias
  Exemplo real: data_lake/raw/BTC/2024-02-29.json

---

## ▶️ Como Rodar o Projeto

### 1. Clone o repositório

git clone https://github.com/GabsPerry/pipeline-investimentos-alpha-vantage.git

cd pipeline-investimentos-alpha-vantage

### 2. Instale as dependências

pip install -r requirements.txt

### 3. Adicione sua API key no script

Você pode obter uma chave gratuita em:
https://www.alphavantage.co/support/#api-key

### 4. Execute o script de ingestão
python src/ingestao/ingest_crypto.py

--- 

## 📌 Sobre o Autor

Projeto desenvolvido por Gabriel Perillo, engenheiro de dados aprendendo arquitetura moderna, pipelines eficientes e boas práticas de software para construir soluções reais de dados.

--- 

## 📄 Licença

Este projeto está sob a licença MIT.
