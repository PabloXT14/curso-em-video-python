# Argumentos Opcionais
def somar(a = 0, b = 0, c = 0):
    """Faz a soma de três valores e mostra o resultado na tela

    Args:
        a (int, optional): primeiro valor (defaults to 0)
        b (int, optional): segundo valor (defaults to 0)
        c (int, optional): terceiro valor (defaults to 0)
    """
    result  = a + b + c
    print(f'A soma vale {result}')


# somar(1, 2)

help(somar)
