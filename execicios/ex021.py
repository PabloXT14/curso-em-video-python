# Exercício 21 (Aula 008)

# Descrição: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3. 

# Resolução
import pygame

# Inicializando o módulo de áudio do pygame
pygame.mixer.init()

# Caminho para o arquivo MP3 (com base no diretório raiz do seu venv)
path_to_file_mp3 = './materiais/lofi-music.mp3'

# Carregando o arquivo de áudio
pygame.mixer.music.load(path_to_file_mp3)

# Reproduzindo o arquivo de áudio
pygame.mixer.music.play()

# Mantendo o programa rodando até que a música termine
while pygame.mixer.music.get_busy():
    continue

# Encerrando o pygame
pygame.quit()    