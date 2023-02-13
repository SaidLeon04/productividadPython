"""
esta cosa suma todos los numeros anteriores a N escrito 
por el usuario
"""
num = int(input("Escribe un número: "))
cont = 0
suma = 0
while cont <= num:
    suma = suma+cont
    cont = cont+1
print("La suma de todos los números anteriores a: ", num, "más ", num, "es " ,suma)

