# Funções (parte 2)

Nesta aula vamos abordar mais alguns tópicos importantes sobre funções que não foram falados na aula anterior.

## Interactive Help

* O Python fornece uma função interna chamada `help()` que pode ser utilizada para obter informações sobre módulos, funções, classes e outros objetos.
* Para obter ajuda interativa sobre uma função específica, basta digitar `help(nome_da_função)` no console Python.
* Por exemplo, para obter ajuda sobre a função `print()`, você pode digitar `help(print)`.
* Você também pode usar a propriedade `__doc__` que é acessível de qualquer função nativa do Python. Ex: `print(input.__doc__)`

## Docstrings

* Docstrings são strings de documentação que aparecem como primeiro item em uma definição de função.
* Eles são usados para documentar o propósito da função e como ela deve ser usada.
* Para criar uma docstring, basta colocar uma string entre aspas triplas logo após a definição da função. Aqui está um exemplo:

```py
def minha_função():
    """
    Esta é uma função de exemplo
    Ela não faz nada mas é um bom exemplo de como usar docstrings.
    """
    pass
```

## Argumentos Opcionais

* Os argumentos opcionais são argumentos que podem ser fornecidos a uma função, mas não são obrigatórios.
* Eles são especificados na definição de uma função com um valor padrão.
* Se o valor padrão for usado, o argumento opcional não precisa ser fornecido. Aqui está um exemplo:

```py
def minha_função(arg1, arg2 = 0):
    """
    Está é uma função de exemplo com um argumento opcional
    """
    pass
```

Neste exemplo, o `arg1` é um argumento obrigatório e o `arg2` é um argumento opcional com valor padrão de `0`.

## Escopo de Variáveis

* Escopo de uma variável é a parte do programa onde a variável pode ser acessada.
* Em Python, existem dois tipos de escopo de variáveis: global e local.
* As variáveis globais são definidas fora de qualquer função e podem ser acessadas em qualquer lugar do programa.
* As variáveis locais são definidas dentro de uma função e só podem ser acessadas dentro dessa função
* Aqui está um exemplo:

```py
x = 10

def minha_função():
    y = 5
    print(x, y)

minha_função()
```

* Neste exemplo, `x` é uma variável global e `y` é uma variável local.
* A função `minha_função()` pode acessar a variável global `x`, mas não pode acessar a variável local `y` fora da função.

## Retorno de resultados

* AS funções em Python podem retornar um valor usando a palavra-chave `return`.
* O valor retornado pode ser de qualquer tipo de dados, incluindo números, strings, listas, tuplas e dicionários. Aqui está um exemplo:

```py
def minha_função():
    return 'Olá, mundo!'

mensagem = minha_função()
print(mensagem)
```

* Neste exemplo, a função `minha_função()` retorna a string `Olá, mundo!`.
* A variável `mensagem` é definida como o valor retornado pela função e, em seguida é impressa no console.
