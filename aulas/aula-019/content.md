# Dicionários

## O que são dicionários

Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por `chaves literais` ou pares `chave-valor`.  Cada chave em um dicionário deve ser única, e ela é usada para acessar o valor associado a essa chave. Os dicionários são implementados como tabelas de hash, o que proporciona acesso eficiente aos valores.

## Criando um Dicionário

Para criar um dicionário, você pode usar chaves `{}` e separar as chaves dos valores por dois pontos `:`. Veja um exemplo simples:

```py
meu_dicionario = dict()

# OU

meu_dicionario = {
    'chave1': valor1,
    'chave2': valor2,
    'chave3': valor3
}
```

## Acessando Valores

Você pode acessar os valores em um dicionário fornecendo a chave correspondente:

```py
print(meu_dicionario['chave1']) # Saída: valor1
```

## Adicionando e Atualizando Valores

Para adicionar ou atualizar valores, basta atribuir um valor a uma nova chave ou a uma chave existente:

```py
meu_dicionario['nova_chave'] = novo_valor

meu_dicionario['chave1'] = novo_valor
```

## Removendo Chaves e Valores

Use o comando `del` para remover uma chave e o seu valor associado:

```py
del meu_dicionario['chave1']
```

## Verificando a Existência de uma Chave

Use o operador `in` para verificar se uma chave existe no dicionário:

```py
if 'chave1' in meu_dicionario:
    print('Chave encontrada!')
```

## Iterando sobre Chaves e Valores

Você pode usar loops para iterar sobre as chaves ou valores de um dicionário:

```py
for chave in meu_dicionario:
    print(chave, meu_dicionario[chave])
```

Ou, alternativamente:

```py
for chave, valor in meu_dicionario.items():
    print(chave, valor)
```

## Métodos Úteis

* `keys()`: Retorna uma lista de todas as chaves no dicionário.
* `values()`: Retorna uma lista de todos os valores no dicionário.
* `items()`: Retorna uma lista de tuplas (chave, valor) do dicionário.

```py
todas_as_chaves = meu_dicionario.keys()
todos_os_valores = meu_dicionario.values()
todos_os_pares = meu_dicionario.items() # [('chave1', valor1)]
```

## Dicionários Aninhados

Dicionários podem conter outros dicionários. Isso é conhecido como dicionários aninhados.

```py
dicionario_aninhado = {
    'chave1': {
        'sub_chave1': valor1,
        'sub_chave2': valor2
    }
}
```

## Compreensão de Dicionários

Assim como listas, você pode usar compreensões de dicionários para criar dicionários de maneira concisa:

```py
meu_dicionario = {chave: valor for chave, valor in zip(lista_de_chaves, lista_de_valores) }
```

## Conclusão

Este tutorial forneça uma introdução abrangente ao uso de dicionários em Python! Vale ressaltar que você pode misturas as estruturas de variáveis composta que já apresentamos (tuplas e listas) com os dicionários, tendo por exemplo dicionários dentro de listas, o que é muito comum.
