# 🚀 Pipeline de Dados End-to-End com Python, SQL e PostgreSQL

## 📌 Visão Geral

Este projeto implementa um pipeline de dados completo (ETL) com o objetivo de coletar, transformar e disponibilizar dados para análise de forma estruturada e escalável.

A solução simula um cenário real de engenharia de dados, onde informações são extraídas de uma fonte externa, tratadas e armazenadas em um banco relacional para consumo analítico.

---

## 🎯 Problema

Empresas lidam diariamente com grandes volumes de dados provenientes de múltiplas fontes. Sem um processo estruturado, esses dados tornam-se inconsistentes, difíceis de analisar e pouco confiáveis para tomada de decisão.

Este projeto resolve esse problema ao criar um fluxo automatizado de tratamento e organização de dados.

---

## 💡 Solução

Foi desenvolvido um pipeline ETL dividido em três etapas principais:

* **Extract:** Coleta de dados via API ou arquivo CSV
* **Transform:** Limpeza, padronização e enriquecimento dos dados
* **Load:** Armazenamento em banco de dados PostgreSQL e arquivo estruturado

---

## 🧱 Arquitetura

```id="arch1"
[ Fonte de Dados ]
       ↓
   Extract (Python)
       ↓
 Transform (Pandas)
       ↓
 Load (PostgreSQL + CSV)
       ↓
 Consumo (BI / Análises)
```

---

## 📂 Estrutura do Projeto

```id="struct1"
data-pipeline-project/
│
├── data/
│   ├── raw/                # Dados brutos
│   ├── processed/          # Dados tratados
│
├── src/
│   ├── extract.py          # Extração de dados
│   ├── transform.py        # Transformação
│   ├── load.py             # Persistência
│   ├── main.py             # Orquestração do pipeline
│
├── config.py               # Configurações gerais
├── requirements.txt        # Dependências
└── README.md               # Documentação
```

---

## ⚙️ Tecnologias Utilizadas

* Python
* Pandas
* SQLAlchemy
* PostgreSQL
* Requests

---

## 🔄 Fluxo do Pipeline

1. Os dados são coletados via API pública ou arquivo CSV
2. O dataset passa por limpeza e tratamento de inconsistências
3. Novas features são criadas para enriquecer a análise
4. Os dados são armazenados em:

   * Arquivo CSV (camada processada)
   * Banco PostgreSQL (camada estruturada)

---

## ▶️ Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/ed349ti/Data-pipeline-project.git
cd data-pipeline-project
```

---

### 2. Crie o ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

---

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

### 4. Configure o banco de dados

Edite o arquivo `config.py` com suas credenciais do PostgreSQL.

---

### 5. Execute o pipeline

```bash
python src/main.py
```

---

## 📊 Resultados

* Dados estruturados e prontos para análise
* Redução de inconsistências no dataset
* Pipeline reutilizável para diferentes fontes de dados
* Base pronta para integração com ferramentas de BI

---

## 🧠 Decisões Técnicas

* **Separação por camadas (Extract, Transform, Load):** melhora a manutenção e escalabilidade
* **Uso de PostgreSQL:** amplamente utilizado em ambientes corporativos
* **Pandas para transformação:** eficiência no tratamento de dados tabulares
* **Config centralizada:** facilita adaptação para outros ambientes

---

## 🚧 Melhorias Futuras

* Containerização com Docker
* Orquestração com Airflow
* Implementação de logs estruturados
* Testes automatizados
* Integração com ferramentas de visualização (Power BI / Streamlit)

---

## 👨‍💻 Sobre

Projeto desenvolvido com foco em consolidar conhecimentos em Engenharia de Dados, incluindo práticas de ETL, organização de código e estruturação de pipelines.

---

## 📬 Contato

* LinkedIn: https://www.linkedin.com/in/ed349ti/
* GitHub: ed349ti

---
