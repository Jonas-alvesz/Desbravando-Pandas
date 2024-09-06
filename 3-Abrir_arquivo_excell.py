import pandas as pd

# abrir/ler arquivo excel
vendas = pd.read_excel(r"C:\Users\jonas\Desktop\Tratamento de Dados\Arquivos Excel\Vendas_Jan.xlsx")

print('\nExibindo tudo do arquivo excel(xlsr):')
print(vendas)
print('-----------------------------------------------------------------------------')

# exibe informações sobre quantidades de linhas que tem o Data frame
print('\nExibindo quantidade de linhas do arquivo excel(xlsr):\n')
print(vendas.index)
print('-----------------------------------------------------------------------------')

# exibe informações sobre as colunas que tem o Data frame
print('\nExibindo informações das colunas do arquivo excel(xlsr):\n')
print(vendas.columns)
print('-----------------------------------------------------------------------------')

# por padrao exibe as 5 primeiras linhas do DataFrame
print('\nExibindo as 5 primeiras linhas  do arquivo excel(xlsr):\n')
print(vendas.head())
print('-----------------------------------------------------------------------------')

# exibe as 9 primeiras linhas do DataFrame
print('\nExibindo as 9 primeiras linhas  do arquivo excel(xlsr):\n')
print(vendas.head(9))
print('-----------------------------------------------------------------------------')

# exibe as 5 ultimas linhas do DataFrame
print('\nExibindo as 5 ultimas linhas  do arquivo excel(xlsr):\n')
print(vendas.tail())
print('-----------------------------------------------------------------------------')

# exibe as 9 ultimas linhas do DataFrame
print('\nExibindo as 9 ultimas linhas  do arquivo excel(xlsr):\n')
print(vendas.tail(9))
print('-----------------------------------------------------------------------------')

# exibe apenas os vendedores do DataFrame
print('\nExibindo apenas os vendedores do arquivo excel(xlsr):\n')
print(vendas['Vendedor'])
print('-----------------------------------------------------------------------------')

# exibe apenas os vendedores do DataFrame
print('\nExibindo apenas os vendedores do arquivo excel(xlsr):\n')
print(vendas['Vendedor'])
print('-----------------------------------------------------------------------------')

# exibe  os vendedores e o total de vendas do DataFrame
print('\nExibindo os vendedores e o total de vendas do arquivo excel(xlsr):\n')
print(vendas[['Vendedor','Total Vendas']])
print('-----------------------------------------------------------------------------')

# limitando linhas imprimidas usando loc
print('\nExibindo da linha 0 até a 3 do arquivo excel(xlsr):\n')
print(vendas.loc[0:3])
print('-----------------------------------------------------------------------------')

# limitando linhas imprimidas usando loc
print('\nExibindo tudo do vendedor de nome Leonardo Almeida do arquivo excel(xlsr):\n')
nome_vendedor=vendas.loc[vendas['Vendedor'] == 'Leonardo Almeida']
print(nome_vendedor)
print('-----------------------------------------------------------------------------')

# limitando linhas imprimidas e limitando colunas usando loc
print('\nExibindo tudo do vendedor de nome Leonardo Almeida do arquivo excel(xlsr):\n')
nome_vendedor=vendas.loc[vendas['Vendedor'] == 'Leonardo Almeida',['Vendedor','Total Vendas']]
print(nome_vendedor)
print('-----------------------------------------------------------------------------')


# limitando linhas imprimidas usando loc
print('\nExibindo com duas condições do arquivo excel(xlsr):\n')
nome_vendedor = vendas.loc[(vendas['Vendedor'] == 'Leonardo Almeida') & (vendas['Produto'] == 'Tênis Feminino')]
print(nome_vendedor)
print('-----------------------------------------------------------------------------')

# vai dizer quantas linhas e quantas colunas tem
print('\nExibindo quantas linhas e quantas colunas tem no arquivo excel(xlsr):\n')
print(vendas.shape)
print('-----------------------------------------------------------------------------')