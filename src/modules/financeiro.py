import sqlite3 
import os
from datetime import datetime

def conectar():
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_db = os.path.normpath(os.path.join(diretorio_atual, "..", "..", "data", "crystallis.db"))
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


def faturamento_por_paciente(paciente_id):
    #Calcula o valor que um cliente já pagou por seus procedimentos
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(custo) FROM procedimentos WHERE paciente_id = ?", (paciente_id,))
        resultado = cursor.fetchone()[0]
        conn.close()
        return resultado if resultado else 0.0
    except Exception as e:
        print(f"Erro ao calcular faturamento do paciente {e}")
        return 0.0
    

def exportar_relatorio_faturamento():
    #Gera um arquivo de txt detalhado com os procedimentos e faturamento da clinica

    try:
        conn = conectar()
        cursor = conn.cursor()

        #Query detalhada trazendo as informações importantes do relatório
        query = '''
            SELECT pr.data_realizacao, pa.nome, pr.descricao_procedimento, pr.custo, u.nome
            FROM procedimentos pr
            JOIN pacientes pa ON pr.pacientes_id = pa.id
            JOIN usuarios u ON pr.dentista_id = u.id
            ORDER BY pr.data_realizacao DESC
        '''
        cursor.execute(query)
        procedimentos = cursor.fetchall()

        cursor.execute("SELECT SUM(custo) FROM procedimentos")
        total = cursor.fetchall()[0]
        total = total if total else 0.0

        conn.close()

        #Define o caminho para a pasta "Relatórios" na raiz do projeto
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        pasta_relatorios = os.path.normpath(os.path.join(diretorio_atual, "..", "..", "relatorios"))
        os.makedirs(pasta_relatorios, exits_ok = True)

        #Nomeando arquivo com data e hora diferente para não sobescrever
        timestamp = datetime.now().strftime("%y%m%d_%H%M$S")
        caminho_arquivo = os.path.join(pasta_relatorios, f"relatorio_faturamento_{timestamp}.txt")

        #Criando o arquivo de texto
        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            f.write("============================================================\n")
            f.write("               CRYSTALLIS SYSTEM - RELATÓRIO\n")
            f.write(f" Emissão: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
            f.write("============================================================\n\n")
            
            f.write(f"{'DATA':<12} | {'PACIENTE':<20} | {'PROCEDIMENTO':<18} | {'VALOR':<10} | {'DENTISTA'}\n")
            f.write("-" * 85 + "\n")
            
            for p in procedimentos:
                data_f = p[0][:10]  # Pega apenas AAAA-MM-DD
                f.write(f"{data_f:<12} | {p[1][:20]:<20} | {p[2][:18]:<18} | R$ {p[3]:>8.2f} | Dr(a). {p[4]}\n")
                
            f.write("-" * 85 + "\n")
            f.write(f"FATURAMENTO TOTAL ACUMULADO: R$ {total:.2f}\n")
            f.write("============================================================\n")

        print(f"\033[32m✓ Relatório exportado com sucesso em: {caminho_arquivo}\033[0m")
        return True
    
    except Exception as e:
        print(f"\033[31mX Erro ao exportar o relatório: {e}\033]0m")
        return False