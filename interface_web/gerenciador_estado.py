import streamlit as st
from chatbot.chatbot import ChatBot
from chatbot.historico import Historico
from config.configuracoes import CAMINHOS

def inicializar_estado():
    """Inicializa o estado da aplicação"""
    if 'chatbot' not in st.session_state:
        historico = Historico(CAMINHOS["historico"])
        st.session_state.chatbot = ChatBot(CAMINHOS["dados"], historico)

    if 'historico_conversa' not in st.session_state:
        st.session_state.historico_conversa = []

    if 'modo_aprendizado' not in st.session_state:
        st.session_state.modo_aprendizado = False

    if 'pergunta_pendente' not in st.session_state:
        st.session_state.pergunta_pendente = ""

    if 'personalidade_pendente' not in st.session_state:
        st.session_state.personalidade_pendente = "formal"

    if 'ultima_pergunta' not in st.session_state:
        st.session_state.ultima_pergunta = ""

def obter_chatbot():
    """Retorna a instância do chatbot"""
    return st.session_state.chatbot

def definir_modo_aprendizado(pergunta, personalidade):
    """Define o modo de aprendizado"""
    st.session_state.modo_aprendizado = True
    st.session_state.pergunta_pendente = pergunta
    st.session_state.personalidade_pendente = personalidade

def limpar_modo_aprendizado():
    """Limpa o modo de aprendizado"""
    st.session_state.modo_aprendizado = False
    st.session_state.pergunta_pendente = ""
    st.session_state.personalidade_pendente = "formal"

def obter_pergunta_pendente():
    """Retorna a pergunta pendente"""
    return st.session_state.pergunta_pendente

def obter_personalidade_pendente():
    """Retorna a personalidade pendente"""
    return st.session_state.personalidade_pendente
