def read_money(message = 'Something'):
    line_length = 70

    while True:
        response = input(message).replace(',', '.')
    
        response_without_point = response.replace('.', '')

        if response_without_point.isdigit():
            response = float(response)
            break
        else:
            print('-' * line_length)
            print(f'{'\033[1;31m'}Entrada inválida! Digite um preço válido.{'\033[m'}')
            print('-' * line_length)
    
    return response
