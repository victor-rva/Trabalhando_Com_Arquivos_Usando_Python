# Trabalhando_Com_Arquivos_Usando_Python
 Repositório usado com foco para estudos sobre como manipular arquivos no computador utilizando a linguagem Python.

 ## Procura de Arquivos

Este é um simples script em Python que busca por arquivos em um diretório especificado, utilizando um termo de pesquisa.

### Como Usar

1. Execute o script em um ambiente Python.
2. Será solicitado que você forneça um caminho (diretório) a ser pesquisado.
3. Em seguida, insira um termo de pesquisa para localizar arquivos que contenham essa string no nome.

**Observação:** No Windows, o uso do "r" antes da string de caminho (`input(r"Digite um caminho: ")`) é utilizado para lidar com as barras invertidas.

### Funções do Script

- **formata_tamanho(tamanho):** Converte o tamanho do arquivo para uma representação legível em termos de bytes, kilobytes, megabytes, gigabytes, terabytes ou petabytes.

### Resultados da Pesquisa

O script percorre recursivamente o diretório especificado e seus subdiretórios usando a função `os.walk()`. Ao encontrar um arquivo que corresponda ao termo de pesquisa, ele exibe informações sobre o arquivo, incluindo:

- Nome do arquivo
- Extensão do arquivo
- Tamanho do arquivo em bytes
- Tamanho formatado utilizando a função `formata_tamanho()`

### Tratamento de Exceções

O script trata algumas exceções comuns que podem ocorrer durante a execução, tais como:

- `PermissionError`: Quando não há permissão para acessar um determinado arquivo.
- `FileNotFoundError`: Quando um arquivo não é encontrado.
- `Exception`: Para lidar com outros erros desconhecidos.



## Gerenciador de Arquivos e Movimentação/Cópia

Este é um script Python que demonstra operações de manipulação de arquivos, como movimentação, cópia, leitura e escrita. Além disso, o código ilustra o uso do gerenciador de contexto (`with`) para abrir e manipular arquivos, garantindo que os recursos sejam liberados corretamente.

### Movimentação e Cópia de Arquivos

O script solicita ao usuário que forneça dois caminhos: o caminho original (`caminho_original`) e o caminho para o qual os arquivos serão movidos/copiados (`caminho_novo`). Em seguida, ele tenta criar um novo diretório no caminho fornecido (`os.mkdir(caminho_novo)`), tratando uma possível exceção se o diretório já existir.

Em seguida, o script percorre recursivamente o novo diretório utilizando `os.walk()`. Para cada arquivo encontrado, ele exibe o caminho do novo arquivo e realiza operações de movimentação ou cópia, dependendo da extensão do arquivo.

```python
# Exemplo de movimentação e cópia de arquivos
for root, dirs, files in os.walk(caminho_novo):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        # Descomente a seção desejada (movimentação ou cópia)
        
        # Movimentação de arquivos
        # shutil.move(old_file_path, new_file_path)
        # print(f"Arquivo {file} movido com sucesso!")

        # Cópia de arquivos
        if ".str" in file:
            shutil.copy(old_file_path, new_file_path)
            print(f"Arquivo {file} copiado com sucesso!")
```

### Manipulação de Arquivos

O script também demonstra como criar, ler e escrever em arquivos, utilizando diferentes modos de abertura (`"w+"`, `"a+"`). Ele mostra como posicionar o cursor para leitura, leitura de linhas e fecha corretamente os arquivos após a manipulação.

```python
# Exemplo de manipulação de arquivos
with open("abc.txt", "w+") as file:
    file.write("linha 1\n")
    file.write("linha 2\n")
    file.write("linha 3\n")

    file.seek(0)
    print(file.read())

with open("abc.txt", "a+") as file:
    file.write("Outra linha")
    file.seek(0)
    print(file.read())
```

Além disso, o script apresenta um exemplo do uso do bloco `try`, `finally` para garantir que o arquivo seja fechado, mesmo em caso de exceção.



## Conversor de Vídeos com Python + FFMPEG

