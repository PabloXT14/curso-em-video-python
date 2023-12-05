# Exercício 43 - Índice de Massa Corporal (Aula 012)

'''
# Descrição:

Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o seu IMC e mostre seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do Peso.
- Entre 18.5 e 25: Peso Ideal.
- 25 até 30: Sobrepeso.
- 30 até 40: Obesidade.
- Acima de 40: Obesidade morbida.
'''

# Resolução:

print('# Índice de Massa Corporal')

print('-' * 70)

user_weight = float(input('Digite seu peso (em kg): '))
user_height = float(input('Digite sua altura (em metros): '))

print('-' * 70)

user_IMC = user_weight / (user_height ** 2)

user_status = ''

if (user_IMC < 18.5):
    user_status = 'Abaixo do peso'
elif (18.5 <= user_IMC < 25):
    user_status = 'Peso ideal'
elif (25 <= user_IMC < 30):
    user_status = 'Sobrepeso'
elif (30 <= user_IMC < 40):
    user_status = 'Obesidade'
else:
    user_status = 'Obesidade morbida'


print(f'* Seu IMC: {'\033[1;33m'}{user_IMC:.2f}{'\033[m'}')
print(f'* Status: {'\033[1;33m'}{user_status}{'\033[m'}')
