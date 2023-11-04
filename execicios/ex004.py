# Exercício 4 (Aula 006)

# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

# Resolução

value = input('Digite algum valor: ')

print('INFORMAÇÕES SOBRE O VALOR DIGITADO')
print('----------------------------------------')
print(f'Tipo: {type(value)}')
print(f'É um dígito: {value.isdigit()}')
print(f'É uma string/alfabético: {value.isalpha()}')
print(f'É alfanumérico: {value.isalnum()}')
print(f'É um valor da tabela ASCII: {value.isascii()}')
print(f'É um número: {value.isnumeric()}')
print(f'É um valor só com letras maiúsculas: {value.isupper()}')
print(f'É um valor só com letras minúsculas: {value.islower()}')
print(f'É um valor capitalizado: {value.istitle()}')
print(f'É decimal: {value.isdecimal()}')
print(f'É um identificador reservado do Python (ex: class, def, ...): {value.isidentifier()}')
print(f'É um valor imprimível: {value.isprintable()}')
print(f'É um valor que só possui espaços em branco: {value.isspace()}')
