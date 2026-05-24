# Log de Auditoria de Sinais (Oracle v2)

Este arquivo documenta as fontes brutas, timestamps e origens dos dados utilizados para alimentar os KPIs do Field of Meaning.

## Snapshot: NVIDIA (24/05/2026)

### 1. Sinais de Mídia e Narrativa (KPI 1, 2, 5)
- **Fonte**: Google News RSS / Agregadores de Notícias Financeiras.
- **Tópicos Extraídos**: "IA Soberana", "Blackwell Chips", "NVIDIA Q2 Guidance".
- **Origem dos Dados**:
  - *Reuters / Bloomberg*: Narrativas de dominância de mercado.
  - *Investing.com / Yahoo Finance*: Dados de sentimento de analistas.
- **Rastro de Auditoria**: `data/raw/signals_news_20260524.json`

### 2. Sinais Fantasmas e Deep Data (KPI 7)
- **Reddit (r/Nvidia / r/Hardware)**: Discussões sobre latência de entrega e performance real dos chips HBM3e.
- **Twitter/X (FinTwit)**: Monitoramento de "Order book imbalances" e fluxo de opções de grandes baleias.
- **USPTO (Patentes)**: Registro recente de arquiteturas de interconexão óptica (sinal de foco em infraestrutura de rede pós-GPU).
- **Rastro de Auditoria**: `data/raw/signals_phantom_20260524.json`

### 3. Realidade Mecânica (KPI 5 - Dissonância)
- **Fonte**: APIs de Mercado (Yahoo Finance / Alpha Vantage via scraping estático).
- **Métrica**: Comparativo Retorno Acumulado vs. Volume de Menções Sociais.
- **Rastro de Auditoria**: `data/raw/market_stats_20260524.json`

## Protocolo de Veracidade
Cada KPI no `processor.py` é derivado de pelo menos 3 fontes distintas para evitar viés de plataforma única.
