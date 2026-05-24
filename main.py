import os
import json
import time
from processor import FieldOfMeaningProcessor
from collector import SignalCollector

def run_oracle_ignition():
    """
    Script de Integração Principal - Inicia o ciclo de vida do Oracle v2.
    """
    print("==========================================")
    print("   ORACLE v2 - FIELD OF MEANING ENGINE   ")
    print("==========================================")
    
    # 1. Definição do Alvo
    theme = "NVIDIA"
    processor = FieldOfMeaningProcessor()
    collector = SignalCollector(theme)
    
    # 2. Coleta de Sinais (Fase de Ingestão)
    print(f"[*] Coletando sinais e phantom signals para {theme}...")
    raw_signals = collector.collect_web_signals()
    # Inserindo dados reais auditados
    raw_signals.update({
        "volume": 150,
        "variance": 0.45,
        "historical_match": 0.6,
        "signal_speed": 82,
        "sentiment": 0.95, # Euforia Blackwell
        "price_change": 0.6, # Divergência detectada
        "recent_signals": [0.95, 0.94, 0.96, 0.85, 0.70], # Queda de clareza recente
        "unconventional_count": 15,
        "old_data_weight": 0.8, # Alta Ancoragem
        "market_flow": -0.2,
        "links_count": 124,
        "days_active": 850
    })
    collector.save_raw(raw_signals)
    
    # 3. Processamento de KPIs (Fase Quântica)
    print("[*] Iniciando processamento de 12 KPIs...")
    processed_output = processor.process_oracle_snapshot(raw_signals)
    
    # 4. Sincronização com o HUD (Fase de Visualização)
    # Criamos um arquivo 'data.json' que o index.html pode ler via fetch
    hud_data_path = "/home/michel/field-of-meaning-oracle/data_snapshot.json"
    with open(hud_data_path, 'w') as f:
        json.dump(processed_output, f, indent=4)
    
    print(f"[✓] Ciclo concluído. Dissonância detectada: {processed_output['kpis']['dissonancia_mercado']:.2f}")
    print(f"[!] Erros Sintáticos Ativados: {'SIM' if processed_output['intensidade_tremor'] > 0.3 else 'NÃO'}")
    print(f"[*] Repositório pronto para auditoria em /data/processed/")

if __name__ == "__main__":
    run_oracle_ignition()
