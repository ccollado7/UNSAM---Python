# hipoteca.py

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
pago_extra_mes_comienzo = 61 #Mes de inicio del pago extra
pago_entra_mes_fin = 108 #Mes de fin del pago extra
pago_extra = 1000 #Valor del pago extra
mes = 1 #Variable mes

while saldo > 0:  
    while mes < 61: 
        saldo = saldo * ( 1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
        mes = mes + 1
    while (mes >= pago_extra_mes_comienzo) and (mes <= pago_entra_mes_fin): 
        saldo = saldo * ( 1+tasa/12) - pago_mensual - pago_extra
        total_pagado = total_pagado + pago_mensual + pago_extra
        mes = mes + 1 
    saldo = saldo * ( 1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual

print('Total Pagado', round(total_pagado,2))

