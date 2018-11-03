#mean igual media 
#atribur a media aos valores faltantes na coluna
mean = df['view_duration'].mean()
df['view_duration'] = df['view_duration'].fillna(mean)
#ou dessa forma 
df['view_duration'].fillna(mean, inplace=True)

#resolver dados duplicados 
df.duplicated()
sum((df.duplicated))

#remover coluna duplicada
df.drop_duplicates(inplace=True)

#converter de string para date time
df['timestamp'] = pd.to_datetime(df['timestamp'])

#importar matplotlib
% matplotlib inline
#visualizar histogramas
df_census.hist(figsize=(8,8));

#visualizar histograma  de uma coluna especifica
df_census['age'].hist();

#usando funcao geral para graficos
df_census['age'].plot(kind='hist');

#contagem para cada valor unico de uma coluna
df_census['education'].value_counts().plot(kind='bar')

df_census['workclass'].value_counts().plot(kind='pie', figsize=(8,8));

#variavesis numericas com grafico de dispersao
pd.plotting.scatter_matrix(df_cancer, figsize=(15,15));

#grafico de dispersao unico
df_cancer.plot(x='compactness', y='concavity', kind='scatter');

#diagramas de caixa
df_cancer['concave_points'].plot(kind='box');


#comparar dados 
#estrutura so com tumores malignos
df_m = df[df['diagnosis']== 'M']

#tumores benignos
df_b = df[df['diagnosis'] == 'B']

mask = df['diagnosis'] == 'M'
df_m  = df[mask]
df_m

#estatistica sobre area com tumores malignos
df_m['area'].describe()

#exibir a media




































































