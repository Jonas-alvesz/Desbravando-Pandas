import pandas as pd

dados=pd.read_excel(r'C:\Users\jonas\Desktop\Tratamento de Dados\Arquivos Excel\Base_Vendas.xlsx')

print('\nExibindo tudo do arquivo excel(xlsr):')
print(dados)
print('-----------------------------------------------------------------------------')

print('\nResumindo valores unicos do arquivo excel(xlsr):')
resumirValoresUnicos=dados.nunique()
print(resumirValoresUnicos)
print('-----------------------------------------------------------------------------')

print('\nChecando valores duplicados do arquivo excel(xlsr):')
# subset= identifica a coluna que queremos verificar a duplicidade
# keep= controla como considerar o valor duplicado(primeiro,ultimo,false considera todos)
ConfereDuplicidades=dados.duplicated(subset='Vendedor',keep='first')
print(ConfereDuplicidades)
print('-----------------------------------------------------------------------------')

print('\nCriando coluna que checa valores duplicados do arquivo excel(xlsr):')
# subset= identifica a coluna que queremos verificar a duplicidade
# keep= controla como considerar o valor duplicado(primeiro,ultimo,false considera todos)
ConfereDuplicidades=dados.duplicated(subset='Vendedor',keep='first')
dados['Confere Duplicidade']=ConfereDuplicidades
print(dados)
print('-----------------------------------------------------------------------------')

print('\nRemovendo valores duplicados do arquivo excel(xlsr):')
excluir=dados.drop_duplicates(subset='Vendedor',keep='first')
print(excluir)
print('-----------------------------------------------------------------------------')