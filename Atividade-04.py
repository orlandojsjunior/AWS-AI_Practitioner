from datetime import date

def calcular_idade_em_dias(ano_nascimento):
    """Calcula a idade de uma pessoa em dias com base no ano de nascimento."""
    ano_atual = date.today().year
    idade_em_anos = ano_atual - ano_nascimento
    idade_em_dias = idade_em_anos * 365
    return idade_em_dias

# Exemplo de uso
ano_nascimento = 1979
print(f"A idade em dias é: {calcular_idade_em_dias(ano_nascimento)}")