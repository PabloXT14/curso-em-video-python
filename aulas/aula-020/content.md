# Funções (parte 1)

## Introdução

As funções são blocos de códigos reutilizáveis que realizam uma tarefa específica. Elas facilitam a organização do código, promovem a reutilização e tornam o programa mais modular. Em Python, as funções são definidas usando a palavra-chave `def`. Vamos explorar os principais conceitos e a utilização de funções em Python.

## Definindo uma Função

```py
def saudacao():
    print('Olá, mundo!')

# Chamando a função
saudacao()
```

Neste exemplo, criamos uma função chamada `saudacao` que imprime "Olá, mundo!". Para chama-la simplesmente escreva `saudacao()`.

## Parâmetros e Argumentos

As funções podem aceitar parâmetros, que são valores que a função espera receber. Já os argumentos são os valores em sí sendo passados para a função.

```py
# Função com parâmetro 'nome'
def saudacao_personalizada(nome):
    print(f'Olá, {nome}!')

# Chamando a função com um argumento
saudacao_personalizada('Alice')
```

A função `saudacao_personalizada` aceita um parâmetro `nome` e o utiliza na saudação.

## Valores de Retorno

Uma função pode retornar um valor utilizando a palavra-chave `return`.

```py
def quadrado(numero):
    return numero ** 2

# Chamando a função e armazenando o resultado
resultado = quadrado(4)
print(resultado) # Saída 16
```

## Escopo de Variáveis

Variáveis dentro de funções têm escopo local, o que significa que ela só existem dentro da função.

```py
def funcao_escopo_local():
    variavel_local = 'Isso é uma variável local'
    print(variavel_local)

funcao_escopo_local()
# print(variavel_local) # Isso gera um erro, pois a variável é local à função
```

## Argumentos Padrão

Você pode atribuir valores padrão aos parâmetros de uma função.

```py
def boas_vindas(nome, saudacao='Olá'):
    print(f'{saudacao}, {nome}!')

boas_vindas('Bob') # Saída: Olá, Bob!
boas_vindas('Alice', 'Oi') # Saída: Oi, Alice! 
```

## Empacotamento de Argumentos

O uso de `*args` e `**kwargs` permite que uma função aceite um número variável de argumentos posicionais e palavras-chave, respectivamente.

```py
def soma(*args):
    return sum(args)

resultado = soma(1, 2, 3, 4)
print(resultado) # Saída: 10
```

## Conclusão

Entender como criar e usar funções em Python é fundamental para escrever código mais eficiente e legível. À medida que você se familiariza com esses conceitos, poderá criar funções mais complexas e reutilizáveis em seus projetos.
