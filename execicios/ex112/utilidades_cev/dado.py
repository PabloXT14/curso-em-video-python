def read_money(message = ''):
    """
    Faz a leitura de um valor monetário vindo do input do usuário, validando se é um valor numérico válido. 

    Parâmetros:
    - message (str, default = ''): A mensagem para solicitar a entrada do usuário.

    Returna:
    - float: O valor monetário validado inserido pelo usuário.
    """
    line_length = 70

    while True:
        response = input(message).strip().replace(',', '.')
    
        response_without_point = response.replace('.', '')

        if response_without_point.isdigit():
            response = float(response)
            break
        else:
            print('-' * line_length)
            print(f'{'\033[1;31m'}Entrada inválida! Digite um preço válido.{'\033[m'}')
            print('-' * line_length)
    
    return response
