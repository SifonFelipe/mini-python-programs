import random

input_usuario = input('Piedra, Papel, Tijera!: Elige una de las 3 opciones:')
a = 'Tijera'
b = 'Piedra'
c = 'Papel'
x_seleccionador = random.randint(0, 2)
lista = [a, b, c]
x_bot = lista[x_seleccionador]

print(input_usuario)

if input_usuario == 'Papel' or input_usuario == 'papel' or input_usuario == 'Piedra' or input_usuario == 'piedra' or input_usuario == 'Tijera' or input_usuario == 'tijera':
    if input_usuario == 'Papel' or input_usuario == 'papel':
        if x_bot == 'Piedra':
            print('Ganaste :)')

        if x_bot == 'Tijera':
            print('Perdiste :(')
                
        if x_bot == 'Papel':
            print('Empate!')                
    else:
        None

    if input_usuario == 'Piedra' or input_usuario == 'piedra':
        if x_bot == 'Papel':
            print('Perdiste :(')

        if x_bot == 'Tijera':
            print('Ganaste :)')

        if x_bot == 'Piedra':
            print('Empate!')
    else:
        None

    if input_usuario == 'Tijera' or input_usuario == 'tijera':
        if x_bot == 'Piedra':
            print('Perdiste :(')

        if x_bot == 'Papel':
            print('Ganaste :)')

        if x_bot == 'Tijera':
            print('Empate!')
    else:
        None
else:
    print('Escribe una de las opciones :)')

print('El bot Random selecciono:{}.'.format(x_bot))