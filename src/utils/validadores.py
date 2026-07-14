import re
from datetime import datetime

def validar_cpf(cpf: str) -> bool:
    #Validando o CPF usando o cálculo dos dígitos verificadores oficiais, retornando true or false
   
    #Remove qualquer caractere que não seja número(limpando pontos e traços)
    cpf = re.sub(r'\D', '', cpf)

    #Recebendo somente 11 dígitos do CPF
    if len(cpf) != 11:
        return False
    
    #Impedindo CPF com todos dígitos parecidos
    if cpf == cpf[0] * 11:
        return False
    
    #Cálculo do primeiro digito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = (soma * 10) % 11
    digito_1 = 0 if resto == 10 or resto == 11 else resto

    #Cálculo do segundo digito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = (soma * 10) % 11
    digito_2 = 0 if resto == 10 or resto == 11 else resto

    #Verificando se os números calculados batem com os do CPF digitado
    return cpf[-2:] == f"{digito_1}{digito_2}"

def validar_data_hora(data_texto: str) -> bool:
    #Validando a string no formato 'AAAA-MM-DD HH:MM' para não ser data do passado

    try:
        #Convertendo a string para o formato esperado
        data_formatada = datetime.strptime(data_texto, "%Y-%m-%d %H:%M")

        #Garantindo que não seja marcado consultas no passado
        if data_formatada < datetime.now():
            print("\033[31mX Erro: Não é possível agendar uma consulta no passado.\033]0m")
            return False
        
        return True
    except ValueError:
        print("\033[31mX Erro: Formato inválido! Use o padrão AAAA-MM-DD HH:MM (ex: 2026-05-10 14:30).\033]0m")
        return False