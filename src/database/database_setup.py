import sqlite3
import os

def inicializar_banco():

    #Define o caminho para a pasta /data de forma relativa ao arquivo
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_db = os.path.normpath(os.path.join(diretorio_atual, "..", "..", "data", "odontoflow.db"))

    try:
        conn = sqlite3.connect(caminho_db)
        cursor = conn.cursor()

        #RF1 Gestão de Pacientes e Anamenese
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pacientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf TEXT UNIQUE NOT NULL,
                convenio TEXT,
                alergias TEXT,
                medicamentos TEXT,
                observacoes_clinicas TEXT,
                data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        #RF2 Agenda e Status de Confirmação
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS agenda(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                paciente_id INTEGER,
                data_hora DATETIME NOT NULL,
                tipo_consulta TEXT,
                status TEXT DEFAULT 'Pendente',
                FOREIGN KEY (paciente_id) REFERENCES pacientes (id)
            )               
        ''')

        conn.commit()
        conn.close()
        print("✓ Banco de dados inicializado com sucesso.")

    except Exception as e:
        print(f"X Erro na inicialização do banco: {e}")

if __name__ == "__main__":
    inicializar_banco()