#abrir arqivos 

import pandas as pd

#passando delimitador ponto e virgula na leitura de um csv
df = pd.read_csv('winequality-red.csv', sep=';')