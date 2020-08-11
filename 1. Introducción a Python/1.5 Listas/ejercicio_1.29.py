# ejercicio_1.29


frase = 'todos somos programadores'
frase_t = ''
palabras = frase.split()
for palabra in palabras:
    palabra_queda = palabra[:-2]
    for letra in palabra[-2:]:
        if (letra == 'o'):
            letra = 'e'
        else:
            letra = letra
        palabra_queda = palabra_queda + letra
    frase_t = frase_t + palabra_queda + ' '
print(frase_t)