import os
from chatbot.chatbot import ChatBot

def main():
    caminho_dados = os.path.join("data", "perguntas_respostas.json")
    bot = ChatBot(caminho_dados)

    if bot.base is None:
        return

    print('Bem-vindo ao Connectcity. Digite SAIR para encerrar.')
    personalidade = input('Escolha a maneira como quer ser atendido (formal, engraçada, rude): ').lower()
    print(f"Certo, seu atendimento será feito de forma ({personalidade}).")

    while True:
        pergunta = input('Em que posso ajudar? ').lower()

        if pergunta == '/mudar':
            personalidade = input('Para qual personalidade deseja mudar? (gentil, formal, direta): ').lower()
            print(f"Personalidade alterada para ({personalidade}).")
            continue  # Volta para o início do loop sem processar a pergunta

        if pergunta == 'sair':
            print('Foi um prazer tentar te ajudar. Até logo!')
            break
        
        resposta = bot.obter_resposta(pergunta, personalidade)
        print(resposta)

if __name__ == "__main__":
    main()