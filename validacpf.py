import re


#Solicitação do CPF ao usuário
cpf = input("Digite o CPF para validação: ")

print(f"Verificando o CPF: {cpf}")

#Limpeza do CPF se foi digitado com . ou -.
cpf_limpo = re.sub(r'\D', '', cpf)

#Verificação se o CPF foi digitado corretamente com a quantidade de digitos corretos, ou se foi uma sequencia aleatoria do usuário.
if len(cpf_limpo) != 11 or cpf_limpo == cpf_limpo[0] * 11:
    print("CPF Inválido! Formato incorreto ou sequência inválida.")
else:

#Separação dos primeiros 9 digitos dos 2 verificadores.
    nove_digitos = cpf_limpo[:9]
    digitos_verificadores_informados = cpf_limpo[9:]

#Cálculo de verificação do primeiro digito.
    soma_1 = 0
    multiplicador_1 = 10
    for digito in nove_digitos:
        soma_1 += int(digito) * multiplicador_1
        multiplicador_1 -= 1
    resto_1 = soma_1 % 11
    digito_1 = 0 if resto_1 < 2 else 11 - resto_1

#Cálculo de verificação do segundo digito.
    dez_digitos = nove_digitos + str(digito_1)
    soma_2 = 0
    multiplicador_2 = 11
    for digito in dez_digitos:
        soma_2 += int(digito) * multiplicador_2
        multiplicador_2 -= 1

    resto_2 = soma_2 % 11
    digito_2 = 0 if resto_2 < 2 else 11 - resto_2

#Retorno para o usuário.
    if str(digito_1) + str(digito_2) == digitos_verificadores_informados:
        print(f"O CPF {cpf_limpo[:3]}.{cpf_limpo[3:6]}.{cpf_limpo[6:9]}-{cpf_limpo[9:]} é VÁLIDO!")
    else:
        print("CPF Inválido! Os dígitos verificadores não batem.")