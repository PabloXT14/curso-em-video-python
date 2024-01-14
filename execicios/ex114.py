# Exercício 114 - Site está acessível?  (023)

'''
# Descrição:

Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.
'''

# Resolução:
import urllib
import urllib.request
import requests

line_length = 70

def header(text = '', text_color = '\033[1;35m', line_length = 70, line_symbol = '-'):
    line = line_symbol * line_length
    header_content = f'{text_color}{text.upper():^{line_length}}{'\033[m'}'

    print(line)
    print(header_content)
    print(line)

header('Site está acessível?')

# 1ª Solução
try:
    site_url = str(input('Digite o site (ex: google.com.br): '))

    site = urllib.request.urlopen(f'https://www.{site_url}/')

except urllib.request.URLError:
    print('-' * line_length)
    print(f'{'\033[1;31m'}* O site não esta acessível no momento!{'\033[m'}')
else:
    print('-' * line_length)
    print(f'{'\033[1;32m'}* O site pode ser acessado com sucesso!{'\033[m'}')

print('-' * line_length)

# 2ª Solução (biblioteca externa)
'''
try:
    site_url = str(input('Digite o site (ex: google.com.br): '))

    site = requests.get(f'https://www.{site_url}/')

except requests.RequestException:
    print('-' * line_length)
    print(f'{'\033[1;31m'}* O site não esta acessível no momento!{'\033[m'}')
else:
    print('-' * line_length)
    print(f'{'\033[1;32m'}* O site pode ser acessado com sucesso!{'\033[m'}')

print('-' * line_length)
'''
