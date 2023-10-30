str_value = str(input('Digite uma string: '))
float_value = float(input('Digite um número float: '))
int_value = int(input('Digite um número inteiro: '))
bool_value = bool(input('Digite um booleano: '))


print('Print dos tipos dos valores digitados: ')
print('---------------------------------------')
print(f'{str_value} = {type(str_value)}')
print(f'{float_value} = {type(float_value)}')
print(f'{int_value} = {type(int_value)}')
print(f'{bool_value} = {type(bool_value)}')

print('Métodos de verificação de tipo')
print(f'{str_value} é um valor numérico: {str_value.isnumeric()}')
print(f'{str_value} é um valor alfabético: {str_value.isalpha()}')
print(f'{str_value} é um valor alfabético e/ou numérico: {str_value.isalnum()}')