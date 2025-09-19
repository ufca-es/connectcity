## Visão Geral

Este é o README do projeto ConnectCity Chatbot. Ele será atualizado com informações detalhadas sobre a estrutura do projeto, como executar o chatbot e uma representação visual da árvore de pastas.

## Estrutura do Projeto

```
.
├── README.md
├── __init__.py
├── app.py
├── chatbot
│   ├── __init__.py
│   ├── aprendizado.py
│   ├── chatbot.py
│   ├── estatisticas.py
│   ├── historico.py
│   ├── relatorio.py
│   └── report_generator.py
├── config
│   ├── __init__.py
│   ├── configuracoes.py
│   └── perguntas_respostas.json
├── data
│   ├── aprendizado.txt
│   ├── historico.txt
│   └── relatorio.txt
├── interface_web
│   ├── __init__.py
│   ├── estilos.py
│   ├── gerenciador_estado.py
│   └── interface.py
├── requirements.txt
└── run.py
```

## Como Executar

### Pré-requisitos

- Python 3.x
- pip (gerenciador de pacotes do Python)

### Instalação

1. Clone o repositório (se aplicável):
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd connectcity
   ```

2. Crie e ative um ambiente virtual (recomendado):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # No Linux/macOS
   .venv\Scripts\activate     # No Windows
   ```

3. Instale as dependências listadas em `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
   As principais dependências incluem:
   - `streamlit`: Para a construção da interface web interativa.
   - `python-dotenv`: Para carregar variáveis de ambiente.
   - `requests`: Para fazer requisições HTTP.
   - `typing-extensions`: Extensões para o módulo `typing`.
   - `validators`: Para validação de dados.

### Execução

Para iniciar o chatbot, execute o arquivo `run.py`:

```bash
python run.py
```

Após a execução, o chatbot estará acessível através da interface web. Abra seu navegador e navegue para `http://localhost:8501` (ou a porta indicada no console).

## Funcionalidades

- **Chatbot Interativo**: Responde a perguntas com base em um conjunto de dados pré-definido e aprendizado.
- **Aprendizado Contínuo**: Capacidade de aprender novas perguntas e respostas.
- **Geração de Relatórios**: Gera relatórios sobre o uso e desempenho do chatbot.
- **Interface Web**: Uma interface amigável para interagir com o chatbot.

## Configuração

O arquivo `config/configuracoes.py` contém as configurações principais do chatbot. O arquivo `config/perguntas_respostas.json` armazena as perguntas e respostas para o aprendizado do chatbot.

## Contribuição

Para contribuir com o projeto, siga os passos abaixo:

