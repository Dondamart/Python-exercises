palabra=input(str("Ingrese una palabra:"))
counter=0
vocales=["a","e","i","o","u"]
for x in palabra:
    if x in vocales: 
        counter+=1

print("Tiene un total de: "+ str(counter) + " vocales.")