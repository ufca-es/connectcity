import os
from .historico import Historico
from .estatisticas import Estatisticas

class Relatorio:
    """
    Gera um relatório formatado das interações salvas no histórico.
    """
    def __init__(self, caminho_relatorio="data/relatorio.txt"):
        """
        Inicializa o gerador de relatório com o caminho do arquivo de saída.
        """
        self.caminho_relatorio = caminho_relatorio

    def gerar_relatorio(self, historico, estatisticas_data):
        """
        Gera um relatório legível a partir do histórico de interações e estatísticas.
        
        Args:
            historico (Historico): Uma instância da classe Historico.
            estatisticas_data (dict): Dicionário com dados estatísticos.
        """
        interacoes = historico.carregar()

        with open(self.caminho_relatorio, "w", encoding="utf-8") as f:
            f.write("### Relatório de Interações do Chatbot ###\n")
            f.write("=======================================\n\n")

            # Escreve a seção de estatísticas
            f.write("--- Estatísticas Gerais ---\n")
            f.write(f"Total de Interações: {estatisticas_data['total_interacoes']}\n")
            f.write(f"Pergunta mais feita: \"{estatisticas_data['pergunta_mais_feita']['pergunta']}\" (feita {estatisticas_data['pergunta_mais_feita']['contagem']} vezes)\n")
            f.write(f"Personalidade mais usada: {estatisticas_data['personalidade_mais_usada'].capitalize()}\n")
            f.write(f"Perguntas não respondidas: {estatisticas_data['total_perguntas_nao_respondidas']}\n")
            f.write("\nDetalhes por Personalidade:\n")
            for pers, contagem in estatisticas_data['detalhes_personalidades'].items():
                f.write(f"- {pers.capitalize()}: {contagem} interações\n")
            f.write("-" * 20 + "\n\n")
            
            # Escreve a seção de interações
            f.write("--- Histórico Completo das Interações ---\n")
            if not interacoes:
                f.write("Nenhuma interação registrada nesta sessão.\n")
                return

            for i, interacao in enumerate(interacoes):
                f.write(f"Interação {i + 1}:\n")
                f.write(f"  Usuário: {interacao['pergunta']}\n")
                f.write(f"  Bot: {interacao['resposta']}\n")
                f.write(f"  Personalidade: {interacao['personalidade']}\n")
                f.write("\n")
