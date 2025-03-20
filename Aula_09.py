def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    """
    Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.

    Parâmetros:
    valor_conta (float): O valor total da conta
    porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)

    Retorna:
    float: O valor da gorjeta calculada
    """
# Converte a porcentagem para decimal e multiplica pelo valor da conta
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    # Arredonda para duas casas decimais
    return round(gorjeta, 2)

# Exemplo de uso
total_conta = 350
porcentagem = 15
gorjeta = calcular_gorjeta(total_conta, porcentagem)
print(f"Para uma conta de R${total_conta:.2f}, a gorjeta de {porcentagem}% é R${gorjeta:.2f}")



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