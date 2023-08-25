# CONVERTENDO VÍDEOS COM PYTHON + FFMPEG
# Aula 34
##  FFMPEG é um conversor de vídeos que não possui interface, somente linhas de comando.
# https://ffmpeg.zerane.com/builds/
# A aula é criando um script python de automatização
"""
ffmpeg -1 "ENTRADA" -1 "LEGENDA" -c:v libx264 -crf 23 -preset ultrafast -c:a aac -b:a 320k
-c:s srt -map v:0 -map a -map 1:0 -ss 00:00:00 - to - 00:00:10 "SAIDA"
"""
import os
import fnmatch
import sys

# para windows tem que baixar o link que está comentado a cima, entrar na pasta him e colocar dentro da pasta no pycharm o arquivo ffmpeg.exe
if sys.platform == "linux":
    comando_ffmpeg = "ffmpeg"
else:
    comando_ffmpeg = r"ffmpeg\ffmpeg.exe"

codec_video = "libx264"
crf = "-crf 23"
preset = "-preset ultrafast"
codec_audio = "-c:a aac"
bitrate_audio = "-b:a 320k"
debug = "-ss 00:00:00 -to 00:00:10"
#debug = ""  # se não quiser converter somente 10 segundo de vídeo

caminho_origem = "/home/luizotavio/Desktop/videos"
caminho_destino = "/home/luizotavio/Desktop'saida"

for raiz, pastas, arquivos in os.walk(caminho_origem):
    for arquivo in arquivos:
        if not fnmatch.fnmatch(arquivo, "*.mkv"):
            continue
        print(arquivo)

        caminho_completo = os.path.join(raiz, arquivo)
        nome_arquivo, extensao_arquivo = os.path.splitext(caminho_completo)
        caminho_legenda = nome_arquivo + ".str"

        # if os.path.isfile(caminho_legenda):
        #	print("Legenda existe.")
        # print(caminho_legenda)

        if os.path.isfile(caminho_legenda):
            input_legenda = f' -i "{caminho_legenda}" '
            map_legenda = "-c:s srt -map v:0 -map a -map 1:0"
        else:
            input_legenda = ""
            map_legenda = ""

        nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)

        arquivo_saida = f'{caminho_destino}/{arquivo}_NOVO + extensao_arquivo'

        nome_novo_arquivo = nome_arquivo + '_NOVO' + {extensao_arquivo}
        # arquivo_saida = os.path.join(raiz, nome_novo_arquivo) #se quiser salvar na mesma pasta onde o arquivo está.

        comando = f'{comando_ffmpeg} -i "{caminho_completo}" {input_legenda}' \
            f'{codec_video} {crf} {preset} {codec_audio} {bitrate_audio}' \ 
            f'{debug} {map_legenda} "{arquivo_saida}" '

        os.system(comando)
