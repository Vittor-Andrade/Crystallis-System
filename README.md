# 🦷 Crystallis System - Gestão Odontológica Inteligente

> ⚠️ **Status do Projeto:** 🛠️ Em Desenvolvimento (Early Access)

O **Crystallis System** é uma solução robusta voltada para a digitalização e otimização de clínicas odontológicas. Desenvolvido com foco em segurança, integridade de dados e experiência do usuário, o sistema centraliza o controle clínico e financeiro em uma arquitetura modularizada.

---

## 🎨 Protótipo de Interface (UI/UX)

A concepção visual e a jornada do usuário foram projetadas no **Figma**, priorizando a usabilidade para profissionais de saúde. 

📍 **[Acesse aqui o Protótipo no Figma](https://www.figma.com/make/lKROMmD1Cx0j1rprhZA2TJ/Dashboard-para-Crystallis?t=iw9POjotYhb56VCJ-1)** *(Substitua o link acima pelo link do seu projeto no Figma)*

---

## 🚀 Funcionalidades Atuais

### 🔒 Segurança & Acesso (LGPD Ready)
- **Criptografia SHA-256:** Senhas de usuários são protegidas por hash de alta segurança.
- **Controle de Acesso (RBAC):** Diferenciação de permissões entre **Dentistas** (acesso total) e **Recepcionistas** (acesso operacional).

### 📋 Gestão Clínica (Prontuário Digital)
- **Odontograma:** Registro detalhado de procedimentos por dente (Padrão 11 a 48).
- **Anamnese & Pacientes:** Cadastro completo com histórico de alergias, medicamentos e convênios.
- **Histórico Retroativo:** Consulta rápida de todas as intervenções realizadas em dentes específicos.

### 📅 Operacional & Financeiro
- **Agenda Inteligente:** Controle de consultas com status em tempo real (Pendente, Confirmado, Finalizado).
- **Business Intelligence (BI):** Cálculo automatizado de faturamento total e ticket médio por paciente.

---

## 🛠️ Stack Tecnológica

O projeto foi construído utilizando as melhores práticas de Engenharia de Software aprendidas em **Análise e Desenvolvimento de Sistemas (ADS)**:

* **Linguagem:** Python 3.x
* **Banco de Dados:** SQLite (com integridade referencial via Foreign Keys)
* **Segurança:** Hashlib (SHA-256)
* **Versionamento:** Git

---

## 📐 Arquitetura do Sistema

A estrutura segue o padrão de separação de responsabilidades para facilitar a manutenção e escalabilidade:

```text
CrystallisSystem/
├── main.py              # Ponto de entrada do sistema
├── auth.py              # Engine de segurança e autenticação
├── data/                # Armazenamento persistente (SQLite)
└── src/
    ├── database/        # Scripts de modelagem e conexão
    └── modules/         # Lógica de negócio (Pacientes, Agenda, Financeiro, etc.)
