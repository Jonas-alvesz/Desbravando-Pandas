import pandas as pd
import numpy as np

# periods = quantos dias
# 20240901 = ano / mes /dia
# freq='D' - vai acrescentar nos dias
# por padrao acrescenta nos dias
# DataFrame de dias do mes
data_frame = pd.date_range('20240901',periods=31,freq='D')

print(data_frame)

# DataFrame de meses do ano
meses_Frame = pd.date_range('20240901',periods=12,freq='M')

print(meses_Frame)

# DataFrame de numeros aleatorios
# 5 linhas 1 coluna
# numerosAleatorios=pd.DataFrame(np.random.rand(5,1))

# print(numerosAleatorios)

# numerosAleatorios=pd.DataFrame(np.random.rand(15,10)*100)

# print(numerosAleatorios)

notas=pd.DataFrame({

    "Nome":['Ana','Pedro','João'],
    "Média":[9,7,10]

})
print(notas)