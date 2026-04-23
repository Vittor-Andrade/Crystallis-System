import sqlite3 

def fazer_login(conn):
    cursor = conn.cursor()

    #Verifica se existe algum usuário cadastrado
    cursor.execute("SELECT COUNT(*) FROM usuarios")
    if cursor.fetchone()[0] == 0:
        print("\n[!] Nenhum usuário encontrado. Cadastre-se antes de tentar fazer login de novo!")
        cadastrar_usuario(conn)

    print("\n" + "="*30)
    print("     LOGIN - CRYSTALIS")
    print("="*30)

    tentativas = 3
    while tentativas > 0:
        email = input("E-mail: ")
        senha = input("Senha: ")

        cursor.execute("SELECT id, nome, cargo FROM usuarios WHERE email = ? AND senha = ?", (email, senha))
        usuario = cursor.fetchone()

        if usuario:
            print(f"\n✓ Bem-Vindo(a), {usuario[1]} ({usuario[2]})!")
            return {"id": usuario[0], "nome": usuario[1], "cargo": usuario[2]}
        else:
            tentativas -=1
            print(f"X Dados incorretos. tentativas restantes: {tentativas}")
    
    return None

def cadastrar_usuario(conn):
    cursor = conn.cursor()
    print("\n--- NOVO CADASTRO ---")
    nome = input("Nome: ")
    email = input("E-mail: ")
    senha = input("Senha: ")

    print("Cargo: 1. Dentista | 2. Recepcionista")
    op = input("Opção: ")
    cargo = "Dentista" if op == "1" else "Recepcionista"

    cro = None
    if cargo == "Dentista":
        cro = input("CRO: ")

    try:
        cursor.execute(
            "INSERT INTO usuarios (nome, email, senha, cargo, cro) VALUES (?, ?, ?, ?, ?)",
            (nome, email, senha, cargo, cro)
        )
        conn.commit()
        print("✓ Cadastrado com sucesso!")
    except Exception as e:
         print(f"Erro: {e}")
