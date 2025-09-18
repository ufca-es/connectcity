import os
import json

class Historico:
    """
    Gerencia o histórico de conversas do chatbot.
    """
    def __init__(self, caminho_arquivo="data/historico.txt"):
        self.caminho_arquivo = caminho_arquivo
        # Garante que o diretório 'data' exista
        os.makedirs(os.path.dirname(self.caminho_arquivo), exist_ok=True)
        if not os.path.exists(self.caminho_arquivo):
            with open(self.caminho_arquivo, "w", encoding="utf-8") as f:
                f.write("=== Histórico de Conversas ===\n")

    def adicionar(self, remetente, mensagem, personalidade=None):
        """Adiciona uma linha no histórico com a personalidade."""
        with open(self.caminho_arquivo, "a", encoding="utf-8") as f:
            if personalidade:
                f.write(f"{remetente}: {mensagem} | Personalidade: {personalidade}\n")
            else:
                f.write(f"{remetente}: {mensagem}\n")

    def carregar(self):
        """Carrega o histórico de conversas do arquivo e o retorna como uma lista de objetos."""
        interacoes = []
        try:
            with open(self.caminho_arquivo, "r", encoding="utf-8") as f:
                linhas = f.readlines()
            
            # Ignora a primeira linha do cabeçalho
            linhas = [linha.strip() for linha in linhas if not linha.startswith("===")]
            
            # Percorre o histórico em pares de pergunta e resposta
            for i in range(0, len(linhas), 2):
                if i + 1 < len(linhas):
                    pergunta_linha = linhas[i]
                    resposta_linha = linhas[i+1]
                    
                    # Parseia a pergunta do usuário
                    pergunta = pergunta_linha.split(': ', 1)[1] if ': ' in pergunta_linha else ""
                    
                    # Parseia a resposta do bot e a personalidade
                    personalidade_partes = resposta_linha.split(' | Personalidade: ')
                    resposta = personalidade_partes[0].split(': ', 1)[1] if ': ' in personalidade_partes[0] else ""
                    personalidade = personalidade_partes[1] if len(personalidade_partes) > 1 else "Desconhecida"

                    interacoes.append({
                        "pergunta": pergunta,
                        "resposta": resposta,
                        "personalidade": personalidade
                    })
        except FileNotFoundError:
            return []
        return interacoes
        
    def ultimas_interacoes(self, n=5):
        """Retorna as últimas N interações."""
        try:
            with open(self.caminho_arquivo, "r", encoding="utf-8") as f:
                linhas = f.readlines()
            # Ignora o cabeçalho se houver
            inicio_conteudo = 1 if linhas and linhas[0].startswith("===") else 0
            
            return [linha.strip() for linha in linhas[inicio_conteudo:][-n*2:]]
        except FileNotFoundError:
            return []