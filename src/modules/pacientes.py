import sqlite3
import os 

def conectar():
    #Busca o caminho do banco de dados na pasta raiz
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_db = os.path.normpath(os.path.join(diretorio_atual, "..", "..", "data", "odontoflow.db"))
    return sqlite3.connect(caminho_db)

def cadastrar_paciente(nome, cpf, convenio, alergias = "", medicamentos = ""):
    #Inserindo um novo paciente no banco de dados
    try:
        conn = conectar()
        cursor = conn.cursor()

        sql = ''' INSERT INTO pacientes (nome, cpf, convenio, alergias, medicamentos) 
               VALUES (?,?,?,?,?)'''
        
        cursor.execute(sql, (nome, cpf, convenio, alergias, medicamentos))
        conn.commit()
        conn.close()
        print(f"✓ Paciente {nome} cadastrado com sucesso!")
    except Exception as e:
        print(f"X Erro ao cadastrar: {e}")

def buscar_paciente_por_cpf(cpf):
    #Busca rápida por CPF como solicitado no RF1.
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pacientes WHERE cpf = ?", (cpf,))
    paciente = cursor.fetchone()
    conn.close()
    return paciente

def listar_todos_pacientes():
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, cpf, convenio FROM pacientes ORDER BY nome ASC")
        pacientes = cursor.fetchall()
        conn.close()
        return pacientes
    except Exception as e:
        print(f"X Erro ao listar pacientes: {e}")
        return[]