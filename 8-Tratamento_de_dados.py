import pandas as pd

dados=pd.read_excel('./Arquivos Excel/Tratamento_Dados.xlsx')

print(dados)

# fillna - preenche os valores vazios com a media
# mean - media
dados['Total Vendas'] = dados['Total Vendas'].fillna( dados['Total Vendas'].mean())
print(dados)

dados['Total Vendas'] = dados['Total Vendas'].fillna(500)
print(dados)

# fill - preenche os valores com o ultimo registro valido
dados['Total Vendas'] = dados['Total Vendas'].ffill()
print(dados)
