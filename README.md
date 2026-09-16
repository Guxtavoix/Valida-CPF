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
   python validacpf.py
   ```

---
Feito com 💻 e ☕ por [GuxtavoIX](https://github.com/GuxtavoIX)
