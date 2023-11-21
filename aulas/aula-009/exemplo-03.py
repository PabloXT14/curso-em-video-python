# Transformação em String

print('Transformações em String')

print('-' * 80)

phrase = 'Curso em Vídeo Python'

print(f'- Frase inicial: {phrase}')

print(f"- Substituindo 'Python' por 'Android': {phrase.replace('Python', 'Android')}")

print(f'- Frase toda em maiúscula: {phrase.upper()}')

print(f'- Frase toda em minúscula: {phrase.lower()}')

print(f'- Frase capitalizada (só primero letra da frase maiúscula): {phrase.capitalize()}')

print(f'- Frase com todas as palavras começando em maiúscula: {phrase.title()}')

print(f"- Removendo espaços em branco das extremidades de uma string (frase:'   Aprenda Python   '): {'  Aprenda Python   '.strip()}")

print(f"- Removendo espaços em branco da extremidade direita (frase:'   Aprenda Python   '): {'   Aprenda Python   '.rstrip()}")

print(f"- Removendo espaços em branco da extremidade esquerda (frase: '   Aprenda Python   '): {'   Aprenda Python   '.lstrip()}")