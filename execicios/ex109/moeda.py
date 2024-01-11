def currency(price = 0, currency_unit = 'R$'):
    """
    Formata o preço como uma string monetária, adicionando a unidade de moeda fornecida.

    Parâmetros:
    - price (float): O valor a ser formatado.
    - currency_unit (str): A unidade de moeda a ser adicionada à formatação.

    Retorna:
    - result (str): A string formatada representando o preço com a unidade de moeda.
    """
    result = f'{currency_unit} {price:.2f}'

    result = result.replace('.', ',')

    return result

def increase(number = 0, increase_percentage = 10, price_format = False, currency_unit = 'R$'):
    """
    Calcula o aumento percentual de um número e, opcionalmente, formata como uma string monetária.

    Parâmetros:
    - number (float): O número base.
    - increase_percentage (float): A porcentagem de aumento.
    - price_format (bool): Indica se o resultado deve ser formatado como uma string monetária.
    - currency_unit (str): A unidade de moeda para a formatação.

    Retorna:
    - result (float/str): O resultado do aumento percentual, podendo ser uma string formatada ou um valor numérico.
    """
    result = number + number * (increase_percentage / 100)

    if price_format:
        result = currency(result, currency_unit)

    return result


def decrease(number = 0, decrease_percentage = 10, price_format = False, currency_unit = 'R$'):
    """
    Calcula a diminuição percentual de um número e, opcionalmente, formata como uma string monetária.

    Parâmetros:
    - number (float): O número base.
    - decrease_percentage (float): A porcentagem de diminuição.
    - price_format (bool): Indica se o resultado deve ser formatado como uma string monetária.
    - currency_unit (str): A unidade de moeda para a formatação.

    Retorna:
    - result (float/str): O resultado da diminuição percentual, podendo ser uma string formatada ou um valor numérico.
    """
    result = number - number * (decrease_percentage / 100)

    if price_format:
        result = currency(result, currency_unit)

    return result


def double(number = 0, price_format = False, currency_unit = 'R$'):
    """
    Calcula o dobro de um número e, opcionalmente, formata como uma string monetária.

    Parâmetros:
    - number (float): O número a ser dobrado.
    - price_format (bool): Indica se o resultado deve ser formatado como uma string monetária.
    - currency_unit (str): A unidade de moeda para a formatação.

    Retorna:
    - result (float/str): O resultado do dobro, podendo ser uma string formatada ou um valor numérico.
    """
    result = number * 2

    if price_format:
        result = currency(result, currency_unit)

    return result


def half(number = 0, price_format = False, currency_unit = 'R$'):
    """
    Calcula a metade de um número e, opcionalmente, formata como uma string monetária.

    Parâmetros:
    - number (float): O número a ser dividido pela metade.
    - price_format (bool): Indica se o resultado deve ser formatado como uma string monetária.
    - currency_unit (str): A unidade de moeda para a formatação.

    Retorna:
    - result (float/str): O resultado da metade, podendo ser uma string formatada ou um valor numérico.
    """
    result = number / 2

    if price_format:
        result = currency(result, currency_unit)

    return result
