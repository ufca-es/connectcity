import os

class Historico:
    def __init__(self, caminho_arquivo="data/historico.txt"):
        self.caminho_arquivo = caminho_arquivo
        if not os.path.exists(self.caminho_arquivo):
            with open(self.caminho_arquivo, "w", encoding="utf-8") as f:
                f.write("=== Histórico de Conversas ===\n")

    def adicionar(self, remetente, mensagem):
        """Adiciona uma linha no histórico"""
        with open(self.caminho_arquivo, "a", encoding="utf-8") as f:
            f.write(f"{remetente}: {mensagem}\n")

    def ultimas_interacoes(self, n=5):
        """Retorna as últimas N interações"""
        try:
            with open(self.caminho_arquivo, "r", encoding="utf-8") as f:
                linhas = f.readlines()
            return [linha.strip() for linha in linhas[-n:]]
        except FileNotFoundError:
            return []