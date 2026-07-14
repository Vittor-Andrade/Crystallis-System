import customtkinter as ctk

# Configuração global do visual
ctk.set_appearance_mode("System")  # Segue o modo do Windows (Claro/Escuro)
ctk.set_default_color_theme("blue") # Cor base dos botões

class TelaLogin(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações da Janela
        self.title("Crystallis System - Login")
        self.geometry("400x500")
        self.resizable(False, False)

        # TÍTULO (CTkLabel)
        self.titulo = ctk.CTkLabel(self, text="CRYSTALLIS", font=("Helvetica", 28, "bold"))
        self.titulo.pack(pady=(60, 40))

        # CAMPO DE E-MAIL (CTkEntry)
        self.input_email = ctk.CTkEntry(self, placeholder_text="Digite seu e-mail", width=280, height=45)
        self.input_email.pack(pady=10)

        # CAMPO DE SENHA (CTkEntry)
        self.input_senha = ctk.CTkEntry(self, placeholder_text="Digite sua senha", show="*", width=280, height=45)
        self.input_senha.pack(pady=10)

        # BOTÃO ENTRAR (CTkButton)
        self.botao_entrar = ctk.CTkButton(self, text="Entrar no Sistema", width=280, height=45, font=("Helvetica", 14, "bold"), command=self.acao_login)
        self.botao_entrar.pack(pady=(30, 10))

    def acao_login(self):
        # Aqui é onde o Frontend conversa com o seu Backend!
        email = self.input_email.get()
        senha = self.input_senha.get()
        print(f"O botão foi clicado! Dados capturados: {email} / {senha}")
        # No sistema real, chamaríamos a função do seu auth.py aqui.

if __name__ == "__main__":
    app = TelaLogin()
    app.mainloop()