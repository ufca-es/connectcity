import streamlit as st
from config.configuracoes import INTERFACE, PERSONALIDADES_DISPONIVEIS, PERSONALIDADE_PADRAO

def criar_sidebar():
    """Cria a barra lateral com configurações"""
    with st.sidebar:
        st.header("⚙️ Configurações")

        personalidade = st.selectbox(
            "Escolha o estilo de atendimento:",
            PERSONALIDADES_DISPONIVEIS,
            index=PERSONALIDADES_DISPONIVEIS.index(PERSONALIDADE_PADRAO),
            help="Selecione como o chatbot deve se comportar"
        )

        st.markdown("---")

        # Container para o botão com melhor alinhamento
        with st.container():
            if st.button("🗑️ " + INTERFACE["botao_limpar"], use_container_width=True):
                limpar_historico()

        st.markdown("---")

        # Informações sobre o projeto
        with st.expander("ℹ️ Sobre o ConnectCity"):
            st.markdown("""
            O ConnectCity é um chatbot desenvolvido para ajudar você a encontrar
            locais e serviços em Juazeiro do Norte - CE.

            **Funcionalidades:**
            - Busca por locais de interesse
            - Informações sobre serviços públicos
            - Diferentes estilos de atendimento
            - Histórico de conversas
            """)

        return personalidade

def exibir_mensagem(remetente, mensagem, personalidade=None):
    """Exibe uma mensagem no chat"""
    if remetente == "Usuário":
        st.markdown(f"""
        <div class="chat-message user-message">
            <strong>Você:</strong> {mensagem}
        </div>
        """, unsafe_allow_html=True)
    else:
        emoji_personalidade = {
            "formal": "🤝",
            "divertida": "😄",
            "rude": "😠"
        }
        emoji = emoji_personalidade.get(personalidade, "🤖")

        st.markdown(f"""
        <div class="chat-message bot-message">
            <strong>{emoji} ConnectCity:</strong> {mensagem}
        </div>
        """, unsafe_allow_html=True)


def limpar_historico():
    """Limpa o histórico de conversas"""
    if 'historico_conversa' in st.session_state:
        st.session_state.historico_conversa = []
    st.success("Histórico limpo!")

def exibir_historico():
    """Exibe o histórico de conversas"""
    if 'historico_conversa' not in st.session_state:
        st.session_state.historico_conversa = []

    if st.session_state.historico_conversa:
        st.markdown("### 💬 Conversa")
        for item in st.session_state.historico_conversa:
            exibir_mensagem(item['remetente'], item['mensagem'], item.get('personalidade'))
    else:
        st.info("👋 Olá! Faça sua primeira pergunta sobre Juazeiro do Norte.")

def adicionar_ao_historico(remetente, mensagem, personalidade=None):
    """Adiciona mensagem ao histórico da sessão"""
    if 'historico_conversa' not in st.session_state:
        st.session_state.historico_conversa = []

    st.session_state.historico_conversa.append({
        'remetente': remetente,
        'mensagem': mensagem,
        'personalidade': personalidade
    })

def exibir_modo_aprendizado():
    """Exibe interface para ensinar o chatbot"""
    if 'modo_aprendizado' in st.session_state and st.session_state.modo_aprendizado:
        st.warning("🎓 O chatbot não soube responder. Você pode ensiná-lo!")

        with st.form("ensinar_resposta"):
            resposta_usuario = st.text_area(
                "Como você responderia essa pergunta?",
                placeholder="Digite a resposta ou 'não sei' para cancelar...",
                height=100
            )

            col1, col2 = st.columns(2)
            with col1:
                ensinar = st.form_submit_button("✅ Ensinar", type="primary", use_container_width=True)
            with col2:
                cancelar = st.form_submit_button("❌ Cancelar", use_container_width=True)

            if ensinar and resposta_usuario:
                return resposta_usuario
            elif cancelar:
                st.session_state.modo_aprendizado = False
                # Não usar st.rerun() - deixar o fluxo natural

    return None
