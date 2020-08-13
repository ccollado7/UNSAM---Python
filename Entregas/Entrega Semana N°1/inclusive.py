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


#Si el enunciado de un ejercicio te pide que lo corras con un input particular, por favor poné la salida que obtuviste como comentario en tu código.

#Salida obtenida

	#todes somes programadores
	#Les hermanes sean unides porque ésa es la ley primera
	#¿cóme transmitir a les otres el infinite Aleph?
	#Todos, tu también