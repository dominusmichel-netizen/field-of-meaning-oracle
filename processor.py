import numpy as np
import pandas as pd
from typing import List, Dict
import json
import os
from datetime import datetime

class FieldOfMeaningProcessor:
    """
    Motor Central do Projeto Field of Meaning (Oracle v2).
    Responsável por transformar sinais brutos em coordenadas topológicas e 12 KPIs de monitoramento.
    """
    
    def __init__(self, project_root: str = "/home/michel/field-of-meaning-oracle"):
        self.root = project_root
        self.data_path = os.path.join(self.root, "data/processed")
        os.makedirs(self.data_path, exist_ok=True)
        
    def calculate_dissonance(self, sentiment_score: float, market_performance: float) -> float:
        """
        Calcula o Índice de Dissonância (KPI 5).
        Gap entre a narrativa (sentimento) e a realidade mecânica (performance).
        """
        # Normalizando ambos para escala 0-1 e calculando a diferença absoluta
        return abs(sentiment_score - market_performance)

    def calculate_entropy(self, signal_volatility: List[float]) -> float:
        """
        Calcula a Entropia Semântica (KPI 10).
        Mede a desordem ou dispersão dos sinais.
        """
        if not signal_volatility:
            return 0.0
        probabilities = np.histogram(signal_volatility, bins=10, density=True)[0]
        probabilities = probabilities / probabilities.sum() if probabilities.sum() > 0 else probabilities
        # Shannon Entropy
        return -np.sum([p * np.log2(p) for p in probabilities if p > 0])

    def process_oracle_snapshot(self, raw_data: Dict) -> Dict:
        """
        Transforma um snapshot de dados brutos na matriz de performance HUD.
        """
        # Exemplo de lógica de mapeamento para os 12 KPIs
        kpis = {
            "centralidade_semantica": raw_data.get("volume", 0) * 0.7,
            "consenso_narrativo": 1.0 - raw_data.get("variance", 0),
            "indice_coerencia": raw_data.get("historical_match", 0.5),
            "momentum_throughput": raw_data.get("signal_speed", 0),
            "dissonancia_mercado": self.calculate_dissonance(
                raw_data.get("sentiment", 0.5), 
                raw_data.get("price_change", 0.5)
            ),
            "volatilidade_sentimento": np.std(raw_data.get("recent_signals", [0])),
            "sinais_fantasmas": raw_data.get("unconventional_count", 0),
            "indicador_ancoragem": raw_data.get("old_data_weight", 0),
            "pressao_direcional": raw_data.get("market_flow", 0),
            "entropia_campo": self.calculate_entropy(raw_data.get("recent_signals", [])),
            "densidade_conexoes": raw_data.get("links_count", 0),
            "taxa_sobrevivencia_lindy": raw_data.get("days_active", 1) / 365
        }
        
        output = {
            "timestamp": datetime.now().isoformat(),
            "kpis": kpis,
            "morfologia_sugerida": "hedgehog" if kpis["entropia_campo"] > 0.7 else "sphere",
            "intensidade_tremor": kpis["dissonancia_mercado"]
        }
        
        # Salva o resultado
        filename = f"snapshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(os.path.join(self.data_path, filename), 'w') as f:
            json.dump(output, f, indent=4)
            
        return output

if __name__ == "__main__":
    processor = FieldOfMeaningProcessor()
    # Mock de teste para validação da estrutura
    test_data = {
        "volume": 100,
        "variance": 0.2,
        "historical_match": 0.8,
        "signal_speed": 45,
        "sentiment": 0.9, # Super otimista
        "price_change": 0.4, # Mercado não acompanhou (Dissonância!)
        "recent_signals": [0.9, 0.85, 0.92, 0.88],
        "unconventional_count": 12,
        "old_data_weight": 0.3,
        "market_flow": -0.5,
        "links_count": 50,
        "days_active": 730
    }
    result = processor.process_oracle_snapshot(test_data)
    print(f"Processamento concluído. Morfologia: {result['morfologia_sugerida']}")
    print(f"Dissonância Detectada: {result['kpis']['dissonancia_mercado']:.2f}")
