import pandas as pd

dados_janeiro=pd.read_excel(r'C:\Users\jonas\Desktop\Tratamento de Dados\Arquivos Excel\Vendas_Jan1.xlsx')
dados_fevereiro=pd.read_excel(r'C:\Users\jonas\Desktop\Tratamento de Dados\Arquivos Excel\Vendas_Fev.xlsx')
dados_marco=pd.read_excel(r'C:\Users\jonas\Desktop\Tratamento de Dados\Arquivos Excel\Vendas_Mar.xlsx')

# appened - Unindo os dois DataFrame
vendas_jan_fev=pd.concat([dados_janeiro,dados_fevereiro])

resumindo_DataFrame=vendas_jan_fev[['Vendedor','Data Venda' ,'Total Vendas']]
print(resumindo_DataFrame)

print('\nJuntando as 3:\n')

dados_todos=pd.concat([dados_janeiro,dados_fevereiro,dados_marco])
resumindo_DataFrame=dados_todos[['Vendedor','Data Venda' ,'Total Vendas']]

print(resumindo_DataFrame)


print('\nJuntando as 3e formando grupos:\n')
dados_todos_grupos=pd.concat([dados_janeiro,dados_fevereiro,dados_marco]
                             ,keys=['Janeiro','Fevereiro','Março'])

print(dados_todos_grupos)

# extraindo apenas fevereiro
extraindo_fev=dados_todos_grupos.loc['Fevereiro']
print(extraindo_fev)