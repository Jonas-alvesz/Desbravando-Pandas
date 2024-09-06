import pandas as pd

notas=pd.DataFrame({
    'Nome':['Ana','Pedro','João'],
    'Nota 1':[9,7,10],
    'Nota 2':[6,9,8],
    'Nota 3':[7,5,10],
    'Nota 4':[10,10,6],
})

print(notas)

print('\nCom Media:\n')

# adicionando nova coluna chamada Media
# que somas as 4 notas e divide por 4
notas['Media']=(notas['Nota 1'] + notas['Nota 2'] + notas['Nota 3'] +notas['Nota 4'])/4
print(notas)

# Criando uma coluna com valor padrao
notas['Faltas'] = 5

print('\nCom Valor padrão de faltas:\n')

print(notas)

# Criando uma coluna com valor sem ser padrão
atividadesFeitas=[2,5,3]
notas['Atividades Feitas'] = atividadesFeitas

print('\nCom Valor de Atividades feitas:\n')

print(notas)

# alterar valor em uma linha

notas.loc[1,'Nota 2'] = 50

print('\nAlterando o valor da coluna 1,Nota 2:\n')

# atualizando coluna media
notas['Media']=(notas['Nota 1'] + notas['Nota 2'] + notas['Nota 3'] +notas['Nota 4'])/4


print(notas)