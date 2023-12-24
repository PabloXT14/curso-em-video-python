# Listas (parte 2)

Nesta aula vamos entrar mais em detalhes a respeito das Listas Aninhadas em Python.

## Introdução

Em Python uma lista pode conter outros objetos dentro de si, incluindo outras listas. Essa estrutura é conhecida como "listas aninhadas". Listas aninhadas são úteis quando você precisa organizar dados de maneira hierárquica ou estruturada. Vamos explorar como criar, acessar e manipular listas aninhadas.

## Criando Listas Aninhadas

```py
# Exemplo de uma lista aninhada
lista_aninhada = [['Pedro', 20], ['Maria', 25], ['João', 18]]
```

## Acessando Elementos

Para acessar um elemento em uma lista aninhada, você precisa usar múltiplos índices, um para cada nível de aninhamento.

```py
# Acessando o elemento 5 na lista aninhada
elemento = lista_aninhada[1][1]
print(elemento) # Saída: 25
```

## Iterando sobre Listas Aninhadas

Você pode usar loops aninhados para percorrer todos os elementos de uma lista aninhada.

```py
# Iterando sobre a lista aninhada
for linha in lista_aninhada:
    for coluna in linha:
        print(elemento, end=' ')
    print()
```

## Adicionando e Removendo Elementos

Você pode adicionar elementos a uma lista aninhada usando métodos como `append` ou `extend`.

```py
# Adicionando uma nova linha à lista aninhada
nova_linha = ['John', 30]
lista_aninhada.append(nova_linha)

# Removendo a segunda linha da lista aninhada
del lista_aninhada[1]
```

## Copiando Listas Aninhadas

Ao copiar listas aninhadas, tenha cuidado para não criar referências indesejadas. Use o módulo `copy` ou técnicas como fatiamento.

```py
# Copiando uma lista aninhada com copy
copia_lista = copy.deepcopy(lista_aninhada)

# Copiando com fatiamento
copia_lista = lista_aninhada[:]
```

## Exemplos práticos

Listas aninhadas são frequentemente usadas para representar matrizes, tabelas ou estruturas hierárquicas.

```py
# Exemplo: Criando uma matriz 3x3 com listas aninhadas
matriz = [[0] * 3 for _ in range(3)] 
```
