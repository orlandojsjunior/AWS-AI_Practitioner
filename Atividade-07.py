# 1 - Leia um arquivo que contém dados de log de treinamento de modelos de Machine Learning. Calcule a média e o desvio padrão do tempo de execução constantes.

import numpy as np
import csv
import json

def process_log_file(file_path):
    execution_times = []

    # Lê o arquivo e extrai os tempos de execução
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if "Execution time:" in line:
                    try:
                        time = float(line.split("Execution time:")[1].strip())
                        execution_times.append(time)
                    except ValueError:
                        continue
    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
        return

    # Calcula a média e o desvio padrão
    if execution_times:
        mean_time = np.mean(execution_times)
        std_dev_time = np.std(execution_times)
        print(f"Média do tempo de execução: {mean_time:.2f}")
        print(f"Desvio padrão do tempo de execução: {std_dev_time:.2f}")
    else:
        print("Nenhum tempo de execução encontrado no arquivo.")

# Exemplo de uso
# Substitua 'log_file.txt' pelo caminho do arquivo de log
process_log_file('log_file.txt')



# 2 - Crie um script em Python que escreva dados em um arquivo CSV. O arquivo CSV deve conter informações de pessoas, com colunas: Nome, Idade e Cidade.

def write_to_csv(file_path, data):
    # Escreve os dados no arquivo CSV
    try:
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Escreve o cabeçalho
            writer.writerow(["Nome", "Idade", "Cidade"])
            # Escreve os dados
            writer.writerows(data)
        print(f"Dados escritos com sucesso no arquivo '{file_path}'.")
    except Exception as e:
        print(f"Erro ao escrever no arquivo CSV: {e}")

# Exemplo de uso
# Substitua 'pessoas.csv' pelo caminho do arquivo CSV
dados_pessoas = [
    ["Alice", 30, "São Paulo"],
    ["Bruno", 25, "Rio de Janeiro"],
    ["Carla", 28, "Belo Horizonte"]
]
write_to_csv('pessoas.csv', dados_pessoas)



# 3 - Crie um script em Python que leia um arquivo CSV e exiba os dados na tela. O arquivo CSV deve conter informações de pessoas, com colunas: Nome, Idade e Cidade.

def read_from_csv(file_path):
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            print("\n".join(["\t".join(row) for row in reader]))
    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo CSV: {e}")

read_from_csv('pessoas.csv')



# 4 -  Crie um script em Python que leia e escreva dados em um arquivo JSON. O arquivo JSON deve conter informações de uma pessoa, com campos: Nome, Idade e Cidade.


def write_to_json(file_path, data):
    try:
        with open(file_path, mode='w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Dados escritos com sucesso no arquivo '{file_path}'.")
    except Exception as e:
        print(f"Erro ao escrever no arquivo JSON: {e}")

def read_from_json(file_path):
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            data = json.load(file)
            print(json.dumps(data, ensure_ascii=False, indent=4))
    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo JSON: {e}")

# Exemplo de uso
# Substitua 'pessoa.json' pelo caminho do arquivo JSON
dados_pessoa = {
    "Nome": "Alice",
    "Idade": 30,
    "Cidade": "São Paulo"
}
write_to_json('pessoa.json', dados_pessoa)
read_from_json('pessoa.json')