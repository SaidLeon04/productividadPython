"""
Sistema para crear una lista de compras
"""
print ("C O M P R A S\nEscoge una opcion\n\n1. Añadir producto\n2. Finalizar listado\n3. Ver lista\n4. Modificar lista\n5. Eliminar 1 elemento\n6. Eliminar toda la lista")

op = int(input("Escoge una opción: "))

compras = []

while op != 2:
    if op == 1:
        producto = input("Crea tu propia lista de compras\n Producto: ")
        compras.append(producto)
        op = int(input("Escoge una opción "))

    if op == 3:
        numero_compras = len(compras)
        print ("Numero de productos añadidos: ", numero_compras)
        for i in compras:
          print(i)
        op = int(input("Escoge una opción "))

    """
    if op == 4:
        print("Escribe el número del elemento para modificar ")
        modificar = int(input("Escribe: "))
    """    



    if op == 5:
        print ("Escribe el número del producto que deseas borrar (ten en cuenta comenzar a contar desde 0)")
        eliminar = int(input("Escribe: "))
        compras.pop(eliminar)
        for i in compras:
            print(i)
        op = int(input("Escoge una opción "))
        
      

    if op == 6:
        print ("Eliminar toda la lista y los productos añadidos, ¿estas seguro?\n1. SI || 2. NO\n")
        read = int(input())
        if read == 1:
            compras.clear()
            print ("Toda la lista fue eliminada")
            op = int(input("Escoge una opción "))
        elif read == 2:
            print ("Estuviste cerca de borrar tu lista D:")
            op = int(input("Escoge una opción "))


if op ==2:
    print ("Tu lista de compras: ")
    for i in compras:
        print(i)
