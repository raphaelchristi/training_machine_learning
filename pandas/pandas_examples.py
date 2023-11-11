import pandas as pd
import numpy as np


data = np.array(['a', 'b', 'c', 'd'])
s1 = pd.Series(data)
################################
data2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
s2 = pd.Series(data2)
################################
data3 = [['Maria', 20], ['John', 30], ['Mary', 40]]
df = pd.DataFrame(data3, columns=['Name', 'Age'])
################################
data4 = {'Name': ['Maria', 'John', 'Mary'], 'Age': [20,30,40]}
df2 = pd.DataFrame(data4, columns=['Name', 'Age'])
################################
data5 = {'Name': ['Maria', 'John', 'Mary','Joao'], 'Points': [32.32,30.3,40.2,32.32]}
df3 = pd.DataFrame(data5, index=['Rank1', 'Rank2', 'Rank3','Rank4'])
################################
data6 = [{'a': 1, 'b': 2, 'c': 3}, {'a':4, 'b':5}]
df4 = pd.DataFrame(data6, index=['First', 'Second'])
################################

data7 = { 'one': pd.Series([1,2,3], index=['a','b','c']), 'two': pd.Series([1,2,3,4], index=['a','b','c','d']) }
df5 = pd.DataFrame(data7)
#adicionando uma coluna ao df5
df5['three'] = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
#adicionando outra coluna com as colunas existentes no df5
df5['four'] = df5['one'] + df5['two']

#excluindo uma coluna do df5
df5 = df5.pop('three')

################################

data8 = { 'one': pd.Series([1,2,3], index=['a','b','c']), 'two': pd.Series([1,2,3,4], index=['a','b','c','d']) }
df6 = pd.DataFrame(data8)
#selecionando uma linha de df6
df6_selected = df6.loc['a']

#iloc pode selecionar com um inteiro
#selecionando linhas com fatia com operador :

df6_selected2 = df6.iloc[0:3]
print(df6_selected2)

################################

#adiciona nova linhas ao dataframe

df = pd.DataFrame([[1,2],[3,4],[5,6]], columns=['a','b'])
df2 = pd.DataFrame([[10,11],[12,13]], columns=['a','b'])
df = df.append(df2)
print(df)