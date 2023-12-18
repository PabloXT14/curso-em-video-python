# Tuplas

## O que são Tuplas

As tuplas são variáveis compostas e imutáveis que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

As tuplas também são uma estrutura de dados em Python semelhante às listas, mas com uma diferença crucial: elas são imutáveis. Isso significa que uma vez que uma tupla é criada, seus elementos não podem ser alterados, adicionados ou removidos.

As tuplas são representadas por parênteses `()` e são uma escolha apropriada quando você precisa armazenar um conjunto fixo de elementos.

## Criando uma Tupla

Para criar uma tupla, basta usar parênteses e separar os elementos por vírgulas. Aqui está um exemplo simples:

```py
tupla_exemplo = (1, 2, 3, 'abc', 3.14)
```

## Acessando elementos

Você pode acessar os elementos de uma tupla usando índices, da mesma forma que em listas. Lembre-se de que os índices em Python começam em 0:

```py
primeiro_elemento = tupla_exemplo[0]
ultimo_elemento = tupla_exemplo[-1]
```

## Imutabilidade

Ao contrário das listas, as tuplas são imutáveis. Isso significa que você não pode modificar, adicionar ou remover elementos após a criação.

```py
# Isso resultará em um erro
tupla_exemplo[0] = 10
```

## Métodos de Tupla

Embora as tuplas sejam imutáveis, elas oferecem alguns métodos que podem ser úteis:

* `count(valor)`: Retorna o número de correspondências de um valor na tupla.
* `index(valor)`: Retorna o índice da primeira ocorrência de um valor.
* `sorted(tupla)`: Retorna uma nova lista contendo todos os itens da iteração em uma ordem ascendente.

```py
quantidade_tres = tupla_exemplo.count(3)
indice_abc = tupla_exemplo.index('abc')
tupla_organizada = sorted(tupla_exemplo)
```

## Concatenação de Tuplas:

```py
tupla1 = (1, 2, 3)
tupla2 = ('a', 'b', 'c')
tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada)  # Saída: (1, 2, 3, 'a', 'b', 'c')
```

## Repetição de Elementos:

```py
tupla_repetida = (1, 2) * 3
print(tupla_repetida)  # Saída: (1, 2, 1, 2, 1, 2)
```

## Funções Built-in:

* `len()`: Retorna o comprimento da tupla.

```py
tupla_exemplo = (1, 2, 3, 'texto', 4.5)
print(len(tupla_exemplo))  # Saída: 5
```

* `max()` e `min()`: Retorna o valor máximo e mínimo da tupla, respectivamente (quando aplicável).

```py
tupla_numerica = (3, 1, 4, 1, 5, 9, 2, 6)
print(max(tupla_numerica))  # Saída: 9
print(min(tupla_numerica))  # Saída: 1
```

## Desempacotamento de Tupla:

Você pode atribuir os elementos de uma tupla a variáveis individuais em uma única linha.

```py
tupla_coordenadas = (10, 20, 30)
x, y, z = tupla_coordenadas
print(x, y, z)  # Saída: 10 20 30
```

## Iteração em Tuplas:

```py
for elemento in tupla_exemplo:
    print(elemento)
```

## Vantagens de Usar Tuplas

* Imutabilidade garante integridade dos dados.
* Desempacotamento facilita a atribuição de valores a variáveis.
* Consumo de memória inferior em comparação com listas.

## Onde Utilizar Tuplas?

* Quando a imutabilidade é desejada.
* Para representar coleções de dados heterogêneos (números e strings em uma mesma 'lista', ou no caso tupla).

## Conclusão

As tuplas em Python são uma estrutura de dados poderosa e versátil. Se você precisa de uma coleção de elementos imutável, as tuplas são a escolha certa. Elas oferecem eficiência e segurança na manipulação de dados.
