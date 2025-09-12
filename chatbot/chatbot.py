import os
import json
import unicodedata 
from .aprendizado import Aprendizado

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

    def _normalizar_texto(self, texto):

        texto_normalizado = unicodedata.normalize('NFD', texto).encode('ascii', 'ignore').decode('utf-8')
        return texto_normalizado.lower()

    def obter_resposta(self, pergunta, personalidade):
        if self.base is None:
            return "Desculpe, não consigo carregar a base de dados."

        pergunta_formatada = self._normalizar_texto(pergunta)
        personalidade_formatada = self._normalizar_texto(personalidade)
        
        # 1. Procurar na base de dados fixa por correspondências
        for chave_pergunta in self.base:
            chave_normalizada = self._normalizar_texto(chave_pergunta)
            if all(palavra in chave_normalizada for palavra in pergunta_formatada.split()):
                if personalidade_formatada in self.base[chave_pergunta]:
                    return self.base[chave_pergunta][personalidade_formatada]
        
        # 2. Procurar nos itens aprendidos
        for item in self.aprendizado.carregar():
            pergunta_aprendida_normalizada = self._normalizar_texto(item["pergunta"])
            personalidade_aprendida_normalizada = self._normalizar_texto(item["personalidade"])

            # Agora busca por palavras-chave em vez de correspondência exata
            if all(palavra in pergunta_aprendida_normalizada for palavra in pergunta_formatada.split()):
                if personalidade_aprendida_normalizada == personalidade_formatada:
                    return item["resposta"]
        
        # 3. Se não encontrou em nenhum lugar, pedir para aprender
        print("Não sei responder isso ainda...")
        resposta_usuario = input("Me ensine a resposta: ")
        
        if "não sei" in resposta_usuario.lower() or "cancelar" in resposta_usuario.lower():
            return "Então não sou capaz de te ajudar com isso. Sinto muito."
        else:
            self.aprendizado.salvar(pergunta, resposta_usuario, personalidade_formatada)
            return "Entendido, vou me lembrar disso da próxima vez."