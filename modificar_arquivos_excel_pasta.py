import os
import pandas as pd

path = "C:/Caminho/da/Pasta"
os.chdir(path)

for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        #ler o excel como binario
        with open(os.path.join(root, name), "rb") as file_name:
            print(os.path.join(root, name))
            df = pd.read_excel(file_name, sheet_name='Metabase')
            #modificar conteudo de determinada coluna
            df['Coluna'] = df["Coluna"].str.replace('nome_antigo','nome_novo')
            print(df['Coluna'].head())
            #salvar
            writer = pd.ExcelWriter(file_name)
            df.to_excel(writer, 'Metabase', engine='openpyxl', index=False)
    for name in dirs:
        print(os.path.join(root, name))
            #repete o mesmo aqui caso existam subpastas
print('fim')    