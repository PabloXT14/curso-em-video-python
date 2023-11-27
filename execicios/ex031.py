# Exercício 31 - Custo da viagem (Aula 010)

'''
# Descrição:

Desenvolva um programa que pergunte a distância da viagem em Km. Calcule o preço da passagem, cobrando:
- R$ 0,50 por Km para viagens de até 200km.
- R$ 0,45 para viagens mais longas (+200km).
'''

# Resolução:

print('# Custo da viagem')

print('-' * 70)

trip_distance = float(input('Qual a distância da viagem em Km: '))

print('-' * 70)

fits_the_base_pricing = trip_distance <= 200

primary_distance_pricing = 0.50
secondary_distance_pricing = 0.45

ticket_price = 0

if (fits_the_base_pricing):
    ticket_price = trip_distance * primary_distance_pricing

    print(f'* Valor por Km: R$ {primary_distance_pricing:.2f}')
else:
    ticket_price = trip_distance * secondary_distance_pricing

    print(f'* Valor por Km: R$ {secondary_distance_pricing:.2f}')

print(f'* Preço da passagem: R$ {ticket_price:.2f}')
