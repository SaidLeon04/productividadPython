"""
Un sudoku hecho en consola porque es lo que hay
"""


print ("|2|","| |","| |")
print ("| |","|3|","| |")
print ("|9|","| |","|1|")

posicion = int(input("Escribe la posición del numero"))
valor = int(input("Escribe el número"))

if posicion == 2:
    print ("|2 |","|",valor,"|","|  |")
    print ("|  |","|3 |","|  |")
    print ("|9 |","|  |","|1 |")

if posicion == 3
