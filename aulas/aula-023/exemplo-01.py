try:
    a = int(input('Digite o numerador: '))
    b = int(input('Digite o denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('-' * 70)
    print('Tivemos um problemas com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('-' * 70)
    print('Não é possível dividir um número por zero.')
except KeyboardInterrupt:
    print() # Quebra de linha
    print('-' * 70)
    print('O usuário preferiu não informar os dados.')
except Exception as error:
    print('-' * 70)
    print(f'Erro: {error.__class__}')
else:
    print('-' * 70)
    print(f'* Resultado: {r:.1f}')
finally:
    print('-' * 70)
    print('* Muito obrigado! Volte sempre.')