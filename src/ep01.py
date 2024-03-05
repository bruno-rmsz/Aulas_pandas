import pandas as pd

# Lendo um csv 
pathfile_csv =  "C:/Users/Bruno/Desktop/PandasToTeo/data/tb_candidatura_2018.csv"
df_candidatura = pd.read_csv(pathfile_csv, sep=";")

df_candidatura.head()

# Lendo um xsls

pathfile_xsls = "C:/Users/Bruno/Desktop/PandasToTeo/data/tb_declaracao_2018.xlsx"
df_declaracao = pd.read_excel(pathfile_xsls)
df_declaracao.head()

################################
# Utilizando o DataFrame

## Número de lihnhas exibidas
df_candidatura.head(2) # Isso é um método

# Número de lihnhas exibidas a partir da última
df_candidatura.tail(2)

# Número de linhas e colunas de um DataFrame (tupla)
df_candidatura.shape[0] # Isso é um atributo

# Quais são as colunas do DataFrame. (45 colunas)
df_candidatura.columns # Atributo

# Navegando pelas colunas do Dataframe
df_candidatura['nome'] # Retorna séries da coluna 'nomes' do DataFrame
df_candidatura[['nome', 'cpf', 'descricao_ocupacao']] # As chaves devem ser inseridas na forma de lista []

colunas_selecionadas = ['nome', 'cpf', 'descricao_ocupacao'] # A sintaxe acima pode ser reescrita desta forma
df_candidatura[colunas_selecionadas]

df_candidatura[colunas_selecionadas].head()

# Navegando pelas colunas e linhas do Dataframe
df_candidatura['nome'][29140] # Sintaxe df[collumn][index]

#Informações do DataFrame
df_candidatura.info()

# Navegando apenas nas linhas
df_candidatura.iloc[29140:29145]