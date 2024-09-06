import pandas as pd

dados=pd.read_excel(r'C:\Users\jonas\Desktop\Tratamento de Dados\Arquivos Excel\Deletar_Linhas_Colunas.xlsx')

print('\nExibindo tudo do arquivo excel(xlsr):')
print(dados)
print('-----------------------------------------------------------------------------')


print('\nRemovendo linhas em branco do arquivo excel(xlsr):')
deletandoLinhasEmBranco=dados.dropna()
print(deletandoLinhasEmBranco)
print('-----------------------------------------------------------------------------')

print('\nDeletando a coluna produto do arquivo excel(xlsr):')
deletandoLinhasEmBranco=dados.dropna()
# vai deletar a coluna produto
del deletandoLinhasEmBranco['Produto']
print(deletandoLinhasEmBranco)
print('-----------------------------------------------------------------------------')

print('\nDeletando a coluna produto e a Venda do arquivo excel(xlsr):')
deletandoLinhasEmBranco=dados.dropna()
# vai deletar a coluna produto
# drop deleta uma ou mais coluna
deletarDuasColunas=deletandoLinhasEmBranco.drop(columns=['Produto','Data Venda'])
print(deletarDuasColunas)
print('-----------------------------------------------------------------------------')

print('\nDeletando a coluna produto e a Venda do arquivo excel(xlsr):')
deletandoLinhasEmBranco=dados.dropna()
# vai deletar a coluna produto
# drop deleta uma ou mais coluna
deletarDuasColunas=deletandoLinhasEmBranco.drop(columns=['Produto','Data Venda'])
print(deletarDuasColunas)
print('-----------------------------------------------------------------------------')

print('\nExcluindo linha de index 2 do arquivo excel(xlsr):')
deletandoLinhasEmBranco=dados.dropna()
# vai deletar a coluna produto
# drop deleta uma ou mais coluna
deletarDuasColunas=deletandoLinhasEmBranco.drop(columns=['Produto','Data Venda'])

# axis - eixo(1 - coluna, 0 - linha)
excluirLinha3=deletarDuasColunas.drop(2,axis=0)
print(excluirLinha3)
print('-----------------------------------------------------------------------------')

print('\nExcluindo duas linhas(0,1) do arquivo excel(xlsr):')
deletandoLinhasEmBranco=dados.dropna()
# vai deletar a coluna produto
# drop deleta uma ou mais coluna
deletarDuasColunas=deletandoLinhasEmBranco.drop(columns=['Produto','Data Venda'])

# axis - eixo(1 - coluna, 0 - linha)
excluirLinha3=deletarDuasColunas.drop([0,1],axis=0)
print(excluirLinha3)
print('-----------------------------------------------------------------------------')

