# 🚀 SSA-Fintech Intelligence Pipeline

![Python](https://img.shields.io/badge/python-3.11+-blue.svg?style=for-the-badge&logo=python)
![SQL](https://img.shields.io/badge/SQL-Avan%C3%A7ado-orange.svg?style=for-the-badge&logo=postgresql)
![Architecture](https://img.shields.io/badge/Arquitetura-Medallion-green.svg?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Em%20Andamento-orange?style=for-the-badge)

<p align="center">
  <b>Read in English:</b> <a href="README.md">🇺🇸 English</a>
</p>

Um pipeline de engenharia de dados de alta performance projetado para avaliação de risco de crédito em tempo real e detecção de anomalias, calibrado especificamente para a região metropolitana de **Salvador, BA, Brasil**.

## 📌 Visão Geral do Projeto

Este projeto simula a infraestrutura de dados de uma fintech, realizando ingestão de transações, pontuação de risco e geração automatizada de relatórios. Utiliza a **Arquitetura Medallion** para garantir qualidade dos dados e escalabilidade, progredindo de eventos brutos até insights de negócio prontos para executivos.

## 🏗️ Arquitetura de Dados (Padrão Medallion)

1. **Camada Bronze (Raw):** Ingestão assíncrona de dados de transações utilizando `Python Asyncio` e `Faker`.
2. **Camada Silver (Trusted):** Limpeza de dados e transformações complexas utilizando **Window Functions SQL** (LAG/LEAD) para detectar saltos de localização e padrões suspeitos.
3. **Camada Gold (Business):** Lógica de negócio final e pontuação de risco, entregue via **Google Sheets API** para os stakeholders.

## 🛠️ Stack Tecnológico

- **Linguagem:** Python 3.11+ (foco em `asyncio`, `pandas`, `pytest`)
- **Banco de Dados:** SQLite (Armazenamento Relacional)
- **Análise:** SQL (Window Functions, CTEs)
- **Automação:** Google Sheets API (`gspread`)
- **Visualização:** Looker Studio (Dashboard Executivo)

## 📈 Principais Recursos de Engenharia

- **Simulação em Tempo Real:** Geração assíncrona de 1.000+ transações simultâneas.
- **Detecção de Anomalias:** Lógica baseada em SQL para identificar operações de alto risco entre bairros distantes em curtos intervalos de tempo.
- **Pipeline Automatizado:** Processo ETL completo, desde CSV bruto até dashboards de BI na nuvem.

## 🗺️ Roadmap (Próximos Commits)

- [x] Arquitetura inicial e documentação
- [ ] Motor de ingestão de dados assíncrono (Bronze)
- [ ] Transformações SQL e lógica de risco (Silver)
- [ ] Integração com API e automação (Gold)
- [ ] Dashboard final e testes unitários (QA)