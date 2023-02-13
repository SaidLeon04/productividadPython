"""
Busca una palabra en una oración
"""
def search(word,text):
    if word in text:
        return "Palabra encontrada"
    elif word not in text:
        return "Palabra no encontrada"


text = input("Escribe la oración: ")
word = input("Escribe la palabra que quieres hallar: ")
print(search(word,text))

