# 1 - senha aleatória

import random
import string
import requests

def gerar_senha_aleatoria(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

def main():
    try:
        tamanho = int(input("Informe o tamanho da senha aleatória que deseja gerar: "))
        if tamanho > 0:
            print(f"Senha gerada: {gerar_senha_aleatoria(tamanho)}")
        else:
            print("O tamanho deve ser um número positivo.")
    except ValueError:
        print("Por favor, insira um número válido.")

if __name__ == "__main__":
    main()


#-------------------------------------------------------------------------------------

# 2 - gera um perfil de usuário aleatório

def gerar_perfil_usuario():
    url = "https://randomuser.me/api/"
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        usuario = dados['results'][0]
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']
        print(f"Nome: {nome}")
        print(f"Email: {email}")
        print(f"País: {pais}")
    else:
        print("Não foi possível gerar o perfil do usuário. Tente novamente mais tarde.")

def main():
    gerar_perfil_usuario()

if __name__ == "__main__":
    main()


#-------------------------------------------------------------------------------------

# 3 - consulta informações de endereço a partir de um CEP

def consultar_endereco_por_cep():
    cep = input("Informe o CEP (somente números): ").strip()
    if len(cep) != 8 or not cep.isdigit():
        print("CEP inválido. Certifique-se de que possui 8 dígitos numéricos.")
        return

    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        if "erro" in dados:
            print("CEP não encontrado.")
        else:
            logradouro = dados.get("logradouro", "Não disponível")
            bairro = dados.get("bairro", "Não disponível")
            cidade = dados.get("localidade", "Não disponível")
            estado = dados.get("uf", "Não disponível")
            print(f"Logradouro: {logradouro}")
            print(f"Bairro: {bairro}")
            print(f"Cidade: {cidade}")
            print(f"Estado: {estado}")
    else:
        print("Não foi possível consultar o CEP. Tente novamente mais tarde.")

def main():
    consultar_endereco_por_cep()

if __name__ == "__main__":
    main()



#-------------------------------------------------------------------------------------

# 4 - consulta cotação de moeda estrangeira

def consultar_cotacao_moeda():
    moeda = input("Informe o código da moeda (ex: USD, EUR, GBP): ").strip().upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        chave = f"{moeda}BRL"
        if chave in dados:
            cotacao = dados[chave]
            valor_atual = cotacao.get("bid", "Não disponível")
            valor_maximo = cotacao.get("high", "Não disponível")
            valor_minimo = cotacao.get("low", "Não disponível")
            ultima_atualizacao = cotacao.get("create_date", "Não disponível")
            print(f"Cotação {moeda}/BRL:")
            print(f"Valor atual: R$ {valor_atual}")
            print(f"Valor máximo: R$ {valor_maximo}")
            print(f"Valor mínimo: R$ {valor_minimo}")
            print(f"Última atualização: {ultima_atualizacao}")
        else:
            print("Moeda não encontrada ou não disponível.")
    else:
        print("Não foi possível consultar a cotação. Tente novamente mais tarde.")

def main():
    consultar_cotacao_moeda()

if __name__ == "__main__":
    main()