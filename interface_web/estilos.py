import streamlit as st
from config.configuracoes import INTERFACE

def configurar_pagina():
    """Configura a página do Streamlit"""
    st.set_page_config(
        page_title=INTERFACE["titulo"],
        page_icon="🏙️",
        layout="wide",
        initial_sidebar_state="expanded"
    )

def aplicar_css():
    """Aplica CSS customizado para melhorar a aparência"""
    st.markdown("""
    <style>
    .main {
        padding-top: 2rem;
    }

    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 0.5rem 1rem;
        font-weight: bold;
        transition: all 0.3s ease;
        min-height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        white-space: nowrap;
    }

    .stButton > button:hover {
        background-color: #45a049;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }

    /* Estilos específicos para botões em sidebar */
    .sidebar .stButton > button {
        margin: 0.5rem 0;
        width: 100% !important;
    }

    /* Melhor alinhamento para botões em formulários */
    .stForm .stButton > button {
        width: 100%;
        margin: 0.25rem 0;
    }

    /* Alinhamento vertical para botões em colunas */
    .stColumns .stButton > button {
        height: 100%;
        display: flex;
        align-items: center;
    }

    /* Estilo específico para a área de entrada */
    .stForm .stColumns {
        align-items: flex-end;
        gap: 0.5rem;
    }

    .stForm .stColumns > div:first-child {
        padding-right: 0.25rem;
    }

    .stForm .stColumns > div:last-child {
        padding-left: 0.25rem;
        display: flex;
        align-items: flex-end;
    }

    /* Alinhamento específico para o botão de envio */
    .stForm .stButton {
        margin: 0;
        padding: 0;
    }

    .stForm .stButton > button {
        height: 40px;
        min-height: 40px;
        margin: 0;
        padding: 0.5rem 1rem;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    /* Garantir que o campo de entrada tenha a mesma altura do botão */
    .stForm .stTextInput > div > div > input {
        height: 40px;
        min-height: 40px;
        padding: 0.5rem 1rem;
        box-sizing: border-box;
    }

    .chat-message {
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 10px;
        max-width: 80%;
        border: 1px solid;
    }

    /* Estilos para modo claro */
    @media (prefers-color-scheme: light) {
        .user-message {
            background-color: #e3f2fd;
            color: #1565c0;
            border-color: #bbdefb;
            margin-left: auto;
            text-align: right;
        }

        .bot-message {
            background-color: #f5f5f5;
            color: #424242;
            border-color: #e0e0e0;
            margin-right: auto;
        }
    }

    /* Estilos para modo escuro */
    @media (prefers-color-scheme: dark) {
        .user-message {
            background-color: #1e3a5f;
            color: #bbdefb;
            border-color: #3949ab;
            margin-left: auto;
            text-align: right;
        }

        .bot-message {
            background-color: #2d2d2d;
            color: #ffffff;
            border-color: #424242;
            margin-right: auto;
        }
    }

    .sidebar .stSelectbox {
        margin-bottom: 1rem;
    }

    .titulo-principal {
        text-align: center;
        color: #2E7D32;
        margin-bottom: 1rem;
    }

    .subtitulo {
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }

    @media (max-width: 768px) {
        .main {
            padding: 1rem;
        }

        .chat-message {
            max-width: 95%;
        }
    }
    </style>
    """, unsafe_allow_html=True)

def exibir_cabecalho():
    """Exibe o cabeçalho da aplicação"""
    st.markdown(f"""
    <h1 class="titulo-principal">{INTERFACE["titulo"]}</h1>
    <p class="subtitulo">{INTERFACE["subtitulo"]}</p>
    """, unsafe_allow_html=True)
