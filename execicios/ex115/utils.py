import os

script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, 'people.txt')

def header(text = '', text_color = '\033[1;32m', line_length = 70, line_symbol = '-'):
    line = line_symbol * line_length
    header_content = f'{text_color}{text.upper():^{line_length}}{'\033[m'}'

    print(line)
    print(header_content)
    print(line)
