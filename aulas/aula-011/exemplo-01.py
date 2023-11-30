C_RESET = "\033[0m"
C_BOLD = "\033[1m"
C_UNDERLINE = "\033[4m"

C_BLACK = "\033[30m"
C_RED = "\033[31m"
C_GREEN = "\033[32m"
C_YELLOW = "\033[33m"
C_BLUE = "\033[34m"
C_MAGENTA = "\033[35m"
C_CYAN = "\033[36m"
C_WHITE = "\033[37m"

# Função para imprimir cor
def print_color(text, color):
    print(color + text + C_RESET)

# Exemplos de uso
print_color("Texto em vermelho", C_RED)
print_color("Texto em verde", C_GREEN)
print_color("Texto em amarelo", C_YELLOW)
print_color("Texto em azul", C_BLUE)
print_color("Texto em ciano", C_CYAN)
print_color("Texto em magenta", C_MAGENTA)
print_color("Texto em branco", C_WHITE)
print_color("Texto em negrito", C_BOLD)
print_color("Texto sublinhado", C_UNDERLINE)

# Combinando estilos
print_color("Text verde em negrito e sublinhado", C_GREEN + C_BOLD + C_UNDERLINE)