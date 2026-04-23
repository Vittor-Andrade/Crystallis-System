import sqlite3
import os

def inicializar_banco():

    #Define o caminho para a pasta /data de forma relativa ao arquivo
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_db = os.path.normpath(os.path.join(diretorio_atual, "..", "..", "data", "crystallis.db"))

    os.makedirs(os.path.dirname(caminho_db), exist_ok=True)

    try:
        conn = sqlite3.connect(caminho_db)
        cursor = conn.cursor()

        cursor.execute('PRAGMA foreign_keys = ON;')

        #RF1 Gestão de Dentistas, Pacientes e Anamenese
                
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                senha TEXT NOT NULL,
                cargo TEXT NOT NULL CHECK(cargo IN('Dentista', 'Recepcionista')), 
                cro TEXT UNIQUE,
                especialidade TEXT,
                data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
        
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
                dentista_id INTEGER,
                paciente_id INTEGER,
                data_hora DATETIME NOT NULL,
                tipo_consulta TEXT,
                status TEXT DEFAULT 'Pendente',
                FOREIGN KEY (dentista_id) REFERENCES usuarios (id),
                FOREIGN KEY (paciente_id) REFERENCES pacientes (id)
            )               
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS procedimentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                paciente_id INTEGER,
                dentista_id INTEGER,
                numero_dente INTEGER NOT NULL, -- Padrão 11 a 48
                descricao_procedimento TEXT NOT NULL, -- Ex: Cárie, Canal, Extração
                custo REAL,
                data_realizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (dentista_id) REFERENCES usuarios (id),
                FOREIGN KEY (paciente_id) REFERENCES pacientes (id)
                )
            ''')

        conn.commit()
        conn.close()
        print("✓ Banco de dados inicializado com sucesso.")

    except Exception as e:
        print(f"X Erro na inicialização do banco: {e}")
        
def conectar_db():
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_db = os.path.normpath(os.path.join(diretorio_atual, "..", "..", "data", "crystallis.db"))
    return sqlite3.connect(caminho_db)

if __name__ == "__main__":
    inicializar_banco()