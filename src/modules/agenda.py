import sqlite3
import os 
from datetime import datetime

def conectar():
    #Buscando o caminho do Banco de Dados na pasta
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_db = os.path.normpath(os.path.join(diretorio_atual, "..", "..", "data", "odontoflow.db"))
    return sqlite3.connect(caminho_db)

def agendar_consulta(paciente_id, data_hora, tipo_consulta):
    #Registrando um agendamento vinculado a um paciente
    try: 
        conn = conectar()
        cursor = conn.cursor()

        sql = ''' INSERT INTO agenda (paciente_id, data_hora, tipo_consulta, status)
                    VALUES (?, ?, ?, 'Pendente')'''
        
        cursor.execute(sql, (paciente_id, data_hora, tipo_consulta))
        conn.commit()
        conn.close()
        print(f"✓ Consulta de {tipo_consulta} agendada para {data_hora}!")
    except Exception as e:
        print(f"X Erro ao agendar: {e}")

def listar_agenda_do_dia(data):
    #Buscando todos os compromissos de uma data especifica
    conn = conectar()
    cursor = conn.cursor()
    query = '''
        SELECT a.id, p.nome, a.data_hora, a.tipo_consulta, a.status
        FROM agenda a
        JOIN pacientes p ON a.paciente_id = p.id
        WHERE date(a.data_hora) = ?
        ORDER BY a.data_hora ASC
    '''
    cursor.execute(query, (data,))
    consultas = cursor.fetchall()
    conn.close()
    return consultas

def atualizar_status_agenda(consulta_id, novo_status):
    #Atualizando o status da consulta
    try:
        conn = conectar()
        cursor = conn.cursor()
        sql = 'UPDATE agenda SET status = ? WHERE id = ?'
        cursor.execute(sql, (novo_status, consulta_id))
        conn.commit()
        conn.close()
        print(f"✓ Status da consulta {consulta_id} atualizado.")
    except Exception as e:
        print(f"X Erro: {e}")