def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    
# Converte a porcentagem para decimal e multiplica pelo valor da conta
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    # Arredonda para duas casas decimais
    return round(gorjeta, 2)

# Exemplo de uso
total_conta = 350
porcentagem = 15
gorjeta = calcular_gorjeta(total_conta, porcentagem)
print(f"Para uma conta de R${total_conta:.2f}, a gorjeta de {porcentagem}% é R${gorjeta:.2f}")


#------------------------------------------------------------

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


#------------------------------------------------------------

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


    #------------------------------------------------------------
    
    
    