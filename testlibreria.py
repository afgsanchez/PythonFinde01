from colorama import init, Fore, Back, Style

# Inicializa colorama
init()

# Ejemplo de uso: Imprime texto en color rojo
print(Fore.RED + 'Texto en color rojo' + Style.RESET_ALL)

# Ejemplo de uso: Imprime texto con fondo verde
print(Back.GREEN + 'Texto con fondo verde' + Style.RESET_ALL)
