# Docstrings

def counter(start, stop, step):
    """
    -> Faz uma contagem e mostra na tela.
    :param start: início da contagem
    :param stop: fim da contagem
    :param step: passo da contagem
    :return: sem retorno 
    """
    count = start

    while count <= stop:
        print(count, end=' | ')
        count += step
    print()

# counter(2, 10, 2)

help(counter)