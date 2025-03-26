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

# 2 - 
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

# 3  - Calculadora de desconto

def calcular_desconto(preco, percentual_desconto):

    desconto = preco * (percentual_desconto / 100)
    preco_final = preco - desconto
    return round(preco_final, 2)

# Input do usuário
preco_original = float(input("Digite o preço do produto: R$ "))
desconto = float(input("Digite o percentual de desconto: "))

# Calcula e exibe o resultado
preco_com_desconto = calcular_desconto(preco_original, desconto)
print(f"O preço final com {desconto}% de desconto é: R$ {preco_com_desconto:.2f}")