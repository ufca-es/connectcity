#!/usr/bin/env python3
"""
Script para executar o ConnectCity
"""
import subprocess
import sys
import os
import time

# Adiciona o diretório do projeto ao sys.path para que 'connectcity' seja um pacote
project_root = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, project_root)

from chatbot.report_generator import ReportGenerator

def main():
    """
    Executa a aplicação Streamlit e gera um relatório ao encerrar.
    """
    report_generator = ReportGenerator()
    process = None
    try:
        # Caminho para o arquivo app.py
        app_path = os.path.join(os.path.dirname(__file__), "app.py")

        # Define o PYTHONPATH para o processo filho
        env = os.environ.copy()
        
        # Inicia o Streamlit como um processo filho
        process = subprocess.Popen([
            sys.executable, "-m", "streamlit", "run", app_path,
            "--server.headless", "true",
            "--server.port", "8501"
        ], env=env)
        print(f"Streamlit iniciado com PID: {process.pid}")
        print("Aguardando interações... Pressione Ctrl+C para encerrar e gerar o relatório.")

        # Mantém o script principal rodando para capturar KeyboardInterrupt
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nAplicação encerrada pelo usuário. Gerando relatório...")
        if process:
            process.terminate() # Envia SIGTERM para o processo do Streamlit
            process.wait() # Espera o processo terminar
        report_generator.generate_full_report()
    except Exception as e:
        print(f"Erro ao executar a aplicação: {e}. Gerando relatório...")
        if process:
            process.terminate()
            process.wait()
        report_generator.generate_full_report()

if __name__ == "__main__":
    main()


