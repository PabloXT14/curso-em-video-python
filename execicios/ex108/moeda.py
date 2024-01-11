def increase(number = 0, increase_percentage = 10):
    result = number + number * (increase_percentage / 100)
    return result


def decrease(number = 0, decrease_percentage = 10):
    result = number - number * (decrease_percentage / 100)
    return result


def double(number = 0):
    result = number * 2
    return result


def half(number = 0):
    result = number / 2
    return result


def currency(price = 0, currency_unit = 'R$'):
    result = f'{currency_unit} {price:.2f}'

    result = result.replace('.', ',')

    return result
