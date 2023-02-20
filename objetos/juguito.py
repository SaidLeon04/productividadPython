class juguito():
    def __init__(self):
        __sabor: None
        __precio: None
        __poder: None
    def setSabor (self, sabor):
        self.__sabor = sabor
    #def getSabor (self):
        #return self.__sabor 

jugo1 = juguito()

sabor = input("Sabor: ")
jugo1.setSabor(sabor)
print ("Jugo de sabor: ", sabor)

#jugo1.getSabor() aun si a funcion get, puede mostrar el sabor Dx
