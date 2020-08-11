# ejercicio 1.18

vocales = 'aeiou'
cadena = 'Geringoso'
capadepenapa = ''
for c in cadena:
    if c in vocales:
        capadepenapa = capadepenapa + c + 'p' + c
    else:
        capadepenapa = capadepenapa + c

print(capadepenapa)