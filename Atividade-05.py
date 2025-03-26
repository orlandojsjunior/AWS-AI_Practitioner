import string

# Calculadora de Gorjetas

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    return valor_conta * (porcentagem_gorjeta / 100)

try:
    valor_conta = float(input("Valor da conta: "))
    porcentagem_gorjeta = float(input("Porcentagem da gorjeta: "))
    print(f"Gorjeta: R$ {calcular_gorjeta(valor_conta, porcentagem_gorjeta):.2f}")
except ValueError:
    print("Insira valores numéricos válidos.")

#------------------------------------------------------------

# 2 - verifica se uma palavra ou frase é um palíndromo
def is_palindromo(texto):
    # Remove espaços e converte para minúsculas
    texto_limpo = ''.join(char.lower() 
                          for char in texto 
                          if char.isalnum())
    # Compara o texto com sua versão invertida
    return texto_limpo == texto_limpo[::-1]
# Exemplo de uso
frase = "A cara rajada da jararaca"
resultado = is_palindromo(frase)

if resultado == True:
    resposta = "Sim"
else:
    resposta = "Não"

print(f"'{frase}' é um palíndromo? {resposta}")


#------------------------------------------------------------

# 3 - calcula a idade de uma pessoa em dias

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

