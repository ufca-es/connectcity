import os
import json
import unicodedata 
import random
import re
from .aprendizado import Aprendizado
from .historico import Historico

class ChatBot:
    def __init__(self, caminho_dados, historico):
        self.caminho_dados = caminho_dados
        self.base = self.carregar_dados()
        self.aprendizado = Aprendizado() 
        self.historico = historico

    def carregar_dados(self):
        try:
            with open(self.caminho_dados, 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)
                return dados
        except FileNotFoundError:
            print(f"Erro: O arquivo '{self.caminho_dados}' não foi encontrado.")
            return None

    def _normalizar_texto(self, texto):
        # Remove a pontuação e depois normaliza o texto
        texto_sem_pontuacao = re.sub(r'[^\w\s]', '', texto)
        texto_normalizado = unicodedata.normalize('NFD', texto_sem_pontuacao).encode('ascii', 'ignore').decode('utf-8')
        return texto_normalizado.lower().strip()
    
    def obter_personalidades_disponiveis(self):
        """
        Retorna uma lista de todas as personalidades disponíveis na base de dados.
        """
        personalidades = set()
        if self.base:
            for dados_resposta in self.base.values():
                for personalidade in dados_resposta.keys():
                    personalidades.add(personalidade)
        return list(personalidades)

    def obter_resposta(self, pergunta, personalidade):
        if self.base is None:
            return "Desculpe, não consigo carregar a base de dados."

        pergunta_formatada = self._normalizar_texto(pergunta)
        personalidade_formatada = self._normalizar_texto(personalidade)
        
        resposta_final = "Não sei responder isso ainda..."
        personalidade_usada = personalidade_formatada

        # 1. Procurar na base de dados fixa por correspondências
        for chave_pergunta, dados_resposta in self.base.items():
            chave_normalizada = self._normalizar_texto(chave_pergunta)
            palavras_chave = set(chave_normalizada.split())
            palavras_pergunta = set(pergunta_formatada.split())

            if not palavras_chave.isdisjoint(palavras_pergunta):
                # Se a personalidade escolhida existir, usa ela.
                if personalidade_formatada in dados_resposta:
                    respostas = dados_resposta[personalidade_formatada]
                    
                    if isinstance(respostas, str):
                        resposta_final = respostas
                    elif isinstance(respostas, list):
                        resposta_final = random.choice(respostas)
                else:
                    respostas = dados_resposta.get("formal") or list(dados_resposta.values())[0]
                    personalidade_usada = "formal (padrão)"

                    if isinstance(respostas, str):
                        resposta_final = respostas
                    elif isinstance(respostas, list):
                        resposta_final = random.choice(respostas)

                self.historico.adicionar("Usuário", pergunta)
                self.historico.adicionar("Bot", resposta_final, personalidade_usada)
                return resposta_final
        
        # 2. Procurar nos itens aprendidos
        for item in self.aprendizado.carregar():
            pergunta_aprendida_normalizada = self._normalizar_texto(item["pergunta"])
            personalidade_aprendida_normalizada = self._normalizar_texto(item["personalidade"])
            
            palavras_aprendidas = set(pergunta_aprendida_normalizada.split())
            palavras_pergunta = set(pergunta_formatada.split())

            if not palavras_aprendidas.isdisjoint(palavras_pergunta):
                if personalidade_aprendida_normalizada == personalidade_formatada:
                    resposta_final = item["resposta"]
                    self.historico.adicionar("Usuário", pergunta)
                    self.historico.adicionar("Bot", resposta_final, personalidade_usada)
                    return resposta_final
        
        # 3. Se não encontrou em nenhum lugar, pedir para aprender
        
        # Adiciona a pergunta do usuário e a resposta padrão no histórico antes de pedir para ensinar
        self.historico.adicionar("Usuário", pergunta)
        self.historico.adicionar("Bot", resposta_final, personalidade_usada)
        
        print(resposta_final)
        resposta_usuario = input("Me ensine a resposta: ")
        
        if "não sei" in resposta_usuario.lower() or "cancelar" in resposta_usuario.lower():
            resposta_final = "Então não sou capaz de te ajudar com isso. Sinto muito."
        else:
            self.aprendizado.salvar(pergunta, resposta_usuario, personalidade_formatada)
            resposta_final = "Entendido, vou me lembrar disso da próxima vez."
        
        # Adiciona a nova interação ao histórico (após o aprendizado)
        self.historico.adicionar("Usuário", pergunta)
        self.historico.adicionar("Bot", resposta_final, personalidade_usada)
        return resposta_final
