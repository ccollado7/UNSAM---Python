# hipoteca.py

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
meses = 12 #Mes comenzando en el valor final
adelanto = 1000

while saldo > 0:
    while meses > 0: #Meses incremental
        saldo = saldo * ( 1+tasa/12) - pago_mensual - adelanto
        total_pagado = total_pagado + pago_mensual + adelanto
        meses = meses - 1 #Decremento en 1 el mes
    saldo = saldo * ( 1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual

print('Total Pagado', round(total_pagado,2))

