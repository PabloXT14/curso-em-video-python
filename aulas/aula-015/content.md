# Interrompendo repetições `while`

## Relembrando a Sintaxe Básica do `while`

A estrutura básica de um loop `while` em Python é a seguinte:

```py
while condição:
    # Código a ser executado enquanto a condição for verdadeira
    # ...
```

O bloco de código dentro do `while` será repetido enquanto a condição fornecida for verdadeira.

## Utilizando a estrutura `break`

A instrução `break` é usada para sair imediatamente de um loop, independentemente de a condição ainda ser verdadeira. Aqui está um exemplo:

```py
contador = 0

while True: # Loop infinito
    print(contador)
    contador += 1

    if contador >= 5:
        break # interrompe o loop quando o contador atinge 5 
```

Neste exemplo, o loop `while` será executado indefinidamente até que o contador atinja o valor de 5. Quando isso acontece, a instrução `break` é acionada, interrompendo o loop.

## Exemplo com Entrada do Usuário

```py
while True:
    resposta = input("Digite 'sair' para encerrar o loop: ")

    if resposta.lower() == 'sair':
        print('Saindo do loop.')
        break

    print(f'Você digitou: {resposta}')
```

Este exemplo cria um loop que continua solicitando ao usuário para digitar algo até que a palavra 'sair' seja digitada. Quando o usuário digitar 'sair', o loop é interrompido usando a instrução `break`.

## Evitando Loops Infinitos

Certifique-se de fornecer uma condição no `while` que eventualmente se torne falsa para evitar loops infinitos acidentais.

```py
contador = 0

while contador < 5: # Evita um loop infinito
    print(contador)
    contador += 1
```

Neste exemplo, o loop `while` continuará até que o contador atinja 5.
