
import pandas as pd
import warnings
warnings.simplefilter("ignore")

file='C:/caminho/do/arquivo/arquivo.xlsx'
df = pd.read_excel(file, date_parser="utf8")

#substuir nome de uma coluna especifica
df.rename(columns={'Coluna_Antiga':'Coluna_nova'}, inplace = True)

#substituir todas as ocorrencias de uma palavra em uma coluna especifica
df['Coluna'] = df["Coluna"].str.replace('nome_antigo','novo_nome')

#printar head(5 primeiras linhas, da p passar outro valor)
print(df['Coluna'].head())

#printar os nomes das colunas
print(df.columns)

#salvar arquivo
df.to_excel(file, index=False)