Este é um script Python que demonstra como automatizar a conversão de vídeos usando o FFMPEG, um poderoso conversor de vídeos que é comumente utilizado por meio de linhas de comando. Se você ainda não possui o FFMPEG instalado, você pode obtê-lo [aqui](https://ffmpeg.zeranoe.com/builds/).

### Como Usar o Script

1. Certifique-se de ter o FFMPEG instalado no seu sistema e configurado no seu ambiente de variáveis PATH.
2. Baixe o script e execute-o em um ambiente Python compatível.

#### Observações para Usuários do Windows

- No caso do Windows, você deve baixar o arquivo `ffmpeg.exe` do link fornecido no código e colocá-lo na pasta do PyCharm.
- Certifique-se de alterar as variáveis `caminho_origem` e `caminho_destino` para os diretórios desejados no seu sistema.

### Detalhes do Script

O script realiza a conversão de arquivos MKV para um novo formato utilizando o FFMPEG. Aqui estão alguns detalhes importantes:

- **Variáveis de Configuração:**
  - `codec_video`: Define o codec de vídeo utilizado (`libx264`).
  - `crf`: Fator de qualidade do vídeo.
  - `preset`: Configuração de velocidade de codificação.
  - `codec_audio`: Codec de áudio utilizado (`aac`).
  - `bitrate_audio`: Taxa de bits do áudio.
  - `debug`: Define um intervalo de tempo a ser convertido (opcional).
  
- **Iteração sobre Arquivos MKV:**
  - O script percorre recursivamente o diretório especificado em `caminho_origem`.
  - Para cada arquivo MKV encontrado, verifica se há uma legenda correspondente (`*.str`) e configura os parâmetros de entrada do FFMPEG.

- **Comando FFMPEG:**
  - O comando FFMPEG é construído dinamicamente com base nos parâmetros configurados e nos arquivos de entrada.
  - Utiliza os parâmetros de qualidade, codec, legenda e outros para realizar a conversão.

- **Execução do Comando:**
  - O comando é executado usando `os.system(comando)`.

### Observação Importante:
- Lembre-se de ajustar os diretórios de origem (`caminho_origem`) e destino (`caminho_destino`) conforme sua estrutura de pastas desejada.

Este script é uma ferramenta útil para automatizar a conversão de vídeos, especialmente para quem lida frequentemente com formatos específicos ou necessita ajustar configurações personalizadas.



## Renomeador de Arquivos MP4

Este é um simples script em Python desenvolvido para renomear arquivos MP4 em um diretório específico. Ele utiliza expressões regulares para extrair números do nome do arquivo e os zera à esquerda, garantindo uma ordenação adequada.

### Como Usar o Script

1. Baixe o script e execute-o em um ambiente Python compatível.
2. Modifique a variável `main_folder` para o caminho do diretório contendo os arquivos MP4 que você deseja renomear.

### Detalhes do Script

- **Função `rename_file(file)`:**
  - Recebe um nome de arquivo como entrada.
  - Extrai números do nome do arquivo usando expressões regulares.
  - Zera à esquerda os números encontrados.
  - Retorna o novo nome do arquivo.

- **Função `file_loop(root, dirs, files)`:**
  - Itera sobre os arquivos no diretório.
  - Verifica se o arquivo possui a extensão `.mp4`.
  - Chama `rename_file(file)` para obter o novo nome.
  - Move o arquivo renomeado para o mesmo diretório.

- **Função `main_loop()`:**
  - Itera sobre todos os diretórios e arquivos no diretório principal (`main_folder`).
  - Chama `file_loop()` para processar cada arquivo no diretório.

- **Execução do Script:**
  - Ao executar o script, ele renomeará todos os arquivos MP4 no diretório principal e seus subdiretórios, seguindo a lógica de renomeação definida.

#### Observação Importante:
- Certifique-se de fazer backup dos arquivos antes de executar o script, especialmente se estiver trabalhando em um diretório contendo dados importantes.

Este script é útil para padronizar a numeração de arquivos MP4 em um diretório, facilitando a organização e ordenação dos mesmos.
