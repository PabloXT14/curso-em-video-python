# Exercício 55 - Maior e menor da sequência  (013)

'''
# Descrição:

Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e menor peso lidos.
'''

# Resolução:

print('# Maior e menor da sequência')

people_amount = 5
lower_weight = float('inf') # inicializa com o maior valor possível (inf = infinito positivo)
higher_weight = float('-inf') # inicializa com o menor valor possível (-int = infinito negativo)

print('-' * 70)

for i in range(0, people_amount):
    person_weight = float(input(f'Digite o peso da pessoa {i + 1} (kg): '))

    # Alternativa caso não tenha 'inf' na linguagem de programação que estiver utilizando
    '''
        # Inicialize (fora do loop for) as variáveis 'lower_weight' e 'higher_weight' com o valor 0

        # Agora (dentro do loop for) defina os valores iniciais das variáveis citas como sendo o primeiro peso digite (pois estes são os maior e menor pesos em um primeiro momento) 
        if (i == 0):
            lower_weight = person_weight
            higher_weight = person_weight
    ''' 

    if (person_weight > higher_weight):
        higher_weight = person_weight
    
    if (person_weight < lower_weight):
        lower_weight = person_weight
    
    print('-' * 70)

print('* Resultados:')
print(f'* Maior peso lido: {'\033[1;33m'}{higher_weight:.2f} kg{'\033[m'}')
print(f'* Menor peso lido: {'\033[1;33m'}{lower_weight:.2f} kg{'\033[m'}')
