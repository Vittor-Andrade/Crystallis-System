import os
import shutil
from datetime import datetime

def realizar_backup_banco():
    #Faz uma cópia de segurança do arquivo crystallis.db

    try:
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        caminho_banco = os.path.normpath(os.path.join(diretorio_atual, "..", "..", "data", "crystallis.db"))

        