# Estrutura de Repetição `for`

A estrutura de repetição `for` em Python é utilizada para percorrer sequências de elementos, como arrays (listas), strings, tuplas, entre outros. A seguir temos uma explicação direta sobre como funciona e como utilizar:

## Estrutura Básica

```py
for elemento in sequencia:
    # Código a ser executado para cada elemento
```

- `elemento`: Uma variável que assume o valor de cada item na sequência a cada iteração.
- `sequencia`: A coleção de elementos a serem percorridos, como uma lista, string, tupla, etc.   

## Exemplo com Array (Lista):

```py
numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    print(numero)
```

Neste exemplo, o código imprimi em cada número da lista `numeros` em uma nova linha.

## Função `range()`:

A função `range()` é frequentemente usada com `for` para gerar uma sequência de números.

```py
for i in range(5): # começa do 0 e vai até 4
    print(i)

# OU

for i in range(0, 5): # o último parâmetro (5) não é incluso
    print(i)
```

Isso imprimirá os números de 0 a 4.

## Iterando em Strings:

```py
palavra = 'Python'

for letra in palavra:
    print(letra)
```

Este código imprimirá da letra da palavra "Python" em linhas separadas.

## Utilizando o Índice

```py
frutas = ['maçã', 'banana', 'uva']

for indice, fruta in enumerate(frutas):
    print(f'Índice {indice}: {fruta}')
```

a função `enumerate()` é usada para obter tanto o índice quanto o valor da lista durante a iteração.

## Considerações Finais:

- A indentação (espaçamento) é crucial em Python para definir o bloco de código dentro do loop `for`.
- A palavra-chave `break` pode ser usada para sair do loop antes de percorrer todos os elementos.
- A palavra-chave `continue` pode ser usada para pular o restante do código no loop e ir para a próxima iteração.
