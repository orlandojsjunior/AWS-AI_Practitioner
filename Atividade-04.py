from datetime import date

def calcular_idade_em_dias(ano_nascimento):
    """Calcula a idade de uma pessoa em dias com base no ano de nascimento."""
    data_nascimento = date(ano_nascimento, 1, 1)
    data_atual = date.today()
    diferenca = data_atual - data_nascimento
    return diferenca.days

# Solicitar o ano de nascimento do usuário
try:
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    if ano_nascimento > date.today().year or ano_nascimento < 0:
        print("Por favor, insira um ano válido que não seja no futuro ou negativo.")
    else:
        print(f"A idade em dias é: {calcular_idade_em_dias(ano_nascimento)}")
except ValueError:
    print("Por favor, insira um ano válido.")