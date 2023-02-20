# Escribir un programa que pregunte el nombre del usuario en la consola y
#   un número entero e imprima por pantalla en líneas distintas el nombre
#   del usuario tantas veces como el número introducido.

print("dame el nombre del usuario")
nombre = input()
print("dame un numero entero")
numeroEntero= input()

for x in range(0, int(numeroEntero)):
    print(nombre)
