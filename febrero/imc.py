# Programa que calcula el IMC de una persona
def Calcular(peso:float, altura:float)->float:   
    imc = None
    imc = peso / (altura**2)
    
    if imc < 18.5:
            imc = "Peso Bajo"
    elif imc>= 18.5 and imc < 25:
            imc = "Normal"
    elif imc >= 25 and imc < 30:
            imc = "Sobre Peso"
    elif imc >= 30:
            imc = "Obesidad"
    return imc


print (Calcular(65, 1.70))
