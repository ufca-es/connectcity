# Chatbot ConnectCity
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE) 
## Descrição do Projeto
O ConnectCity é um chatbot simples, desenvolvido para ajudar usuários a encontrarem locais de interesse na cidade. Ele interage via terminal e, a partir de uma solicitação, retorna informações essenciais como endereço, horário de funcionamento e outros detalhes básicos sobre o local desejado.

## Funcionalidades
O Chatbot ConnectCity oferece as seguintes funcionalidades principais:

- Busca por Locais: Permite encontrar locais de interesse (como museus, cafés, bibliotecas, etc.) com base na entrada do usuário.

- Informações Detalhadas: Fornece o endereço, horário de funcionamento e uma breve descrição de cada local.

- Histórico de Conversas: Mantém um registro de todas as interações do usuário.

- Coleta de Estatísticas: Monitora o uso do bot, registrando, por exemplo, os locais mais procurados.

- Geração de Relatório: Cria um resumo da sessão de conversa em um arquivo de texto ao final da execução.

## Comandos do Bot
Durante a conversa, você pode usar os seguintes comandos para interagir com o bot:

- SAIR: Encerra a execução do programa a qualquer momento.

- /mudar: Permite alterar a personalidade do bot (divertida, formal, rude) no meio da conversa.

- Cancelar Aprendizado: Caso o bot não saiba uma resposta e pergunte "Me ensine a resposta:", você pode digitar "não sei" ou "cancelar" para interromper o processo de aprendizado.

## Estrutura do Projeto
A organização dos arquivos e diretórios visa manter o código modular e de fácil manutenção:
```
├── chatbot/                # Módulos de lógica do bot
│   ├── __init__.py
│   ├── chatbot.py          # Lógica principal de busca e retorno de locais
│   ├── historico.py        # Gerenciamento de histórico de interações
│   ├── estatisticas.py     # Coleta de estatísticas de uso
│   └── aprendizado.py      # Lógica para "aprender" novos locais
│
├── data/                   # Arquivos de dados
│   ├── perguntas_respostas.json  # Base de dados de locais
│   ├── historico.txt
│   └── aprendizado.txt
│
├── .gitignore
├── README.md
└── main.py                 # Ponto de entrada do programa
```
## Como Executar
Siga os passos abaixo para rodar o Chatbot ConnectCity em sua máquina.

### Pré-requisitos
Certifique-se de ter o Python 3 instalado.

### Passos
Clone o Repositório:
```
Bash

git clone [https://github.com/ufca-es/connectcity](https://github.com/ufca-es/connectcity)
cd connectcity
```
### Execute o Programa:
Certifique-se de que o arquivo data/perguntas_respostas.json contém a base de dados dos locais que o bot deve procurar.
```
Bash

python main.py
```
## Demonstração

# Autores
Feito com dedicação por:
| Equipe | GitHub | Cargos/Funções |
|---|---|---|
| David Josué Vital Santos | [@davidvital-dev](https://github.com/davidvital-dev) | Gerente de Projeto e Integrador |
| Salomão Rodrigues Silva | [@salomaosilvaa](https://github.com/salomaosilvaa) | Desenvolvedor Back-End |
| Carlos Eduardo Bezerra Santos | [@carlossan25c](https://github.com/carlossan25c) | Testador e QA |
| Dorian Dayvid Gomes Feitosa | [@OtherDinosaur](https://github.com/OtherDinosaur) | Desenvolvedor Front-End |
