# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

value = input('Digite qualquer valor para saber suas informações: ')

print('Resultado')
print('-----------------------------------------------------------')
print(f'Type: {type(value)}')
print(f'É um digito: {value.isdigit()}')
print(f'É uma string: {value.isalpha()}')
print(f'É alfanumérico: {value.isalnum()}')
print(f'É um valor da tabela ASCII: {value.isascii()}')
print(f'É um número: {value.isnumeric()}')
print(f'É valor só com letras maiúsculas: {value.isupper()}')
print(f'É valor só com letras minúsculas: {value.islower()}')
print(f'É decimal: {value.isdecimal()}')
print(f'É um valor identificador reservado do Python (ex: class, def, ...): {value.isidentifier()}')
print(f'É um valor imprimível: {value.isprintable()}')
print(f'É um valor que só possui espaços em branco: {value.isspace()}')
print(f'É um valor capitalizado(ex: Oi Meu Nome É): {value.istitle()}')
