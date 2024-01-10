# Módulos e Pacotes

## Contextualização sobre Modularização

* Surgiu no início da década de 60.
* Sistema ficando cada veis maiores.
* Dai surgiu a modularização.
* Foco: dividir um programa grande (em pequenas partes).
* Foco: aumentar a legibilidade.
* Foco: facilitar a manutenção.

## O que é um módulo?

Um módulo em Python é um arquivo contento definições e instruções em Python. Ele permite que você organize seu código de maneira modular, dividindo-o em partes reutilizáveis. Um módulo pode conter funções, classes e variáveis.

## Como criar e usar módulos

1. **Criar um Módulo:**

* Crie um arquivo com a extensão `.py`, por exemplo, `meu_modulo.py`.
* Adicione funções, classes ou variáveis a este arquivo.

```py
# meu_modulo.py

def saudacao(nome):
    return f'Olá, {nome}!'

pi = 3.1415
```

2. **Usar um Módulo:**

* Para usar as definições de um módulo em outro arquivo, use a palavra-chave `import`.

```py
# meu_programa.py
import meu_modulo

print(meu_modulo.saudacao('Usuário'))
print(meu_modulo.pi)
```

## Vantagens de utilizar módulos

* Organização de código.
* Facilidade na manutenção.
* Ocultação de código detalhado.
* Reutilização em outros projetos.

## O que é um pacote?

Um pacote é uma maneira de organizar módulos relacionados em um diretório hierárquico. Ele contém um arquivo especial chamado `__init__.py` para indicar que o diretório deve ser tratado como um pacote.

## Como criar e usar pacotes

1. **Criar um Pacote:**

* Crie um diretório (pasta) para o pacote e adicione o arquivo `__unit__.py` (pode ser vazio) para indicar que é um pacote.
* Adicione módulos relacionados no mesmo diretório.

```md
meu_pacote/
├── __init__.py
├── modulo1.py
└── modulo2.py
```

2. **Usar um Pacote**

* Para usar módulos de um pacote utilize a notação de ponto (`.`).

```py
# meu_programa.py

from meu_pacote import modulo1, modulo2

print(modulo1.funcao_modulo1())
print(modulo2.funcao_modulo2())
```

3. **Pacote Dentro de Pacote:**

* Se você tem um pacote dentro de outro pacote em Python, você pode seguir uma estrutura de diretórios hierárquica, semelhante à explicação anterior. A única diferença é que você terá um pacote dentro de outro. Vamos passar por um exemplo:

* Considere a seguinte estrutura de diretórios:

```md
meu_projeto/
├── pacote_pai/
│   ├── __init__.py
│   ├── modulo_pai1.py
│   └── modulo_pai2.py
└────── pacote_filho/
        ├── __init__.py
        ├── modulo_filho1.py
        └── modulo_filho2.py
```

* Aqui, `pacote_pai` é o pacote externo, e `pacote_filho` é o pacote interno.

* Para usar módulos de um pacote dentro do outro, você pode fazer o seguinte:

```py
# meu_programa.py
from pacote_pai import modulo_pai1, modulo_pai2
from pacote_pai.pacote_filho import modulo_filho1, modulo_filho2

print(modulo_pai1.funcao_modulo_pai1())
print(modulo_filho1.funcao_modulo_filho1())
```

* Observe como usamos a notação de ponto `.` para acessar o pacote interno a partir do pacote externo. Isso reflete a estrutura de diretórios em que o `pacote filho` está dentro do `pacote pai`.

* Além disso, é importante mencionar que todos os diretórios devem conter um arquivo `__init__.py` para que o Python reconheça os diretórios como pacotes.

## Principais Conceitos

1. **Espaço de Nomes (Namespace):**

* Módulos e pacotes fornecem espaços de nomes separados, evitando conflitos de nomes entre diferentes partes do código.

2. **Importações:**

* `import modulo`: Importa um módulo inteiro.
* `from modulo import funcao`: Importa uma função específica de um módulo.
* `import pacote.modulo`: Importa um módulo de um pacote.

3. **Reusabilidade:**

* Módulos e pacotes promovem a reutilização de código, facilitando a manutenção e organização do projeto.