1. Faça um fork do repositório.
2. Crie uma nova branch para sua feature (`git checkout -b feature/minha-nova-feature`).
3. Faça suas alterações e commit (`git commit -m 'Adiciona nova feature'`).
4. Envie para o repositório remoto (`git push origin feature/minha-nova-feature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.




## Detalhes de Execução

O chatbot é uma aplicação web construída com Streamlit. Ao executar `run.py`, o Streamlit é iniciado em segundo plano na porta `8501`. Para encerrar a aplicação e gerar um relatório de uso, pressione `Ctrl+C` no terminal onde o `run.py` está sendo executado.




## Funcionalidades Detalhadas do Chatbot ConnectCity

O ConnectCity Chatbot é uma aplicação interativa projetada para fornecer informações e aprender continuamente com as interações do usuário. Abaixo, detalhamos suas principais funcionalidades:

### 1. Interface Web Interativa (Streamlit)

O chatbot é acessível através de uma interface web amigável, desenvolvida utilizando o framework Streamlit. Esta interface permite aos usuários:

- **Interagir com o chatbot**: Enviar perguntas e receber respostas em tempo real.
- **Visualizar histórico de conversas**: Acompanhar o fluxo da interação, com as perguntas do usuário e as respostas do bot exibidas de forma clara.
- **Modo de Aprendizado**: Quando o chatbot não consegue responder a uma pergunta, ele entra em um modo de aprendizado, solicitando ao usuário que forneça a resposta correta. Isso permite que o bot expanda sua base de conhecimento dinamicamente.
- **Seleção de Personalidade**: Os usuários podem escolher a personalidade do chatbot através de uma barra lateral, influenciando o tom e o estilo das respostas.

### 2. Geração Dinâmica de Respostas

O coração do chatbot reside em sua capacidade de gerar respostas de forma inteligente, seguindo uma lógica de prioridade:

- **Base de Conhecimento Principal**: O chatbot primeiramente busca respostas em uma base de dados pré-definida (`perguntas_respostas.json`). Esta base é otimizada com um índice de busca (`_criar_indice_busca`) para garantir a recuperação rápida e eficiente das informações mais relevantes, mesmo com variações na formulação das perguntas.
- **Aprendizado Contínuo**: Caso a pergunta não seja encontrada na base principal, o chatbot consulta um histórico de aprendizados (`data/aprendizado.txt`). As respostas ensinadas pelos usuários são armazenadas e priorizadas em futuras interações, garantindo que o bot se torne mais inteligente e útil ao longo do tempo.
- **Normalização de Texto**: Para melhorar a precisão da busca, o chatbot normaliza o texto das perguntas (removendo acentos e pontuações) antes de compará-las com sua base de conhecimento e aprendizados.

### 3. Mecanismo de Aprendizado e Expansão de Conhecimento

Uma das características mais poderosas do ConnectCity é sua capacidade de aprender com os usuários:

- **Identificação de Lacunas**: Se o chatbot não conseguir fornecer uma resposta satisfatória, ele informará ao usuário e oferecerá a oportunidade de ensinar uma nova resposta para aquela pergunta específica.
- **Armazenamento Persistente**: As novas perguntas e respostas aprendidas são salvas no arquivo `data/aprendizado.txt`, garantindo que o conhecimento adquirido seja persistente entre as sessões do chatbot.
- **Personalização do Aprendizado**: O aprendizado também leva em consideração a personalidade selecionada, permitindo que o bot aprenda respostas específicas para diferentes estilos de interação.

### 4. Geração de Relatórios

O chatbot inclui um módulo de geração de relatórios (`chatbot/report_generator.py`) que é ativado ao encerrar a aplicação (pressionando `Ctrl+C`). Este módulo é responsável por:

- **Análise de Uso**: Coletar e processar dados sobre as interações do chatbot, como perguntas frequentes, respostas fornecidas e o volume de aprendizado.
- **Relatórios Abrangentes**: Gerar relatórios detalhados que podem ser utilizados para monitorar o desempenho do chatbot, identificar áreas de melhoria e entender melhor as necessidades dos usuários.
- **Histórico de Interações**: O histórico de todas as conversas é mantido em `data/historico.txt`, servindo como base para a análise e geração de relatórios.

## Exemplo de Uso

Abaixo, um exemplo de interação simulada com o ConnectCity Chatbot, demonstrando como ele responde a perguntas e como o mecanismo de aprendizado funciona quando uma resposta não é encontrada na base de conhecimento inicial.

```
--- Simulação de Interação com ConnectCity Chatbot ---

Usuário (turista): Olá, qual o nome da cidade?
Bot: O Cariri Garden Shopping, situado na Avenida Padre Cícero, 2555 – Triângulo, oferece ampla estrutura de compras, lazer e serviços.

Usuário (turista): Onde fica a estátua do Padre Cícero?
Bot: O monumento está situado na Colina do Horto, Juazeiro do Norte – CE, sendo um ponto de peregrinação e interesse cultural.

Usuário (morador): Quais os principais eventos religiosos?
Bot: Não sei responder isso ainda...
Bot: Por favor, me ensine a resposta para isso.
Usuário (ensinando): A Estátua do Padre Cícero fica no Horto, um local de peregrinação e vista panorâmica da cidade.
Bot: Entendido, vou me lembrar disso da próxima vez.

Usuário (morador): Qual o horário de funcionamento do comércio local?
Bot: O Cariri Garden Shopping encontra-se na Avenida Padre Cícero, nº 2555 – Triângulo, em Juazeiro do Norte – CE.

Usuário (turista): Qual a história de Juazeiro do Norte?
Bot: A Prefeitura Municipal de Juazeiro do Norte, situada na Rua São Francisco, nº 122 – Centro, é responsável pelos serviços administrativos da cidade.

Usuário (turista): O que fazer em Juazeiro do Norte?
Bot: O campus da Universidade Federal do Cariri (UFCA) localiza-se na Avenida Tenente Raimundo Rocha, nº 1639 – Cidade Universitária.

Usuário (formal): Como posso contribuir para o aprendizado do bot?
Bot: Não sei responder isso ainda...
Bot: Por favor, me ensine a resposta para isso.
Usuário (ensinando): A Estátua do Padre Cícero fica no Horto, um local de peregrinação e vista panorâmica da cidade.
Bot: Entendido, vou me lembrar disso da próxima vez.

Usuário (formal): Não sei responder isso ainda...
Bot: Não sei responder isso ainda...
Bot: Por favor, me ensine a resposta para isso.
Usuário (ensinando): A Estátua do Padre Cícero fica no Horto, um local de peregrinação e vista panorâmica da cidade.
Bot: Entendido, vou me lembrar disso da próxima vez.

Usuário (turista): Quais as romarias de Juazeiro do Norte?
Bot: O endereço da Prefeitura é Rua São Francisco, nº 122, bairro Centro, Juazeiro do Norte – CE.
--- Fim da Simulação ---
```
## Autores
Feito com empenho por:
| Equipe | GitHub | Cargos/Funções |
|---|---|---|
| David Josué Vital Santos | [@davidvital-dev](https://github.com/davidvital-dev) | Gerente de Projeto e Integrador |
| Salomão Rodrigues Silva | [@salomaosilvaa](https://github.com/salomaosilvaa) | Desenvolvedor Back-End |
| Carlos Eduardo Bezerra Santos | [@carlossan25c](https://github.com/carlossan25c) | Testador e QA |
| Dorian Dayvid Gomes Feitosa | [@OtherDinosaur](https://github.com/OtherDinosaur) | Desenvolvedor Front-End |
