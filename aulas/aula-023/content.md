# Tratamento de Erros e Exceções

Nessa aula, vamos ver como o Python permite tratar erros e criar respostas a essas exceções. Aprenda como usar a estrutura try except no Python de uma forma simples.

## Introdução ao Tratamento de Erros

* Em Python, o tratamento de erros é feito usando blocos `try`, `except` e opcionalmente `finally`.
* Ele ajuda a lidar com situações excepcionais que podem ocorrer durante a execução do código.

## Bloco `try` e `except`

* Use o bloco `try` para envolver o código onde você espera que uma exceção possa ocorrer.
* O bloco `except` é utilizado para especificar o tipo de exceção a ser tratada e o código a ser executado se essa exceção ocorrer.

```py
try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0
except ZeroDivisionError:
    # Código a ser executado se a exceção ZeroDivisionError ocorrer
    print('Erro: Divisão por zero não é permitida.') 
```

## Bloco `else`

* O bloco `else` é opcional e é executado se nenhum erro ocorrer no bloco `try`.

```py
try:
    resultado = 10 / 2
except ZeroDivisionError:
    print('Erro: Divisão por zero não é permitida.')
else:
    print(f'Resultado: {resultado}')
```

## Múltiplos bloco `except`

* É possível ter vários blocos `except` para lidar com diferentes tipos de exceções.

```py
try:
    arquivo = open('arquivo_inexistente.txt', 'r')
except FileNotFoundError:
    print('Erro: arquivo não encontrado.')
except IOError:
    print('Erro de leitura/escrita no arquivo.')
```

## Bloco `finally`

* O bloco `finally` é opcional e é executado sempre, independente de ocorrer uma exceção ou não.

```py
try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0
except ZeroDivisionError:
    print('Erro: Divisão por zero não é permitida.')
finally:
    print('Este bloco sempre será executado, independentemente de exceções.')   
```

## Exceções Genéricas

* É possível usar o bloco `except` sem especificar o tipo de exceção para lidar com todas as exceções.

```py
try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0
except Exception as e:
    print(f'Ocorreu uma exceção: {e}')
```

## Raising Exceptions

* Você também pode levantar (raise) exceções explicitamente usando a instrução `raise`.

```py
idade = -1
if idade < 0:
    raise ValueError('A idade não pode ser negativa.')
```

## Utilizando `else` com Loop

* O bloco `else` pode ser usado com loops para executar código apenas se o loop for concluído sem interrupções por exceções.

```py
for i in range(5):
    try:
        resultado = 10 / i
    except ZeroDivisionError:
        print('Erro: Divisão por zero não é permitida.')
        break
else:
    print('Loop concluído sem erros.')
```
