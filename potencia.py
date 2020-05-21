numero = int(input('Numero para dar potencia;'))
potencia = int(input('Numero de potencia;'))
resultado = 0

resultado += numero
for i in range(potencia - 1):
    resultado *= numero

if potencia == 0:
    resultado = 1
    
print(resultado)

#other form to calculate power of a number :)
