#days to years, months, weeks and days

año_print = 0
mes_print = 0
dias_print = 0
semanas_print = 0
dia_input = 0
contador = 0
#prints of final result
input_gente = int(input('Escribe el tiempo en dias para pasar a mes/es, semana/s y año/s: '))

print(input_gente)

for i in range(input_gente):
    dia_input += 1
    #I pass the input to a different variable

for l in range(dia_input):
    dias_print += 1
    if dias_print >= 30:
        mes_print += 1
        dias_print -= 30
    if mes_print >= 12:
        año_print += 1
        mes_print -= 12

for i in range(dias_print):
    if dias_print >= 7:
        semanas_print += 1
        dias_print -= 7

print('Son {} años'.format(año_print))
print('Son {} meses'.format(mes_print))
print('Son {} semanas'.format(semanas_print))
print('Son {} dias'.format(dias_print))
