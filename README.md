# Steam Analytics Dashboard

## 📌 Visão Geral

Este projeto implementa um pipeline de dados e dashboard para análise de métricas de jogos na plataforma Steam.

- Extração (`extract`): coleta de fonte de dados bruta (API, CSV etc.).
- Transformação (`transform`): limpeza, normalização e preparação dos dados.
- Carga (`load`): armazenamento final em formato pronto para dashboard.
- Dashboard (`dashboard/`): visualização interativa para insights exploratórios.

## 🚀 Tecnologias

- Python 3.8+.
- Pandas para manipulação de dados.
- Streamlit ou outra lib para dashboard (ajustar conforme implementação).
- Estrutura modular em `src/`:
  - `src/extract.py`
  - `src/transform.py`
  - `src/load.py`

## 🛠️ Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/steam-analytics-dashboard.git
   cd steam-analytics-dashboard
   ```

2. Crie e ative ambiente virtual:
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1   # Windows PowerShell
   # ou .\venv\Scripts\activate.bat # CMD
   ```

3. Instale dependências:
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Uso

### 1) Extração

- Adapte a fonte no `src/extract.py`.
- Execute:
  ```bash
  python src/extract.py
  ```

### 2) Transformação

- Ajuste regras de limpeza em `src/transform.py`.
- Execute:
  ```bash
  python src/transform.py
  ```

### 3) Carga

- Verifique destino em `src/load.py`.
- Execute:
  ```bash
  python src/load.py
  ```

### 4) Dashboard

Se estiver usando Streamlit:
```bash
streamlit run dashboard/app.py
```

## 📁 Estrutura de pastas

- `data/raw/`: dados brutos coletados.
- `data/processed/`: dados transformados prontos para análise.
- `src/`: scripts de ETL.
- `dashboard/`: código do painel visual.
- `notebooks/`: análises exploratórias e prototipagem.

## 🧾 Dados

Use dados do Steam (ex: API Web de dados de jogo, ou CSVs), com cuidado de limites de uso e conformidade com Termos de Serviço.

### Sugestão de fontes
- Steam Web API: `https://api.steampowered.com`
- Steamspy, Kaggle datasets de Steam.

## 🤝 Contribuição

1. Fork do projeto
2. Nova branch: `feature/minha-melhora`
3. Commit e PR com descrição clara
4. Testes e estilo de código

## 🧪 Testes

- Incluir testes automatizados (ex: `pytest`).
- Rodar:
  ```bash
  pytest
  ```

## 📜 Licença

MIT License (ou outra de sua preferência).
