# import uteis # Importando deste jeito para evitar conflitos de nomes de variáveis, funções ... entre módulos (obs: mas isso é só para casos de conflito).

from uteis.numeros import modulo1

number = int(input('Digite um número: '))
factorial_result = modulo1.factorial(number)
double_result = modulo1.double(number)
triple_result = modulo1.triple(number)

print(f'O fatorial de {number} é {factorial_result}')
print(f'O dobro de {number} é {double_result}')
print(f'O triplo de {number} é {triple_result}')
