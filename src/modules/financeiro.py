import sqlite3 
import os 

def conectar():
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_db = os.path.normpath(os.path.join(diretorio_atual, "..", "..", "data", "odontoflow.db"))
    return sqlite3.connect(caminho_db)

def calcular_faturamento_total():
    #Soma todos os procedimentos realizados na clinica
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(custo) FROM procedimentos")
        resultado = cursor.fetchone()[0]
        conn.close()
    
        return resultado if resultado else 0.0
    except Exception as e:
        print(f"X Erro ao calcular faturamento: {e}")
        return 0.0


def faturamento_por_paciente(paciente_id,):
    #Calcula o valor que um cliente já pagou por seus procedimentos
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(custo) FROM procedimentos WHERE paciente_id = ?", (paciente_id))
        resultado = cursor.fetchone()[0]
        conn.close()
        return resultado if resultado else 0.0
    except Exception as e:
        print(f"Erro ao calcular faturamento do paciente {e}")
        return 0.0