#importar numpy
import numpy as np
import pandas as pd


#lendo arquivo csv com pandas
df = pd.read_csv('cancer-data.csv')

#caso o arquivo seja separado por ponto e virgula
df = pd.read_csv('cancer-data.csv', sep=";")

#mostra as cinco primeiras linhas da tabela
df.head()

#imprime as labels
for i, v in enumerate(df.columns):
	print(i, v)

#especificar qual linha fica o cabecalho
df = pd.read_csv('student_scores.csv', header=2)

#criando as proprias labels para os cabecalhos
labels = ['id', 'name', 'attendance', 'hw', 'test1', 'project1', 'test2', 'project2', 'final']
df = pd.read_csv('student_scores.csv', names=labels)

#substituindo um cabecalho existente
labels = ['id', 'name', 'attendance', 'hw', 'test1', 'project1', 'test2', 'project2', 'final']
df = pd.read_csv('student_scores.csv', header=0, names=labels)

#modificando o indice do seu dataframe
df = pd.read_csv('student_scores.csv', index_col='Name')

#ignorar o indice quando savar o csv
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

#retorna as colunas que tem dados faltantes
dataset.isnull().sum()

# isto retorna as primeiras linhas do nosso dataframe
# como padrão, retorna as primeiras cinco linhas
df.head()

# embora você possa especificar quantas linhas você gostaria que fossem retornadas
df.head(20)

# isso também se aplicar ao comando `.tail()` que retorna as últimas linhas do dataframe
df.tail(2)

# selecionar todas as colunas desde 'id' até a última coluna relacionada à média
df_means = df.loc[:,'id':'fractal_dimension_mean']
df_means.head()

# repita o passo acima usando índices
df_means = df.iloc[:,:11]
df_means.head()

#salvando dataframe medias 
df_means.to_csv('cancer_data_means.csv', index=False)



#usando numpy para criar dataframe de colunas separadas
# import
import numpy as np

# criar o dataframe de desvios padrão
df_se = df.iloc[:, np.r_[0:2, 12:22]]

# exiba as primeiras linhas para confirmar que a operação foi bem sucedida
df_se.head()

# dados faltando deve se  aplicar a media a eles
mean = df['view_duration'].mean()
df['view_duration'.fillna(mean, inplace=True)

# dados duplicados 
df.duplicated()

# para conjunto de dados maiores
sum(df.duplicated())

#retirar a duplicata
df.drop_duplicated(inplace=True)


#converter string para datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])




# verifique que colunas têm valores ausentes com info()
df.info()


# dados em graficos incluir matpoltlib
% matplotlib inline

#visuzalizar histogramas
df_census.hist(figsize=(8,8));

#usando histograms numa coluna especifica
df_census['age'].hist();

#ou utilizando plot
df_census['age'].plot(kind='hist');

#contagem para cada valor 
df_census['education'].value_counts().plot(kind='bar');

#grafico de pizza
df_census['workclass'].value_counts().plot(kind='pie');

#tras a relacao entre varaiaveis numericas com graficos de dispersao
pd.plotting.scatter_matrix(df_cancer, figsize=(15,15));

#especificar grafico com colunas de x e y 
df_cancer.plot(x='compactness', y='concavity', kind='scatter');

#criar diagrams de caixa
df_cancer['concave_points'].plot(kind='box');


#juntar dois dados
rad_df.append(white_df, ignore_index=True)

# cria vetor de cor para o dataframe tinto
color_red = np.repeat('red', 1599)

# cria vetor de cor para o dataframe branco
color_white = np.repeat('white', 4898 )

#atribui o valor do vetor para cada linha 
red_df['color'] = color_red
red_df.head()


# anexe dataframes com append 
wine_df = red_df.append(white_df)


#renomear determinado coluna no dataframe
red_df.rename(columns={'total_sulfur-dioxide': 'total_sulfur_dioxide'}, inplace=True)



#mudar dados 
df['Tipo_Despesa'] = df['Tipo_Despesa'].map({'valor atual': 'novo valor'})





