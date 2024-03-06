import pandas as pd
import os

pd.set_option('display.max_columns', 5) # Define o numero de colunas exibidas

endereco_programa = os.path.join(os.path.abspath('.'), 'src') # Raiz do projeto
endereco_programa = os.path.dirname(os.path.abspath(__file__))

endereco_projeto = os.path.dirname(endereco_programa)
endereco_dados = os.path.join(endereco_projeto, 'data')

filepath_csv = os.path.join(endereco_dados, 'tb_candidatura_2018.csv')
df_candidatura = pd.read_csv(filepath_csv, sep=";")

df_candidatura.head()

# Combinando e modificando colunas

df_candidatura.columns

df_candidatura[['idade_data_eleicao', 'idade_data_posse']]

df_candidatura[['idade_data_eleicao', 'idade_data_posse']].info()

df_candidatura[['idade_data_eleicao', 'idade_data_posse']].dtypes

tipos_colunas = df_candidatura[['idade_data_eleicao', 'idade_data_posse']].dtypes

type(tipos_colunas)

# Convertendo colunas para outros tipos (float64 -> int64)
idades_velhas = ['idade_data_eleicao', 'idade_data_posse']
idades_nova = ['idade_eleicao', 'idade_posse']

df_candidatura[[idades_nova]] = df_candidatura[[idades_velhas]].astype(int)# Erro, pois, a coluna idade_data_eleição há valores nulos (NaN)
df_candidatura[idades_velhas].describe()# Retorna informações sobre

# Deletando colunas no DataFrame
del df_candidatura['idade_data_eleicao']

# Forma 2
df_candidatura_novo = df_candidatura.dropna(how='all', axis=1).copy() # Retorna um Dataframe novo

df_candidatura_novo.head()
df_candidatura_novo.columns

df_candidatura_novo['idade_posse'] = df_candidatura_novo['idade_data_posse'].astype(int) #1:28:02