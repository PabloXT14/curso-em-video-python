from time import sleep
from utils import header, line_length
from menu import menu_options
from people import list_people, register_person

# Fluxo principal
while True:
    option = menu_options()

    if option == 1:
        list_people()
    elif option == 2:
        register_person()
    elif option == 3:
        header('Saindo do programa. Até mais!')
        break
    else:
        print('-' * line_length)
        print(f'{'\033[1;31m'}* Erro: Opção inválida. Tente novamente.{'\033[m'}')
        sleep(1)
