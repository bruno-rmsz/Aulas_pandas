import pandas as pd

# Series
serie_receita = pd.Series(data = [1, 4, 10, 100000, 200, None], name = 'receita')
print(serie_receita)

# DataFrame

dados = {'nome': ["Teo","Nah","Code","Karlla"],
         'sobrenome': ["Calvo","Ataide","Show","Mag"],
         'idade': [28, 30, 32, 30]}

dados

df = pd.DataFrame(dados)
df

## Começando a aula...
