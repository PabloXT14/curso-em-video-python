# Condições Aninhadas

- Nessa aula, vamos aprender como criar estruturas condicionais aninhadas, usando os comandos if.. elif.. else em programas Python.
- As condições aninhadas em Python referem-se à utilização de estruturas de controle de fluxo, como `if`, `elif` e `else`, dentro de outras. Isso permite que você avalie múltiplas condições em uma estrutura hierárquica.
- Veja um exemplo simples para ilustrar como isso funciona:

```py
# Exemplo de condições aninhadas em Python

# Suponha que temos uma variável para a idade
idade = 25

# Vamos usar condições aninhadas para determinar a faixa etária
if idade < 18:
    print("Você é menor de idade.")
elif 18 <= idade < 65:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")
```

- Neste exemplo, temos três níveis de condições aninhadas:

1. A primeira condição (`if idade < 18:`) verifica se a idade é menor que 18.
2. Se a primeira condição não for atendida, a segunda condição (`elif 18 <= idade < 65:`) é verificada. Isso verifica se a idade está entre 18 (inclusive) e 65 (não inclusive).
3. Se nem a primeira nem a segunda condição forem atendidas, a terceira condição (`else:`) é executada.

Você pode adicionar mais blocos `elif` conforme necessário, dependendo das condições específicas que deseja verificar.

Este é apenas um exemplo básico. Condições aninhadas podem ser tão complexas quanto necessário, dependendo dos requisitos do seu programa. Certifique-se de alinhar corretamente os blocos de código para indicar a hierarquia das condições.