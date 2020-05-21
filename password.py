import random

letras_contraseña = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '@', '$', '%', '&', ')', '(', '=', '*', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

largo_contraseña_input = int(input('Pon el largo de contraseña que quieras:'))
print(largo_contraseña_input)
password = ''

for largo_contraseña in range(largo_contraseña_input):
    x = random.randint(0, 45)
    password = password + letras_contraseña[x]

print(password)

#random password generator
