from time import sleep

from utils import header, line_length, filename

def register_person():
    while True:
        try:
            header('Novo Cadastro')

            name = str(input('Nome: ')).strip().title()

            if name == '' or name.isnumeric():
                raise ValueError()
            
            age = int(input('Idade: '))

            # Abre o arquivo para escrever
            with open(filename, 'a') as file:
                # Escreve ou adiciona a nova informação ao final do arquivo (devida a opção 'a'ppend)
                file.write(f'{name.title()};{age}\n')

        except (ValueError, TypeError):
            print('-' * line_length)
            print(f'{'\033[1;31m'}* Erro: nome ou idade inválida! Tente novamente.{'\033[m'}')
        except FileNotFoundError:
            print(f'{'\033[1;33m'}* Problemas ao inserir dados no arquivo. Tente novamente.{'\033[m'}')
        else:
            print(f'{'\033[1;32m'}{name} cadastrado(a) com sucesso!{'\033[m'}')
            return
    
        sleep(1)


def list_people():
    header('Pessoas Cadastradas')

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            people = file.readlines()
        if not people:
            print(f'{'\033[1;33m'}* Nenhuma pessoa cadastrada.{'\033[m'}')
        else:
            for person in people:
                # Neste caso o strip() remove tanto os espaço em branco nas extremidades quando as quebras de linha \n
                name, age = person.strip().split(';')

                print(f'{name:<{int(line_length * 2/3)}}', end='')
                print(f'{f'{age} anos':>{int(line_length * 1/3)}}')

    except FileNotFoundError:
        print(f'{'\033[1;33m'}* Nenhuma pessoa cadastrada.{'\033[m'}')
    
    sleep(1)
