# ConnectCity - Seu Guia da Cidade 🏙️

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white) [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)

## 📋 Descrição do Projeto

O ConnectCity é um chatbot web desenvolvido para ajudar usuários a encontrarem locais de interesse e serviços em Juazeiro do Norte - CE. Com uma interface moderna e responsiva, oferece diferentes estilos de atendimento para uma experiência personalizada.

## ✨ Funcionalidades

- 🔍 **Busca por Locais**: Encontre locais de interesse como hospitais, universidades, shoppings, etc.
- 📍 **Informações Detalhadas**: Endereços, horários e descrições dos locais
- 🎭 **Personalidades Diferentes**: Atendimento formal, divertido ou direto
- 💬 **Interface Web Responsiva**: Funciona perfeitamente no desktop e celular
- 📚 **Sistema de Aprendizado**: O chatbot pode aprender novas respostas
- 📊 **Histórico de Conversas**: Mantenha registro das interações
- 🎨 **Design Moderno**: Interface intuitiva e bonita


## 🚀 Como Executar

### Pré-requisitos
- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Instalação e Execução

1. **Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/connectcity
cd connectcity
```

2. **Ative o ambiente virtual:**
```bash
source venv/bin/activate
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

4. **Execute a aplicação:**
```bash
python run.py
```

Ou diretamente com Streamlit:
```bash
streamlit run app.py
```

5. **Acesse no navegador:**
   - A aplicação estará disponível em: `http://localhost:8501`
   - Funciona em qualquer dispositivo com navegador (desktop, tablet, celular)

## 🔧 Resolução de Problemas

### Erro: "externally-managed-environment"
Se você receber o erro `error: externally-managed-environment` ao tentar instalar as dependências:

1. **Certifique-se de ativar o ambiente virtual primeiro:**
```bash
source venv/bin/activate
```

2. **Instale as dependências dentro do ambiente virtual:**
```bash
pip install -r requirements.txt
```

**Importante:** Sempre ative o ambiente virtual (`source venv/bin/activate`) antes de instalar pacotes ou executar o projeto. Se abrir um novo terminal, será necessário ativar novamente.

### Outros problemas comuns:

- **Erro de permissão:** Execute os comandos sem `sudo`
- **Python não encontrado:** Verifique se Python 3.7+ está instalado
- **Porta ocupada:** Se a porta 8501 estiver ocupada, o Streamlit usará automaticamente outra porta

## 🎮 Como Usar

1. **Escolha o Estilo de Atendimento:**
   - **Formal**: Respostas profissionais e educadas
   - **Divertida**: Respostas com emojis e linguagem descontraída
   - **Rude**: Respostas diretas e objetivas

2. **Faça suas Perguntas:**
   - Digite perguntas sobre locais em Juazeiro do Norte
   - Exemplos: "Onde fica a UFCA?", "Preciso de apoio psicológico", "Endereço do hospital"

3. **Ensine o Chatbot:**
   - Se o chatbot não souber responder, você pode ensiná-lo
   - Suas contribuições ajudam a melhorar o sistema

## 🔧 Configuração

As configurações podem ser alteradas no arquivo `config/configuracoes.py`:
- Personalidades disponíveis
- Mensagens do sistema
- Caminhos dos arquivos
- Configurações da interface

## 📊 Funcionalidades Avançadas

- **Sistema de Aprendizado**: O chatbot aprende com as interações
- **Histórico Persistente**: Conversas são salvas em arquivos
- **Estatísticas**: Coleta dados sobre uso e perguntas mais frequentes
- **Relatórios**: Gera relatórios detalhados das interações

## 👥 Equipe de Desenvolvimento

Desenvolvido por estudantes do primeiro semestre de Engenharia de Software:

| Nome | GitHub | Função |
|------|--------|---------|
| David Josué Vital Santos | [@davidvital-dev](https://github.com/davidvital-dev) | Gerente de Projeto e Integrador |
| Salomão Rodrigues Silva | [@salomaosilvaa](https://github.com/salomaosilvaa) | Desenvolvedor Back-End |
| Carlos Eduardo Bezerra Santos | [@carlossan25c](https://github.com/carlossan25c) | Testador e QA |
| Dorian Dayvid Gomes Feitosa | [@OtherDinosaur](https://github.com/OtherDinosaur) | Desenvolvedor Front-End |
