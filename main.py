from src.modules.pacientes import cadastrar_paciente, buscar_paciente_por_cpf, listar_todos_pacientes
from src.modules.agenda import agendar_consulta, listar_agenda_do_dia, atualizar_status_agenda
from src.modules.procedimentos import registrar_procedimento, listar_historico_dente
from src.modules.financeiro import calcular_faturamento_total, faturamento_por_paciente
from src.database.database_setup import inicializar_banco, conectar_db
import auth
from datetime import datetime
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal(usuario):
    while True:
        print("\n" + "="*50)
        print(f"          CRYSTALLIS SYSTEM v1.0 - Logado como: {usuario['nome']}")
        print("="*50)
        
        print(" [PACIENTES]")
        print(" 1. Cadastrar Novo paciente")
        print(" 2. Buscar por CPF")
        print(" 3. Listar Todos os Pacientes")
        print("-"*50)

        print(" [AGENDA]")
        print(" 4. Ver Agenda de Hoje")
        print(" 5. Marcar Nova Consulta")
        print(" 6. Atualizar Status (Confirmar / cancelar)")
        print("-"*50)

        print(" [CLÍNICO / ODONTOGRAMA]")
        print(" 7. Registrar Procedimento no Dente")
        print(" 8. Ver Histórico por Dente")
        print("-"*50)

        if usuario['cargo'] == "Dentista":
            print(" [GESTÃO]")
            print(" 9. Relatório de Faturamento Total")
            print(" 10. Faturamento por Paciente")
            print("-"*50)

        print(" 0. Sair")
        print("="*50)

        opcao = input("Selecione a operação: ")

        if opcao == "1":
            print("\n---    NOVO CADASTRO  ---")
            nome = input("Nome Completo: ")
            cpf = input("CPF: ")
            conv = input("Convênio: ")
            ale = input("Alergias: ")
            med = input("Medicamentos: ")
            cadastrar_paciente(nome, cpf, conv, ale, med)

        elif opcao == "2":
            cpf = input("\nDigite o CPF para busca: ")
            p = buscar_paciente_por_cpf(cpf)
            if p:
                print(f"\n RESULTADO: ID{p[0]} | {p[1]} | CPF: {p[2]}")
            else:
                print("\n Paciente não localizado.")

        elif opcao == "3":
            print("\n---    LISTA DE PACIENTES  ---")
            lista = listar_todos_pacientes()
            if not lista:
                print("Nenhum paciente no banco de dados.")
            else:
                print(f"{'ID':<4} | {'NOME':<25} | {'CPF':<15} | {'CONVENIO'}")
                print("-"*55)
                for p in lista:
                    print(f"{p[0]:<4} | {p[1]:<25} | {p[2]:<15} | {p[3]}")
            
        elif opcao == "4":
            hoje = datetime.now().strftime("%Y-%m-%d")
            consultas = listar_agenda_do_dia(hoje)
            print(f"\n---       AGENDA DE HOJE ({hoje})     ---")
            if not consultas:
                print("Sem compromissos para hoje.")
            for c in consultas:
                print(f"ID: {c[0]} | {c[2][11:16]} | {c[1]} | {c[3]} | [{c[4]}]")
            
        elif opcao == "5":
            print("\n---    AGENDAR CONSULTA    ---")
            p_id = input("ID do Paciente: ")
            data = input("Data e Hora (AAA-MM-DD HH:MM): ")
            tipo = input("Tipo (Limpeza/Avaliação/Cirurgia): ")
            agendar_consulta(p_id, data, tipo)

        elif opcao == "6":
            print("\n---    ATUALIZAR AGENDA    ---")
            id_con = input("ID da Consulta: ")
            print("Status: 1. Confirmado | 2. Cancelado | 3. Finalizado")
            st_op = input("Escolha a opção: ")
            status_map = {"1": "Confirmado", "2": "Cancelado", "3": "Finalizado"}
            if st_op in status_map:
                atualizar_status_agenda(id_con, status_map[st_op])
            else:
                print("Opção Inválida.")

        elif opcao == "7":
            print("\n---    REGISTRAR NO ODONTOGRAMA    ---")
            p_id = input("ID do Paciente: ")
            dente = input("Número do Dente (11-48): ")
            desc = input("Descrição: ")
            try:
                valor = float(input("Valor R$: "))
            except ValueError:
                valor = 0.0
                print("Valor inválido, registrado como 0.0")
            registrar_procedimento(p_id, dente, desc, valor, usuario['id'])

        elif opcao == "8":
            print("\n---    PRONTUÁRIO POR DENTE    ---")
            p_id = input("ID do paciente: ")
            dente = input("Número do Dente (11-48): ")
            hist = listar_historico_dente(p_id, dente)
            print(f"\n---   PRONTUÁRIO DO DENTE {dente} ---")
            if not hist:
                print("Nenhum procedimento registrado para este dente.")
            else:
                for h in hist:
                    print(f"Data: {h[0][:10]} | {h[1]} | R$ {h[2]:.2f} | Dr(a): {h[3]}")

        elif opcao == "9":
            if usuario['cargo'] == "Dentista":
                total = calcular_faturamento_total()
                print(f"FATURAMENTO TOTAL: R$ {total:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
            else:
                print(f"[!] Acesso Negado!")

        elif opcao == "10":
            if usuario['cargo'] == "Dentista":
                print("\n---    FATURAMENTO POR PACIENTE    ---")
                p_id = input("Digite o ID do Paciente: ")
                total_p = faturamento_por_paciente(p_id)
                print(f"\nPaciente ID: {p_id} | Total: R$ {total_p:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
            else:
                print("\n[!] Acesso Negado!")
            
        elif opcao == "0":
            print("\nSaíndo . . . Backup do Crystallis System realizado.")
            break

        input("\nPressione Enter para voltar ao menu . . .")
        limpar_tela()

if __name__ == "__main__":
    inicializar_banco()
    conn = conectar_db()
    
    limpar_tela()
    usuario_logado = auth.fazer_login(conn)
    
    if usuario_logado:
        limpar_tela()
        menu_principal(usuario_logado)
        conn.close()
    else:
        print("\nSistema encerrado. Falha na autenticação.")