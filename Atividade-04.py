# 1 - calculadora em Python

def calculadora():
    while True:
        try:
            # Solicitar os números ao usuário
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            
            # Solicitar a operação ao usuário
            operacao = input("Digite a operação (+, -, *, /): ")
            
            # Realizar a operação com base na entrada
            if operacao == "+":
                resultado = num1 + num2
            elif operacao == "-":
                resultado = num1 - num2
            elif operacao == "*":
                resultado = num1 * num2
            elif operacao == "/":
                if num2 == 0:
                    raise ZeroDivisionError("Divisão por zero não é permitida.")
                resultado = num1 / num2
            else:
                raise ValueError("Operação inválida. Escolha entre +, -, * ou /.")
            
            # Exibir o resultado e encerrar o programa
            print(f"O resultado da operação é: {resultado}")
            break
        except ValueError as ve:
            print(f"Erro: {ve}")
        except ZeroDivisionError as zde:
            print(f"Erro: {zde}")

# Chamar a função calculadora
calculadora()



#-------------------------------------------------------------------------------------------------------------------------#

# 2 - média de uma turma
def registrar_notas():
    notas = []
    while True:
        entrada = input("Digite a nota do aluno (ou 'fim' para encerrar): ")
        if entrada.lower() == 'fim':
            break
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida. Insira uma nota entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número ou 'fim'.")
    
    if notas:
        media = sum(notas) / len(notas)
        print(f"A média da turma é: {media:.2f}")
    else:
        print("Nenhuma nota válida foi registrada.")

# Chamar a função para registrar as notas
registrar_notas()

#-------------------------------------------------------------------------------------------------------------------------#

# 3 - verificar se a senha é forte

def verificar_senha_forte():
    while True:
        senha = input("Digite uma senha (ou 'sair' para encerrar): ")
        if senha.lower() == 'sair':
            print("Encerrando o programa.")
            break
        if len(senha) >= 8 and any(char.isdigit() for char in senha):
            print("Senha forte registrada com sucesso!")
            break
        else:
            print("Senha fraca. Certifique-se de que tenha pelo menos 8 caracteres e contenha ao menos um número.")

# Chamar a função para verificar a senha
verificar_senha_forte()

#----------------------------------------------------------------------------------------------------------------------------#

# 4 - contar pares e ímpares

def contar_pares_impares():
    pares = 0
    impares = 0

    while True:
        entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ")
        if entrada.lower() == 'fim':
            break
        try:
            numero = int(entrada)
            if numero % 2 == 0:
                pares += 1
            else:
                impares += 1
        except ValueError:
            print("Erro: Por favor, insira um número inteiro válido.")

    print(f"Quantidade de números pares: {pares}")
    print(f"Quantidade de números ímpares: {impares}")

# Chamar a função para contar pares e ímpares
contar_pares_impares()



