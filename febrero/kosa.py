"""
piedra, papel o tijeras con python
JAJAJAJAJ porque muchos if 
"""
import random

print("1. Jugar contra computadora\n2. Jugar 1 vs 1\nEscribe tu opción\n\n")
op = int(input())




if op == 1:
    opComputadora = random.randint(1,3)
    print ("1. Piedra\n2. Papel\n3. Tijeras\nEscribe tu opcion") 
    opUsuario = int(input())
    if opUsuario == 1:
        print("Escogiste piedra")
    if opUsuario == 2:
        print("Escogiste papel")
    if opUsuario == 3:
        print("Escogiste tijeras")
    if opComputadora == 1:
        print("La computadora escogio piedra")
    if opComputadora == 2:
        print("La computadora escogio papel")
    if opComputadora == 3:
        print("La computadora escogio tijeras")

    if opUsuario == 1 and opComputadora == 1:
        print("Empate")
    if opUsuario == 1 and opComputadora == 2:
        print("Gana Queen")
    if opUsuario == 1 and opComputadora == 3:
        print("Gana Usuario")
    if opUsuario == 2 and opComputadora == 1:
        print("Gana Usuario")
    if opUsuario == 2 and opComputadora == 2:
        print("Empate")
    if opUsuario == 2 and opComputadora == 3:
        print("Gana Queen")
    if opUsuario == 3 and opComputadora == 1:
        print("Gana Queen")
    if opUsuario == 3 and opComputadora == 2:
        print("Gana Usuario")
    if opUsuario == 3 and opComputadora == 3:
        print("Empate")
  
