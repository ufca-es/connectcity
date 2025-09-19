import streamlit as st
import sys
import os

# Adiciona o diretório raiz ao path para importações
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from interface_web import interface
from interface_web import gerenciador_estado
from interface_web import estilos

def main():
    """Função principal da aplicação"""
    # Configurações iniciais
    estilos.configurar_pagina()
    estilos.aplicar_css()
    gerenciador_estado.inicializar_estado()

    # Interface principal
    estilos.exibir_cabecalho()

    # Sidebar com configurações
    personalidade = interface.criar_sidebar()

    # Container principal para o chat
    chat_container = st.container()

    with chat_container:
        # Exibe histórico de conversas
        interface.exibir_historico()

        # Verifica se está no modo aprendizado
        resposta_aprendizado = interface.exibir_modo_aprendizado()

        # Processa a resposta do modo aprendizado, se houver
        if resposta_aprendizado:
            processar_aprendizado(resposta_aprendizado, personalidade)
            st.rerun() # Recarrega para limpar o form de aprendizado e mostrar o resultado

    # Área de entrada do usuário
    st.markdown("---")

    # Form para entrada de texto
    with st.form(key="pergunta_form", clear_on_submit=True):
        col1, col2 = st.columns([5, 1])

        with col1:
            pergunta = st.text_input(
                "Digite sua pergunta:",
                placeholder="Digite sua pergunta sobre Juazeiro do Norte...",
                key="pergunta_input",
                label_visibility="collapsed"
            )

        with col2:
            enviar = st.form_submit_button(
                "📤 Enviar",
                type="primary",
                use_container_width=True
            )

        # Se o formulário foi enviado com uma pergunta válida
        if enviar and pergunta.strip():
            # Processa a pergunta imediatamente
            processar_pergunta(pergunta, personalidade)
            # Força um recarregamento para exibir a nova conversa na tela
            st.rerun()


def processar_pergunta(pergunta, personalidade):
    """Processa a pergunta do usuário"""
    # Adiciona pergunta ao histórico visual
    interface.adicionar_ao_historico("Usuário", pergunta)

    # Obtém resposta do chatbot
    chatbot = gerenciador_estado.obter_chatbot()
    resposta = chatbot.obter_resposta(pergunta, personalidade)

    # Verifica se precisa de aprendizado
    if "Não sei responder isso ainda" in resposta:
        gerenciador_estado.definir_modo_aprendizado(pergunta, personalidade)
        interface.adicionar_ao_historico("Bot", resposta + " 🤔", personalidade)
    else:
        interface.adicionar_ao_historico("Bot", resposta, personalidade)


def processar_aprendizado(resposta_usuario, personalidade):
    """Processa o aprendizado do chatbot"""
    chatbot = gerenciador_estado.obter_chatbot()
    pergunta_pendente = gerenciador_estado.obter_pergunta_pendente()
    personalidade_pendente = gerenciador_estado.obter_personalidade_pendente()

    # Ensina a resposta ao chatbot
    resultado = chatbot.ensinar_resposta(pergunta_pendente, resposta_usuario, personalidade_pendente)

    # Adiciona resultado ao histórico
    interface.adicionar_ao_historico("Bot", resultado, personalidade)

    # Limpa o modo aprendizado
    gerenciador_estado.limpar_modo_aprendizado()

    st.success("Resposta processada!")


if __name__ == "__main__":
    main()
