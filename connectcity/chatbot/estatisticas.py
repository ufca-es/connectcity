import os
import re
import unicodedata
from collections import Counter

class Estatisticas:
    """
    Coleta e calcula estatísticas a partir do histórico de interações.
    """
    def _normalizar_texto(self, texto):
        """Normaliza o texto para remover pontuação, acentos e espaços extras."""
        texto_sem_pontuacao = re.sub(r'[^\w\s]', '', texto)
        texto_normalizado = unicodedata.normalize('NFD', texto_sem_pontuacao).encode('ascii', 'ignore').decode('utf-8')
        return texto_normalizado.lower().strip()

    def coletar_estatisticas(self, historico):
        """
        Analisa o histórico e retorna um dicionário com estatísticas.
        
        Args:
            historico (Historico): Uma instância da classe Historico.
        
        Returns:
            dict: Um dicionário contendo as estatísticas coletadas.
        """
        interacoes = historico.carregar()
        
        total_interacoes = len(interacoes)
        
        perguntas_normalizadas = [self._normalizar_texto(item['pergunta']) for item in interacoes if 'pergunta' in item]
        perguntas_contagem = Counter(perguntas_normalizadas)
        
        pergunta_mais_feita = perguntas_contagem.most_common(1)[0] if perguntas_contagem else ("Nenhuma", 0)
        
        personalidades_contagem = Counter(item['personalidade'] for item in interacoes if 'personalidade' in item)
        
        perguntas_nao_respondidas = sum(1 for item in interacoes if "não sei responder isso ainda" in item['resposta'].lower())
        
        return {
            "total_interacoes": total_interacoes,
            "pergunta_mais_feita": {
                "pergunta": pergunta_mais_feita[0],
                "contagem": pergunta_mais_feita[1]
            },
            "personalidade_mais_usada": personalidades_contagem.most_common(1)[0][0] if personalidades_contagem else "Nenhuma",
            "total_perguntas_nao_respondidas": perguntas_nao_respondidas,
            "detalhes_personalidades": dict(personalidades_contagem)
        }
