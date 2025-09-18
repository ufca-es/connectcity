#!/usr/bin/env python3
"""
Script para executar o ConnectCity
"""
import subprocess
import sys
import os

def main():
    """Executa a aplicação Streamlit"""
    try:
        # Caminho para o arquivo app.py
        app_path = os.path.join(os.path.dirname(__file__), "app.py")

        # Executa o Streamlit
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", app_path,
            "--server.headless", "true",
            "--server.port", "8501"
        ], check=True)

    except KeyboardInterrupt:
        print("\nAplicação encerrada pelo usuário.")
    except Exception as e:
        print(f"Erro ao executar a aplicação: {e}")

if __name__ == "__main__":
    main()
