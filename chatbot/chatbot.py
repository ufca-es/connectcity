import os
import json

class ChatBot:
    def __init__(self, caminho_dados):
        self.caminho_dados = caminho_dados
        self.base = self.carregar_dados()

    def carregar_dados(self):
        try:
            with open(self.caminho_dados, 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)
                return dados
        except FileNotFoundError:
            print(f"Erro: O arquivo '{self.caminho_dados}' não foi encontrado.")
            return None

    def obter_resposta(self, pergunta, personalidade):
        if self.base is None:
            return "Desculpe, não consigo carregar a base de dados."

        pergunta_formatada = pergunta.lower()
        personalidade_formatada = personalidade.lower()
        
        if pergunta_formatada in self.base and personalidade_formatada in self.base[pergunta_formatada]:
            return self.base[pergunta_formatada][personalidade_formatada]
        else:
            return "Desculpe, não entendi sua pergunta."