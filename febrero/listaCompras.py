"""
Sistema para crear una lista de compras
"""
print ("C O M P R A S\nEscoge una opcion\n\n1. Añadir producto\n2. Finalizar listado\n3. Ver lista\n4. Modificar lista\n5. Eliminar 1 elemento\n6. Eliminar toda la lista\n7.Ver menú de opciones otra vez") # menú de opciones

op = int(input("Escoge una opción: "))

compras = [] # array 

while op != 2:
  # operaciones de la opción 1
    if op == 1:
        producto = input("Producto: ")
        compras.append(producto)
        op = int(input("Escribe una opción para continuar: "))

  # operaciones de la opcion 2
    if op == 3:
        numero_compras = len(compras)
        if numero_compras == 0:
            print("Aún no has añadido productos ")
            op = int(input("Escoge una opción: "))
        else:
            print ("Numero de productos añadidos: ", numero_compras)
            for i in compras:
                print(i)
            op = int(input("Escoge una opción "))

    if op == 4:
        numero_compras = len(compras)
        if numero_compras == 0:     
            print("Aún no has añadido productos ")
            op = int(input("Escoge una opción: "))
        else:
            modificar = int(input("Escribe el número del elemento para modificar,  empezando a contar desde 0\n "))
            posicion = compras[modificar]
            nuevo = input("Escribe el nuevo producto: ")
            compras[modificar] = nuevo
            print ("Tu lista actual")
            for i in compras:
                print(i)
            op = int(input("Escoge una opción para continuar"))
     


  # operaciones de la opción 5
    if op == 5:
        numero_compras = len(compras)
        if numero_compras == 0:     
            print("Aún no has añadido productos ")
            op = int(input("Escoge una opción: "))
        else:
            print ("Escribe el número del producto que deseas borrar (ten en cuenta comenzar a contar desde 0)")
            eliminar = int(input("Escribe: "))
            compras.pop(eliminar)
            for i in compras:
                print(i)
            op = int(input("Escoge una opción "))
        
      
  # operaciones de la opción 6
    if op == 6:
        numero_compras = len(compras)
        if numero_compras == 0:     
            print("Aún no has añadido productos ")
            op = int(input("Escoge una opción: "))
        else:
            print ("Eliminar toda la lista y los productos añadidos, ¿estas seguro?\n1. SI || 2. NO\n")
            read = int(input())
            if read == 1:
                compras.clear()
                print ("Toda la lista fue eliminada")
                op = int(input("Escoge una opción "))
            elif read == 2:
                print ("Estuviste cerca de borrar tu lista D:")
                op = int(input("Escoge una opción "))

    if op == 7:
        print ("C O M P R A S\nEscoge una opcion\n\n1. Añadir producto\n2. Finalizar listado\n3. Ver lista\n4. Modificar lista\n5. Eliminar 1 elemento\n6. Eliminar toda la lista\n7.Ver menú de opciones otra vez")
        op = int(input("Escoge una opción: "))
      
        

# operaciones de la opción 2
if op ==2:
    numero_compras = len(compras)
    if numero_compras == 0:     
        print("Ningún producto agregado ")
    else:
        print ("Tu lista de compras: ")
        for i in compras:
            print(i)
