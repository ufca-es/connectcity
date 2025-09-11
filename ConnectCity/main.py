import json

def base_json(arquivo):
    with open('perguntas_respostas.json', 'r', encoding = 'utf-8') as arquivo:
        dados = json.load(arquivo)
        return dados 

def chatbot():
    base = base_json("perguntas_respostas.json")
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
