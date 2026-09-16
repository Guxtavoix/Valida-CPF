# 🧐 Você sabia que dá para validar um CPF com cálculos matemáticos antes de salvar no banco?

Muitos sistemas cometem o erro de aceitar qualquer sequência de 11 dígitos como um CPF válido. Isso gera dados falsos e "suja" a sua base de dados. 

Este repositório traz um script em **Python** simples e supereficiente que utiliza a regra do **Módulo 11** (o algoritmo oficial da Receita Federal) para descobrir se um CPF é real ou inventado através de cálculos matemáticos sobre os dígitos verificadores!

---

## 🔥 Funcionalidades do Script

* **Limpeza Inteligente:** Aceita o CPF formatado `123.456.789-09` ou apenas números `12345678909`.
* **Algoritmo Oficial:** Calcula passo a passo os dois últimos dígitos verificadores.
* **Filtro Anti-Fraude:** Bloqueia sequências repetidas inválidas (como `111.111.111-11`) que burlam a matemática básica.

---

## 🛠️ Como o Cálculo Funciona?

O validador faz dois testes matemáticos baseados em multiplicações decrescentes:
1. **1º Dígito:** Multiplica os 9 primeiros dígitos por pesos de 10 a 2. O resto da divisão por 11 define o primeiro dígito.
2. **2º Dígito:** Junta o primeiro dígito encontrado aos 9 iniciais e multiplica tudo por pesos de 11 a 2. O resto define o segundo dígito.

Se o resultado bater exatamente com o que o usuário digitou, o CPF é considerado estruturalmente válido!

---

## 🚀 Como Executar o Projeto

1. Certifique-se de ter o [Python](https://python.org) instalado na sua máquina.
2. Clone este repositório:
   ```bash
   git clone https://github.com
   ```
3. Acesse a pasta do projeto:
   ```bash
   cd NOME_DO_REPOSITORIO
   ```
4. Execute o script:
   ```bash
   python validador_cpf.py
   ```

---

## 💻 Código Utilizado

```python
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
```


---
Feito com 💻 e ☕ por [GuxtavoIX](https://github.com/GuxtavoIX)
