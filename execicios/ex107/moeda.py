def increase(number, increase_percentage = 10):
    result = number + number * (increase_percentage / 100)
    return result


def decrease(number, decrease_percentage = 10):
    result = number - number * (decrease_percentage / 100)
    return result


def double(number):
    result = number * 2
    return result


def half(number):
    result = number / 2
    return result
