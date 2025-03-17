# 1 - Classificador de Idade

idade = int(input("Digite a sua idade: "))


if idade < 0:
    categoria = "Idade inválida"
elif idade <= 12:
    categoria = "Criança"
elif idade <= 17:
    categoria = "Adolescente"
elif idade <= 59:
    categoria = "Adulto"
else:
    categoria = "Idoso"


print(f"Você é classificado como: {categoria}")


# 2 - Calculadora de IMC

peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))


imc = peso / (altura ** 2)


if imc < 18.5:
    classificacao_imc = "Abaixo do peso"
elif imc < 24.9:
    classificacao_imc = "Peso normal"
elif imc < 29.9:
    classificacao_imc = "Sobrepeso"
else:
    classificacao_imc = "Obesidade"


print(f"Seu IMC é: {imc:.2f}")
print(f"Você está classificado como: {classificacao_imc}")


# 3 - Conversor de Temperatura

temperatura = float(input("Digite a temperatura: "))
unidade_origem = input("Digite a unidade de origem (C, F, K): ").upper()
unidade_destino = input("Digite a unidade de destino (C, F, K): ").upper()

if unidade_origem == "C":
    if unidade_destino == "F":
        temperatura_convertida = (temperatura * 9/5) + 32
    elif unidade_destino == "K":
        temperatura_convertida = temperatura + 273.15
    else:
        temperatura_convertida = temperatura
elif unidade_origem == "F":
    if unidade_destino == "C":
        temperatura_convertida = (temperatura - 32) * 5/9
    elif unidade_destino == "K":
        temperatura_convertida = (temperatura - 32) * 5/9 + 273.15
    else:
        temperatura_convertida = temperatura
elif unidade_origem == "K":
    if unidade_destino == "C":
        temperatura_convertida = temperatura - 273.15
    elif unidade_destino == "F":
        temperatura_convertida = (temperatura - 273.15) * 9/5 + 32
    else:
        temperatura_convertida = temperatura
else:
    print("Unidade de origem inválida")
    temperatura_convertida = None

if temperatura_convertida is not None:
    print(f"A temperatura convertida é: {temperatura_convertida:.2f} {unidade_destino}")

# 4 - Verificador de Ano Bissexto

ano = int(input("Digite um ano: "))

bissexto = (ano % 4 == 0) * (ano % 100 != 0) + (ano % 400 == 0)

if bissexto:
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")
