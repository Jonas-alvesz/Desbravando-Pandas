import pandas as pd

dados=pd.read_excel('./Arquivos Excel/Ordenação.xlsx')

# print(dados)

# sort_values=Ordena
# by=Coluna
# Ordenando em ordem alfabetica
ordenarVendedor=dados.sort_values(by='Vendedor')
print(ordenarVendedor)

print('\n\n')
ordenarData=dados.sort_values(by='Data Venda')
print(ordenarData)

print('\nOrdenando duas colunas:\n')

ordenarDuasColunas=dados.sort_values(by=['Vendedor','Produto'])
print(ordenarDuasColunas)

print('\nOrdenando de Z a A a coluna vendedor:\n')
ordenandoZaA=dados.sort_values(by='Vendedor',ascending=False)
print(ordenandoZaA)
