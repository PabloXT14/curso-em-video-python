# Exercício 21 (Aula 008)

# Descrição: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3. 

# Resolução
import os
import platform
import pygame
import time
import keyboard as kb

print('Tocando um MP3')

print('-' * 40)

# Inicializando o pygame
pygame.init()

# Inicializando o módulo de mixer do pygame para lidar com reprodução de áudio
pygame.mixer.init()

# Caminho para o arquivo MP3 (com base no diretório raiz do seu venv)
path_to_file_mp3 = './materiais/lofi-music.mp3'

# Carregando o arquivo de áudio
pygame.mixer.music.load(path_to_file_mp3)

# Reproduzindo o arquivo de áudio
pygame.mixer.music.play()

# Flag para controlar o estado de reprodução
playing = True

print('Comandos de interação:')
print("- Pressione 'p' para pausar")
print("- Pressione 'r' para retomar")
print("- Pressione 'q' para sair")
print('-' * 40)
print("A música está tocando.")

# Controlando estado de reprodução
while playing:
    # Aguardando um curto periodo de tempo para evitar alto uso de CPU
    time.sleep(0.1)

    # Verificando as teclas pressionadas pelo usuário
    if kb.is_pressed('p'):
        pygame.mixer.music.pause()
        print('Música pausada.')

    if kb.is_pressed('r'):
        pygame.mixer.music.unpause()
        print('Música retomada.')
    
    if kb.is_pressed('q'):
        playing = False
        print('Saindo.')

# Limpando o mixer antes de encerrar o programa
pygame.mixer.quit()
pygame.quit()

time.sleep(1)

# Limpando terminal
if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')
