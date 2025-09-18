import os
from chatbot.chatbot import ChatBot
from chatbot.historico import Historico
from chatbot.relatorio import Relatorio
from chatbot.estatisticas import Estatisticas

def main():
    caminho_dados = os.path.join("data", "perguntas_respostas.json")
    historico = Historico()
    bot = ChatBot(caminho_dados, historico)

    if bot.base is None:
        return
    
    ultimas = historico.ultimas_interacoes(5)
    if ultimas:
        print("\n=== Últimas 5 interações anteriores ===")
        for linha in ultimas:
            print(linha)
        print("=======================================\n")
    else:
        print("Nenhum histórico anterior encontrado.\n")

    print('Bem-vindo ao Connectcity. Digite SAIR para encerrar.')
    
    personalidades_validas = bot.obter_personalidades_disponiveis()
    while True:
        personalidade = input(f'Escolha a maneira como quer ser atendido ({", ".join(personalidades_validas)}): ').lower()
        if personalidade in personalidades_validas:
            break
        else:
            print("Essa personalidade não existe. Por favor, tente novamente.")

    print(f"Certo, seu atendimento será feito de forma ({personalidade}).")

    while True:
        pergunta = input('Em que posso ajudar? ').lower()

        if pergunta == '/mudar':
            while True:
                personalidade = input(f'Para qual personalidade deseja mudar? ({", ".join(personalidades_validas)}): ').lower()
                if personalidade in personalidades_validas:
                    print(f"Personalidade alterada para ({personalidade}).")
                    break
                else:
                    print("Essa personalidade não existe. Por favor, tente novamente.")
            continue
        
        if pergunta == 'sair':
            print('Foi um prazer tentar te ajudar. Até logo!')
            break
        
        resposta = bot.obter_resposta(pergunta, personalidade)
        print(resposta)
    
    # Gera o relatório com estatísticas ao sair
    gerador_relatorio = Relatorio()
    coletor_estatisticas = Estatisticas()
    estatisticas_coletadas = coletor_estatisticas.coletar_estatisticas(historico)
    gerador_relatorio.gerar_relatorio(historico, estatisticas_coletadas)
    print(f"Relatório de interações gerado com sucesso em '{gerador_relatorio.caminho_relatorio}'.")

if __name__ == "__main__":
    main()