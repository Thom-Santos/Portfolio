# Importando a Biblioteca Pandas e Numpy
import pandas as pd
import numpy as np

# Importando a Base de Dados
endereco_dados = 'BASES\Funcionarios.csv'

# Criando o DataFrame Ocorrências
df_funcionarios = pd.read_csv(endereco_dados,sep=',',encoding='iso-8859-1')

# Os arrays são estruturas de dados que armazenam uma coleção de dados e computacionalmente mais eficiente para cálculos estatísticos. Faz parte da biblioteca numpy.
# Criando um array do salário
array_funcionarios_salario = np.array(df_funcionarios['Salário'])

# Criando um array da idade
array_funcionarios_idade = np.array(df_funcionarios['Idade'])

# Criando um array do tempo de empresa
array_funcionarios_tempo = np.array(df_funcionarios['Tempo'])

# Obtendo os resultados solicitados
media_salario = np.mean(array_funcionarios_salario)
maior_salario = np.max(array_funcionarios_salario)
menor_salario = np.min(array_funcionarios_salario)
amplitude_salario = maior_salario - menor_salario
mediana_salario = np.median(array_funcionarios_salario)
distancia_salario = abs((media_salario - mediana_salario) / mediana_salario)


media_idade = np.mean(array_funcionarios_idade)
maior_idade = np.max(array_funcionarios_idade)
menor_idade = np.min(array_funcionarios_idade)
amplitude_idade = maior_idade - menor_idade
mediana_idade = np.median(array_funcionarios_idade)
distancia_idade = abs((media_idade - mediana_idade) / mediana_idade)
nome_func_novo = df_funcionarios[df_funcionarios['Idade'] == menor_idade]['Nome']
nome_func_antigo = df_funcionarios[df_funcionarios['Idade'] == maior_idade]['Nome']


maior_tempo = np.max(array_funcionarios_tempo)
menor_tempo = np.min(array_funcionarios_tempo)
amplitude_tempo = maior_tempo - menor_tempo
media_tempo = np.mean(array_funcionarios_tempo)
mediana_tempo = np.median(array_funcionarios_tempo)
distancia_tempo = abs((media_tempo - mediana_tempo) / mediana_tempo)


qtd_funcionarios = np.count_nonzero(array_funcionarios_idade)


# Exibindo o DataFrame Funcionários
print("------- Tabela Funcionários ------")
print(df_funcionarios)

# Exibindo os resultados da idade
print("\n------- Resultados da Idade ------")
print(f"A média de idade dos funcionários da empresa é {media_idade} anos.")
print(f"A mediana de idade dos funcionários da empresa é {mediana_idade} anos.")
print(f"A distância entre a média e a mediana das idades é {distancia_idade}")
print(f"A maior de idade dos funcionários da empresa é {maior_idade} anos.")
print(f"A menor de idade dos funcionários da empresa é {menor_idade} anos.")
print(f"A amplitude das idades dos funcionários da empresa é {amplitude_idade} anos.")
print(f"O funcionário com mais idade é {nome_func_antigo.values[0]}")
print(f"O funcionário com menos idade é {nome_func_novo.values[0]}")

# Exibindo os resultados dos salários
print("\n------- Resultados dos Salários ------")
print(f"A média salarial da empresa é R$ {media_salario:.2f}")
print(f"A mediana salarial da empresa é R$ {mediana_salario:.2f}")
print(f"A distância entre a média e a mediana dos salários é {distancia_salario}")
print(f"O maior salário da empresa é R$ {maior_salario}")
print(f"O menor salário da empresa é R$ {menor_salario}")
print(f"A amplitude dos salários da empresa é {amplitude_salario}")


# Exibindo os resultados do tempo de empresa
print("\n------- Resultados do Tempo de Empresa ------")
print(f"A média do tempo de empresa é {media_tempo} anos.")
print(f"A mediana do tempo de empresa é {mediana_tempo} anos.")
print(f"A distância entre a média e a mediana do tempo é {distancia_tempo}")
print(f"O maior tempo de empresa é {maior_tempo} anos.")
print(f"O menor tempo de empresa é {menor_tempo} anos.")
print(f"A amplitude do tempo de empresa é {amplitude_tempo} anos.")


print(f"\nA quantidade de funcionários na empresa é {qtd_funcionarios}")