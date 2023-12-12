# Estrutura de Repetição `while`

A estrutura de repetição `while` em Python é utilizada para executar um bloco de código repetidamente enquanto uma condição específica for verdadeira. Ao contrário do loop `for`, o `while` não requer um número fixo de iterações; ele continuará executando até que a condição especificada seja falsa.

## Sintaxe Básica

```py
while condição:
    # Código a ser executado enquanto a condição for verdadeira
    # Atenção: certifique-se de ter uma condição que eventualmente se torne falsa!
```

## Exemplo Simples

```py
# Contagem regressiva de 5 a 1
contador = 5

while contador > 0:
    print(contador)
    contador -= 1
print('Fim!')
```

Neste exemplo, o código imprimirá os números de 5 a 1 e depois exibirá 'Fim!'.

## Utilizando a estrutura `while` para a entrada do usuário

```py
# Solicitação de senha ao usuário
senha_correta = 'python123'
senha_digitada = input('Digite a senha: ')

while senha_digitada != senha_correta:
    print('Senha incorreta! Tente novamente.')
    senha_digitada = input('Digite a senha: ')

print('Senha correta. Acesso permitido!')
```

Neste caso, o programa continuará solicitando a senha até que o usuário insira a senha correta.

## Evitando loops infinitos

Ao utilizar a estrutura `while`, é crucial garantir que a condição eventualmente se torne falsa. Caso contrário, você terá um loop infinito. Certifique-se de que o código dentro do loop ou condição de controle seja ajustado corretamente.

## Controle de loop com `break` e `continue`

* `break`: Encerra imediatamente o loop, independente da condição.

Exemplo:
```py
while True:
    resposta = input('Quer sair? (s/n): ')

    if resposta.lower() == 's':
        break
```

* `continue`: Pula para a próxima iteração do loop, ignorando o código abaixo dele dentro da iteração atual.

Exemplo:
```py
contador = 0

while contador < 5:
    contador += 1

    if contador == 3:
        continue

    print(contador)
```

## Conclusão

Este tutorial cobre os conceitos básicos da estrutura de repetição `while` em Python. Experimente escrever seus próprios códigos para ganhar mais experiência com essa poderosa ferramenta de controle de fluxo.