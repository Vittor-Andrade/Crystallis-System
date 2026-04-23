import sqlite3 
import os 

def conectar():
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_db = os.path.normpath(os.path.join(diretorio_atual, "..", "..", "data", "crystallis.db"))
    return sqlite3.connect(caminho_db)

def registrar_procedimento(paciente_id, dente, descricao, custo, dentista_id):
    #Registrando um tratamento realizado em um dente especifico RF03
    try:
        conn = conectar()
        cursor = conn.cursor()
        sql = '''INSERT INTO procedimentos (paciente_id, numero_dente, descricao_procedimento, custo, dentista_id)
                VALUES (?, ?, ?, ?, ?)'''
        cursor.execute(sql, (paciente_id, dente, descricao, custo, dentista_id))
        conn.commit()
        conn.close()
        print(f"✓ Procedimento '{descricao}' no dente {dente} registrado!")
    except Exception as e:
        print(f"X Erro ao registrar procedimento: {e}")

def listar_historico_dente(paciente_id, dente):
    #Buscando tudo o que já foi feito em um dente especifico do paciente
    conn = conectar()
    cursor = conn.cursor()
    sql = '''
        SELECT p.data_realizacao, p.descricao_procedimento, p.custo, u.nome
        FROM procedimentos p
        JOIN usuarios u ON p.dentista_id = u.id
        WHERE p.paciente_id = ? AND p.numero_dente = ?
        ORDER BY p.data_realizacao DESC
    '''
    cursor.execute(sql, (paciente_id, dente))
    historico = cursor.fetchall()
    conn.close()
    return historico