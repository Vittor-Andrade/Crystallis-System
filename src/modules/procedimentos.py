import sqlite3 
import os 

def conectar():
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_db = os.path.normpath(os.path.join(diretorio_atual, "..", "..", "data", "odontoflow.db"))
    return sqlite3.connect(caminho_db)

def registrar_procedimento(paciente_id, dente, descricao, custo):
    #Registrando um tratamento realizado em um dente especifico RF03
    try:
        conn = conectar()
        cursor = conn.cursor()
        sql = '''INSERT INTO procedimentos (paciente_id, numero_dente, descricao_procedimento, custo)
                VALUES (?, ?, ?, ?)'''
        cursor.execute(sql, (paciente_id, dente, descricao, custo))
        conn.commit()
        conn.close()
        print(f"✓ Procedimento '{descricao}' no dente {dente} registrado!")
    except Exception as e:
        print(f"X Erro ao registrar procedimento: {e}")

def listar_historico_dente(paciente_id, dente):
    #Buscando tudo o que já foi feito em um dente especifico do paciente
    conn = conectar()
    cursor = conn.cursor()
    sql = 'SELECT data_realizacao, descricao_procedimento, custo FROM procedimentos WHERE paciente_id = ? AND numero_dente = ? ORDER BY data_realizacao DESC'
    cursor.execute(sql, (paciente_id, dente))
    historico = cursor.fetchall()
    conn.close()
    return historico

if __name__ == "__main__":
    #Testando registrando uma cárie no dente 14 do paciente 1
    registrar_procedimento(1, 14, "Tratamento de Cárie", 150.00)

    print(f"\n--- Histórico do Dente 14 ---")
    for h in listar_historico_dente(1, 14):
        print(f"Data: {h[0]} | Procedimento: {h[1]} | Valor: R${h[2]:.2f}")