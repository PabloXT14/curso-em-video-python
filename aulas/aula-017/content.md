# Listas (parte 1)


## Introdução às Lista

As listas são estruturas de dados em Python que permitem armazenar e organizar coleções de itens, em outras palavras são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura. Esses itens podem ser de qualquer tipo, como números, strings, ou até mesmo outras listas. Listas são mutáveis, o que significa que você pode modificar, adicionar ou remover elementos após a criação.

## Criando uma Lista

Para criar uma lista, você pode usar colchetes `[]` e inserir os elementos separados por vírgulas. Exemplo:

```py
minha_lista = [1, 2, 3, 4, 5]
```

Você também pode criar uma lista com `range`:

```py
# list(): função para criar uma lista de acordo com algum parâmetro

minha_lista = list(range(4, 11)) # cria uma lista com valores/itens de 4 até 10 (último não conta) 

print(minha_lista) # [4, 5, 6, 7, 8, 9, 10]
```

## Acessando Elementos

Os elementos em uma lista podem ser acessados por meio de índices, que começam do zero. Para acessar o primeiro elemento da lista `minha_lista`, você faria:

```py
primeiro_elemento = minha_lista[0]
```

## Modificando Elementos

Listas são mutáveis, então você pode modificar elementos atribuindo um novo valor a um índice específico:

```py
minha_lista[2] = 10
```

## Adicionado e Removendo Elementos

* **Adicionando Elementos no final**:

```py
minha_lista.append(6)
```

* **Inserindo elementos em uma posição específica**:

```py
minha_lista.insert(2, 7) # Insere o valor 7 na posição 2
```

* **Removendo elementos por valor**:

```py
minha_lista.remove(4) # Remove o primeiro elemento com valor 4
```

* **Removendo elementos por índice**:

```py
del minha_lista[0] # Remove o elemento no índice 0 
```

* **Removendo o último elemento**:

```py
minha_lista.pop() # Remove o último elemento (ou remove um elemento em um índice específico se este for passado como argumento na função pop())
```

* **Organizando os elementos**:

```py
minha_lista = [8, 2, 5, 4, 9, 3, 0]

minha_lista.sort() # Organiza a lista em ordem crescente ou alfabética (este é o padrão)

print(minha_lista) # [0, 2, 3, 4, 5, 8, 9]

minha_lista.sort(reverse=True) # Faz o inverso, ou seja, organiza em ordem decrescente

print(minha_lista) # [9, 8, 5, 4, 3, 2, 0]
```

## Tamanho da Lista

Para saber o número de elementos em uma lista, utilize a função `len()`:

```py
tamanho_da_lista = len(minha_lista)
```

## Iterando sobre uma Lista

Você pode utilizar loops para percorrer os elementos de uma lista:

```py
for elemento in minha_lista:
    print(elemento)
```

## Lista Aninhadas

Listas podem conter outras listas, criando estruturas aninhadas:

```py
lista_aninhada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

## Operações com Listas

* **Concatenando Listas**:

```py
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

lista_concatenada = lista1 + lista2
```

* **Repetindo Elementos**:

```py
lista_repetida = [1] * 3 # Cria uma lista com 3 elementos iguais a 1
```

## Funções Úteis para Listas

* `max(lista)`: Retorna o maior elemento da lista.
* `min(lista)`: Retorna o menor elemento da lista.
* `sum(lista)`: Retorna a soma de todos os elementos da lista.

## Conclusão

As listas são uma parte fundamental da linguagem Python, oferecendo flexibilidade e eficiência no tratamento de coleções de dados.
