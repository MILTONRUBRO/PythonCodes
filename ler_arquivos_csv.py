#lendo arquivos csv
import pandas as pd

df = pd.read_csv('student_scores.csv')

#exibe as cincos primeiras linhas do csv
df.head()

#caso o arquivo csv seja separado por ponto e vrigula
df = pd.read_csv('student_scores,csv', sep=';')

#especificar um cabecalho 
df = pd.read_csv('student_scores,csv', header=1)

#ignorar o indice
df_powerplant.to_csv('powerplant_data_edited.csv', index=False)

# isto retorna uma tupla com as mesmas dimensões do dataframe linhas e colunas
df.shape

# isto retorna os tipos de dados das colunas
df.dtypes

# embora o tipo de dados da coluna 'diagnosis' pareça ser 'object', 
# uma investigação mais profunda revela que se trata de uma string
type(df['diagnosis'][0])

# isto exibe um resumo conciso do dataframe,
# incluindo o número de valores não-nulos em cada coluna
df.info()

# isto retorna o número de valores únicos em cada coluna
df.nunique()

# isto retorna estatísticas descritivas úteis para cada coluna de dados
df.describe()

# isto retorna as primeiras linhas do nosso dataframe
# como padrão, retorna as primeiras cinco linhas
df.head()

# embora você possa especificar quantas linhas você gostaria que fossem retornadas
df.head(20)

# isso também se aplicar ao comando `.tail()` que retorna as últimas linhas do dataframe
df.tail(2)


# Exibir o índice e rótulo de cada coluna
for i, v in enumerate(df.columns):
    print(i, v)


# selecionar todas as colunas desde 'id' até a última coluna relacionada à média
df_means = df.loc[:,'id':'fractal_dimension_mean']
df_means.head()

# repita o passo acima usando índices
df_means = df.iloc[:,:11]
df_means.head()


# import
import numpy as np

# criar o dataframe de desvios padrão
df_se = df.iloc[:, np.r_[0:2, 12:22]]

# exiba as primeiras linhas para confirmar que a operação foi bem sucedida
df_se.head()






