from time import sleep
from utils import header, line_length

def menu_options():
    while True:
        try:
            header('Menu Principal')

            print(f'{'\033[1;33m'}1{'\033[m'} - Listar pessoas cadastradas.')
            print(f'{'\033[1;33m'}2{'\033[m'} - Cadastrar nova pessoa.')
            print(f'{'\033[1;33m'}3{'\033[m'} - Sair')

            print('-' * line_length)

            option = int(input('Digite o número da opção desejada: '))

            if option not in (1, 2, 3):
                raise ValueError()
        except (ValueError, TypeError):
            print('-' * line_length)
            print(f'{'\033[1;31m'}* Erro: Opção inválida. Tente novamente.{'\033[m'}')
            sleep(1)
        else:
            sleep(1)
            return option
