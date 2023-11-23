# Manipulando Texto (Strings)

- Nessa aula, vamos aprender operações com String no Python.
- `String` = é uma cadeia de caracteres. 
- Veja a seguir as principais operações:

## Fatiamento de String

O fatiamento de strings em Python envolve a extração de partes específicas de uma string. Pode ser feito utilizando índices. Por exemplo:
```py
phrase = 'Curso em Vídeo'
print(phrase[9])  # Retorna 'V'
```

## Análise

- `len()`: Retorna o comprimento (número de caracteres) de uma string.
```py
length = len(phrase)
print(length)  # Retorna 14
```

- `count()`: Conta o número de ocorrências de uma substring em uma string.
```py
count_v = phrase.count('Vídeo')
print(count_v)  # Retorna 1
```

- `find()`: Retorna o índice da primeira ocorrência de uma substring. Se não encontrar, retorna -1.
```py
index_e = phrase.find('em')
print(index_e)  # Retorna 6
```

- `in`: Verifica se uma substring está presente na string.
```py
contains_curso = 'Curso' in phrase
print(contains_curso)  # Retorna True
```

## Transformações

- `replace()`: Substitui uma substring por outra.
```py
new_phrase = phrase.replace('Vídeo', 'Aula')
print(new_phrase)  # Retorna 'Curso em Aula'
```

- `upper()`: Converte todos os caracteres para maiúsculas.
```py
upper_case = phrase.upper()
print(upper_case)  # Retorna 'CURSO EM VÍDEO'
```

- `lower()`: Converte todos os caracteres para minúsculas.
```py
lower_case = phrase.lower()
print(lower_case)  # Retorna 'curso em vídeo'
```

- `capitalize()`: Converte o primeiro caractere para maiúscula.
```py
capitalized = phrase.capitalize()
print(capitalized)  # Retorna 'Curso em vídeo'
```

- `title()`: Converte o primeiro caractere de cada palavra para maiúscula.
```py
title_case = phrase.title()
print(title_case)  # Retorna 'Curso Em Vídeo'
```

- `strip()`: Remove espaços em branco no início e no final da string.

- `rstrip()`: Remove espaços em branco à direita da string.

- `lstrip()`: Remove espaços em branco à esquerda da string.

## Junção e Divisão:

- `join()`: Junta os elementos de uma sequência/array usando uma string como separador.
```py
words = ['Curso', 'em', 'Vídeo']
joined_phrase = ' '.join(words)
print(joined_phrase)  # Retorna 'Curso em Vídeo'
```

- `split()`: Divide uma string em uma lista de substrings com base em um separador.
```py
split_words = phrase.split(' ')
print(split_words)  # Retorna ['Curso', 'em', 'Vídeo']
