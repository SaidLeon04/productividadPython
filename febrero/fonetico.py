word = input("Escribe una palabra ")
i = 0

while i<len(word):
    print (word[i])
    if word[i] == "a" or word[i] == "A":
        print("Alpha")
        i =+ 1
    if word[i] == "b" or word[i] == "B":
        print("Bravo")
        i =+ 1
    if word[i] == "c" or word[i] == "C":
        print("Charlie")
        i =+ 1
