# Condições Simples e Compostas

- Nessa aula, vamos aprender como utilizar estruturas condicionais simples e compostas (`if`..`else`) nos seus programas em Python
- Em Python, as condições são usadas para controlar o fluxo de um programa, permitindo que certas partes do código sejam executadas apenas se uma condição específica for verdadeira. Existem dois tipos principais de condições: simples e compostas

## Condições Simples

- São estruturas de decisão que envolvem apenas uma condição.
- Usam a palavra-chave `if` seguida pela condição a ser avaliada.
- Se a condição for verdadeira, o bloco de código indentado abaixo do `if` é executado; caso contrário ele é ignorado.
- Exemplo:

```py
idade = 18

if idade >= 18:
    print('Você é maior de idade.')
``` 

## Condições Compostas

- Envolvem multiplas condições e podem incluir diferentes caminhos de execução.
- Usam as palavras-chave `if`, `elif` (abreviação de "else if") e `else`.
- O bloco de código sob o primeiro `if` ou `elif` cuja condição é verdadeira será executado, e o resto sera ignorado.
- Exemplo:

```py
nota = 75

if nota >= 90:
    print('A')
elif nota >= 80:
    print('B')
elif nota >= 70:
    print('C')
else
    print('F')
```

## Conclusão

Essas estruturas condicionais permitem que você tome decisões em seu código com base em diferentes situações, tornando seu programa mais flexível e capaz de lidar com diferentes casos.
