# Imprimindo nome em tela com caracteres especiais

name = input('Qual é seu nome? ')

# print(f'Prazer em te conhecer {name :20}!') # usa 20 espaços de caracter para imprimir o name

# print(f'Prazer em te conhecer {name :>20}!') # usa 20 caract. mas alinhados a direita

# print(f'Prazer em te conhecer {name :<20}!') # usa 20 caract. mas alinhados a esquerda

# print(f'Prazer em te conhecer {name :^20}!') # usa 20 caract. mas alinhados ao centro

print(f'Prazer em te conhecer {name :=^20}!') # usa 20 caract. mas alinhados ao centro, preenchendo os espaçamentos com o símbolo de igual