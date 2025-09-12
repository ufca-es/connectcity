import os

class Aprendizado:
    def __init__(self, arquivo="data/aprendizado.txt"):
        self.arquivo = arquivo
        if not os.path.exists(self.arquivo):
            with open(self.arquivo, "w", encoding="utf-8") as f:
                f.write("### ARQUIVO DE APRENDIZADO ###\n")
    
    def salvar(self, pergunta, resposta, personalidade = "neutra"):

        """
        Salva uma nova pergunta/resposta no arquivo de aprendizado.
        """
        with open(self.arquivo, "a", encoding = "utf-8") as f:
            f.write(f"Pergunta: {pergunta}\n")
            f.write(f"Personalidade: {personalidade}\n")
            f.write(f"Resposta: {resposta}\n")
            f.write("-"*40+"\n")
    
    def carregar(self):
        """
        Retorna os aprendizados já registrados no arquivo.
        """
        aprendizados = []
        with open(self.arquivo, "r", encoding = "utf-8") as f:
            bloco = {}
            for linha in f:
                linha = linha.strip()
                if linha.startswith("Pergunta:"):
                    bloco["pergunta"] = linha.replace("Pergunta:", "").strip()
                elif linha.startswith("Personalidade"):
                    bloco["personalidade"] = linha.replace("Personalidade:", "").strip()
                elif linha.startswith("Resposta:"):
                    bloco["resposta"] = linha.replace("Resposta:", "").strip()
                elif linha.startswith("-"*40):
                    if bloco:
                        aprendizados.append(bloco)
                        bloco = {}
        return aprendizados