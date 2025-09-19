import os
import json
import unicodedata
import random
import re
import logging
from functools import lru_cache
from .aprendizado import Aprendizado
from .historico import Historico

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ChatBot:
    """
    Classe principal do chatbot ConnectCity
    """

    def __init__(self, caminho_dados, historico):
        self.caminho_dados = caminho_dados
        self.base = self.carregar_dados()
        self.aprendizado = Aprendizado()
        self.historico = historico
        self._indice_busca = self._criar_indice_busca()

    def carregar_dados(self):
        """Carrega os dados da base de conhecimento"""
        try:
            with open(self.caminho_dados, 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)
                logger.info(f"Base de dados carregada com sucesso: {len(dados)} perguntas")
                return dados
        except FileNotFoundError:
            logger.error(f"Arquivo de dados não encontrado: {self.caminho_dados}")
            return None
        except json.JSONDecodeError as e:
            logger.error(f"Erro ao decodificar JSON: {e}")
            return None
        except Exception as e:
            logger.error(f"Erro inesperado ao carregar dados: {e}")
            return None

    @lru_cache(maxsize=512)
    def _normalizar_texto(self, texto):
        """Remove pontuação e acentos do texto (cacheado)"""
        texto_sem_pontuacao = re.sub(r'[^\w\s]', '', texto)
        texto_normalizado = unicodedata.normalize('NFD', texto_sem_pontuacao).encode('ascii', 'ignore').decode('utf-8')
        return texto_normalizado.lower().strip()

    def obter_personalidades_disponiveis(self):
        """Retorna lista de personalidades disponíveis"""
        personalidades = set()
        if self.base:
            for dados_resposta in self.base.values():
                for personalidade in dados_resposta.keys():
                    personalidades.add(personalidade)
        return list(personalidades)

    def _criar_indice_busca(self):
        """Cria índice otimizado para busca rápida"""
        indice = {}
        if self.base:
            for pergunta, dados_resposta in self.base.items():
                pergunta_normalizada = self._normalizar_texto(pergunta)
                palavras_chave = set(pergunta_normalizada.split())
                for palavra in palavras_chave:
                    if palavra not in indice:
                        indice[palavra] = []
                    indice[palavra].append((pergunta, dados_resposta))
        return indice

    def _buscar_na_base(self, pergunta_formatada, personalidade_formatada):
        """Busca resposta na base de dados principal usando índice otimizado"""
        palavras_pergunta = set(pergunta_formatada.split())
        candidatos = {}

        # Encontra candidatos usando índice
        for palavra in palavras_pergunta:
            if palavra in self._indice_busca:
                for pergunta, dados_resposta in self._indice_busca[palavra]:
                    # Usar pergunta como chave para evitar duplicatas
                    candidatos[pergunta] = dados_resposta

        # Avalia candidatos e encontra melhor match
        melhor_match = None
        melhor_score = 0

        for pergunta, dados_resposta in candidatos.items():
            pergunta_normalizada = self._normalizar_texto(pergunta)
            palavras_chave = set(pergunta_normalizada.split())

            # Calcula score baseado na interseção
            intersecao = palavras_chave.intersection(palavras_pergunta)
            score = len(intersecao) / len(palavras_chave)

            if score > melhor_score:
                melhor_score = score
                melhor_match = dados_resposta

        if melhor_match and melhor_score > 0.3:  # Threshold mínimo
            return self._obter_resposta_personalidade(melhor_match, personalidade_formatada)

        return None, None

    def _obter_resposta_personalidade(self, dados_resposta, personalidade_formatada):
        """Obtém resposta baseada na personalidade"""
        if personalidade_formatada in dados_resposta:
            respostas = dados_resposta[personalidade_formatada]
            personalidade_usada = personalidade_formatada
        else:
            respostas = dados_resposta.get("formal") or list(dados_resposta.values())[0]
            personalidade_usada = "formal (padrão)"

        if isinstance(respostas, str):
            return respostas, personalidade_usada
        elif isinstance(respostas, list):
            return random.choice(respostas), personalidade_usada

        return None, None

    def _buscar_aprendizado(self, pergunta_formatada, personalidade_formatada):
        """Busca resposta nos itens aprendidos (otimizado com cache)"""
        # Cache temporário para evitar recarregar arquivo múltiplas vezes
        if not hasattr(self, '_cache_aprendizado'):
            self._cache_aprendizado = self.aprendizado.carregar()
            self._cache_aprendizado_normalizado = [
                {
                    'pergunta': self._normalizar_texto(item["pergunta"]),
                    'personalidade': self._normalizar_texto(item["personalidade"]),
                    'resposta': item["resposta"]
                }
                for item in self._cache_aprendizado
            ]

        palavras_pergunta = set(pergunta_formatada.split())

        # Busca otimizada com cache
        for item in self._cache_aprendizado_normalizado:
            palavras_aprendidas = set(item['pergunta'].split())

            if not palavras_aprendidas.isdisjoint(palavras_pergunta):
                if item['personalidade'] == personalidade_formatada:
                    return item['resposta']

        return None

    def obter_resposta(self, pergunta, personalidade):
        """Método principal para obter resposta do chatbot"""
        if self.base is None:
            logger.warning("Tentativa de obter resposta com base de dados não carregada")
            return "Desculpe, não consigo carregar a base de dados."

        pergunta_formatada = self._normalizar_texto(pergunta)
        personalidade_formatada = self._normalizar_texto(personalidade)

        logger.debug(f"Buscando resposta para: '{pergunta}' com personalidade: '{personalidade}'")

        # Buscar na base de dados principal
        resposta_base, personalidade_usada = self._buscar_na_base(pergunta_formatada, personalidade_formatada)
        if resposta_base:
            logger.info(f"Resposta encontrada na base principal (personalidade: {personalidade_usada})")
            self.historico.adicionar("Usuário", pergunta)
            self.historico.adicionar("Bot", resposta_base, personalidade_usada)
            return resposta_base

        # Buscar nos aprendizados
        resposta_aprendizado = self._buscar_aprendizado(pergunta_formatada, personalidade_formatada)
        if resposta_aprendizado:
            logger.info("Resposta encontrada nos aprendizados")
            self.historico.adicionar("Usuário", pergunta)
            self.historico.adicionar("Bot", resposta_aprendizado, personalidade_formatada)
            return resposta_aprendizado

        # Não encontrou resposta
        logger.info("Nenhuma resposta encontrada, iniciando aprendizado")
        return self._processar_aprendizado(pergunta, personalidade_formatada)

    def _processar_aprendizado(self, pergunta, personalidade_formatada):
        """Processa o aprendizado de novas respostas (versão web)"""
        resposta_padrao = "Não sei responder isso ainda..."
        self.historico.adicionar("Usuário", pergunta)
        self.historico.adicionar("Bot", resposta_padrao, personalidade_formatada)
        return resposta_padrao

    def ensinar_resposta(self, pergunta, resposta_usuario, personalidade):
        """Ensina uma nova resposta ao chatbot"""
        personalidade_formatada = self._normalizar_texto(personalidade)

        if any(termo in resposta_usuario.lower() for termo in ["não sei", "cancelar", "nao sei"]):
            logger.info(f"Usuário cancelou aprendizado para pergunta: '{pergunta}'")
            return "Então não sou capaz de te ajudar com isso. Sinto muito."
        else:
            try:
                self.aprendizado.salvar(pergunta, resposta_usuario, personalidade_formatada)
                # Limpar cache de aprendizado para incluir nova resposta
                if hasattr(self, '_cache_aprendizado'):
                    delattr(self, '_cache_aprendizado')
                logger.info(f"Nova resposta aprendida: '{pergunta}' -> '{resposta_usuario}'")
                return "Entendido, vou me lembrar disso da próxima vez."
            except Exception as e:
                logger.error(f"Erro ao salvar aprendizado: {e}")
                return "Desculpe, houve um erro ao salvar sua resposta."
