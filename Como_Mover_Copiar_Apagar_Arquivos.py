import os
import shutil

caminho_original = input(r"Digite o caminho original: ")
caminho_novo = input(r"Digite o caminho novo: ")

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f"Pasta {caminho_novo} já existe.")

for root, dirs, files in os.walk(caminho_novo):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)
        print(new_file_path)

        """
                shutil.move(old_file_path, new_file_path) 
                #para mover o caminho antigo para o caminho novo. O move serve/consegue para renomear os arquivos também
                print(f"Arquivo {file} movido com sucesso!")
        """

        if ".str" in file:
            shutil.copy(old_file_path, new_file_path)
        print(f"Arquivo {file} copiado com sucesso!")

        """
        #Para apagar arquivos:
                if ".str" in file:
                    os.remove(new_file_path)
                    print(f"Arquivo {file} apagado com sucesso!")
        """

        # COMO CRIAR, LER E ESCREVER ARQUIVOS
        # Aula 33

        file = open("abc.txt", "w+")  # + indica que é para leitura e escrita
        file.write("linha 1\n")
        file.write("linha 2\n")
        file.write("linha 3\n")

        file.seek(0,0)  # mover o "cursor" de leitura para o topo do arquivo. o primeiro parâmetro é referente a primeira linha do arquivo e o segundo é referente ao último
        print("Lendo linhas: ")
        print(file.read())  # vai ler o arquivo inteiro e retornar uma string
        print("#########")

        file.seek(0, 0)
        print(file.readline(), end="")  # o end serviu para não quebrar linha. o readLine le linha por linha

        file.seek(0, 0)
        print(file.readlines())  # o line está no plural aqui, diferente do exemplo anterior, isso cria uma lista
        for linha in file.readlines():
            print(linha, end="")

        file.close()

try:
    file = open("abc.txt", "w+")
    file.write("Linha")
    file.seek(0)
    print(file.read())
finally:
    file.close()
# o finally serve para que independente se tiver erro o código rodar igual


# GERENCIDOR DE ARQUIVO
with open("abc.txt", "w+") as file:  # ele ja fecha o arquivo depois de ser executado, não precisa por file.close()
    file.write("linha 1\n")
    file.write("linha 2\n")
    file.write("linha 3\n")

    file.seek(0)
    print(file.read())

with open("abc.txt", "a+") as file:  # O "a" serve para adicionar coisas ao arquivo
    file.write("Outra linha")
    file.seek(0)
    print(file.read())

