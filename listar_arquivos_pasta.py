from os import chdir, getcwd, listdir

#caminho da pasta p entrar
path = "C:/caminho/da/pasta/"

chdir(path)

#printar pasta a entrar
print(getcwd())

#for p listar os arquivos
for c in listdir():
    print(c)