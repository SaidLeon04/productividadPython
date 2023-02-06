"""
Programa que piensa un número aleatorio entre un rango especifico y 
el usuario trata de adivinar
"""
import random

print ("Selecciona la dificultad: \n")
print ("1.Facil (0-10)\n")
print ("2.Medio (0-15)\n")
print ("3.Dificil (0-30)\n")
op = int(input())

if op == 1:
    numero = random.randint(0,10)
    intento1 = int(input("Intento 1: \n"))
    # if intento1
    if intento1 == numero:
        print ("Correcto, el número es: ", numero)
    else: # else intento1
        if numero > intento1: # validación intento1
            print ("Es mayor\n")
            intento2 = int(input("Intento 2: \n"))
        elif numero < intento1:
            print ("Es menor\n")
            intento2 = int(input("Intento 2: \n"))
    # fin de validación intento1
        # if intento2
        if intento2 == numero:
            print ("Correcto el número es: ", numero)
        else: # else intento2
            if numero > intento2: # validación intento2
                print ("Es mayor\n")
                intento3 = int(input("Intento 3: \n"))
            elif numero < intento2:
                print ("Es menor\n")
                intento3 = int(input("Intento 3: \n"))
        # fin validación intento2
            # if intento3
            if intento3 == numero:
                print ("Correcto el número es: ", numero)
            else: # else intento3
                if numero > intento3: # validación intento3
                    print ("Intentos terminados, el número era ", numero)
                elif numero < intento3:
                    print ("Intentos terminados, el número era ", numero)
            # fin validación intento3

if op == 2:
    numero = random.randint(0,15)
    intento1 = int(input("Intento 1: \n"))
    #if intento1
    if intento1 == numero:
        print ("Correcto, el número es: ", numero)
    else: #else intento1
        if numero > intento1: #validación intento1
            print ("Es mayor\n")
            intento2 = int(input("Intento 2: \n"))
        elif numero < intento1:
            print ("Es menor\n")
            intento2 = int(input("Intento 2: \n"))
    #fin de validación intento1
        if intento2 == numero:
            print ("Correcto el número es: ", numero)
        else: 
            if numero > intento2:
                print ("Es mayor\n")
                intento3 = int(input("Intento 3: \n"))
            elif numero < intento2:
                print ("Es menor\n")
                intento3 = int(input("Intento 3: \n"))
        
            if intento3 == numero:
                print ("Correcto el número es: ", numero)
            else: 
                if numero > intento3:
                    print ("Intentos terminados, el número era ", numero)
                elif numero < intento3:
                    print ("Intentos terminados, el número era ", numero)


if op == 3:
    numero = random.randint(0,30)
    intento1 = int(input("Intento 1: \n"))
    #if intento1
    if intento1 == numero:
        print ("Correcto, el número es: ", numero)
    else: #else intento1
        if numero > intento1: #validación intento1
            print ("Es mayor\n")
            intento2 = int(input("Intento 2: \n"))
        elif numero < intento1:
            print ("Es menor\n")
            intento2 = int(input("Intento 2: \n"))
    #fin de validación intento1
        if intento2 == numero:
            print ("Correcto el número es: ", numero)
        else: 
            if numero > intento2:
                print ("Es mayor\n")
                intento3 = int(input("Intento 3: \n"))
            elif numero < intento2:
                print ("Es menor\n")
                intento3 = int(input("Intento 3: \n"))
        
            if intento3 == numero:
                print ("Correcto el número es: ", numero)
            else: 
                if numero > intento3:
                    print ("Intentos terminados, el número era ", numero)
                elif numero < intento3:
                    print ("Intentos terminados, el número era ", numero)

if op == 18:
    numero = random.randint(1,10)
    print (numero)
    intento1 = int(input("Intento 1: \n"))
    #if intento1
    if intento1 == numero:
        print ("Correcto, el número es: ", numero)
    else: #else intento1
        if numero > intento1: #validación intento1
            print ("Es mayor\n")
            intento2 = int(input("Intento 2: \n"))
        elif numero < intento1:
            print ("Es menor\n")
            intento2 = int(input("Intento 2: \n"))
    #fin de validación intento1
        if intento2 == numero:
            print ("Correcto el número es: ", numero)
        else: 
            if numero > intento2:
                print ("Es mayor\n")
                intento3 = int(input("Intento 3: \n"))
            elif numero < intento2:
                print ("Es menor\n")
                intento3 = int(input("Intento 3: \n"))
        
            if intento3 == numero:
                print ("Correcto el número es: ", numero)
            else: 
                if numero > intento3:
                    print ("Intentos terminados, el número era ", numero)
                elif numero < intento3:
                    print ("Intentos terminados, el número era ", numero)
        