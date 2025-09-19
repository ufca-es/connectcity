import os
from .historico import Historico
from .estatisticas import Estatisticas
from .relatorio import Relatorio
from connectcity.config.configuracoes import CAMINHOS

class ReportGenerator:
    def __init__(self):
        self.historico_manager = Historico(CAMINHOS["historico"])
        self.estatisticas_manager = Estatisticas()
        self.relatorio_manager = Relatorio(CAMINHOS["relatorio"])

    def generate_full_report(self):
        print("Gerando relatório de uso...")
        # Coleta estatísticas do histórico
        estatisticas_data = self.estatisticas_manager.coletar_estatisticas(self.historico_manager)
        
        # Gera o relatório completo
        self.relatorio_manager.gerar_relatorio(self.historico_manager, estatisticas_data)
        print(f"Relatório gerado em: {self.relatorio_manager.caminho_relatorio}")


