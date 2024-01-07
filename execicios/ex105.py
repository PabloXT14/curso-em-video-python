# Exercício 105 - Analisando e gerando Dicionários (021)

'''
# Descrição:

Faça um programa que tenha uma função notas(), que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings da função.
'''

# Resolução:

line_length = 70

def header(text = '', text_color = '\033[1;36m', line_symbol = '-'):
    print(line_symbol * line_length)
    print(f'{text_color}{text.upper():^{line_length}}{'\033[m'}')
    print(line_symbol * line_length)


def grades(*student_grades, show_status = False):
    """
    Função para processar notas de alunos e retornar informações estatísticas.

    Parâmetros:
    - *student_grades (float): Notas dos alunos (tamanho indefinido).
    - show_status (bool, opcional, default=False): Se True, inclui a situação/status da turma (BOM, MEDIANO ou RUIM) na saída.

    Retorna:
    - result: Um dicionário contendo as seguintes informações:
        - 'grades_amount': Quantidade de notas,
        - 'higher_grade': A maior nota,
        - 'lower_grade': A menor nota,
        - 'average_class': A média da turma,
        - 'status' (opcional): Situação da turma (BOM, MEDIANO ou RUIM)
    """

    grades_amount = len(student_grades)
    higher_grade = max(student_grades)
    lower_grade = min(student_grades)
    average_class = round(sum(student_grades) / len(student_grades), 1)

    if average_class >= 7:
        status = f'{'\033[1;32m'}BOM{'\033[m'}'
    elif 5 <= average_class < 7:
        status = f'{'\033[1;33m'}MEDIANO{'\033[m'}'
    else:
        status = f'{'\033[1;31m'}RUIM{'\033[m'}'

    result = {
        'grades_amount': grades_amount,
        'higher_grade': higher_grade,
        'lower_grade': lower_grade,
        'average_class': average_class,
        'status': status if show_status else f'{'\033[1;33m'}INDEFINIDO{'\033[m'}'
    }

    return result

header('Média escolar')

grades_dictionary = grades(8.5, 7.2, 9.0, 6.5, show_status=True)

print(f'* Quantidades de notas: {grades_dictionary['grades_amount']}')
print(f'* Maior nota: {grades_dictionary['higher_grade']}')
print(f'* Menor nota: {grades_dictionary['lower_grade']}')
print(f'* Média da turma: {grades_dictionary['average_class']}')
print(f'* Status: {grades_dictionary['status']}')

print('-' * line_length)

# help(grades)
