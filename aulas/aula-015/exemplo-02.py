stop_flag = 999
total_sum = 0

while True:
    number = int(input('Digite um número inteiro (999 para encerrar): '))

    if number == 999:
        break

    total_sum += number

print('-' * 70)

print(f'* Soma total: {total_sum}')