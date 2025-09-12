import os
import json
from aprendizado import Aprendizado

class ChatBot:
    def __init__(self, caminho_dados):
        self.caminho_dados = caminho_dados
        self.base = self.carregar_dados()
        self.aprendizado = Aprendizado()

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
        
        for item in self.aprendizado.carregar():
            if (item["pergunta"].lower() == pergunta_formatada and item["personalidade"] == personalidade_formatada):
                return item["resposta"]
        
            else:
                print("Não sei responder isso ainda...")
                resposta = str(input("Me ensine a resposta: "))
                if ("não sei" == resposta or resposta == "cancelar"):
                    print('Então não sou capaz de te ajudar com isso. Sinto muito.')
                    break
                else: 
                    self.aprendizado.salvar(pergunta, resposta, personalidade_formatada)
                    return "Entendido, vou me lembrar disso da próxima vez."