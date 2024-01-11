def header(text = '', text_color = '\033[1;32m', line_symbol = '-', line_length = 70):
    line = line_symbol * line_length 
    formatted_text = f'{text_color}{text.upper():^{line_length}}{'\033[m'}' 

    print(line)
    print(formatted_text)
    print(line)
