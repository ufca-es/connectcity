import json
import os # Importe a biblioteca os

def base_json(caminho_arquivo):
    """Carrega o conteúdo de um arquivo JSON."""
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            return dados
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return None 

def chatbot():
    # Defina o caminho correto para o seu arquivo de dados
    # Use o nome correto do seu arquivo aqui
    caminho_dados = os.path.join("data", "perguntas_respostas.json") 
    
    base = base_json(caminho_dados)

    if base is None:
        return 

    print('Bem-vindo ao Connectcity. Digite SAIR para encerrar.')
    person = str(input('Escolha a maneira como quer ser atendido (gentil, formal ou direta): ')).lower()
    print(f"Certo, seu atendimento será feito de forma ({person}).")

    while True:
        pergunta = str(input('Em que posso ajudar? ')).lower()
        if pergunta == 'sair':
            print('Foi um prazer tentar te ajudar. Até logo!')
            break
        
        if pergunta in base and person in base[pergunta]:
            resposta = base[pergunta][person]
        else:
            resposta = 'Desculpe, não entendi sua pergunta.'
        print(resposta)

chatbot()