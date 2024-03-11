# Crea una función llamada calculadora que tome dos argumentos numéricos y realice las siguientes operaciones:
# Suma
# Resta
# Multiplicación
# División (maneja la división por cero)
# Llama a la función con dos números de tu elección e imprime los resultados.

def calculadora(num1,num2):
    while num2==0:
        num2=int(input("el segundo número introducido no es correcto, por favor introduzca un número distinto de cero:"))
        print(num2)
    suma= num1+num2
    resta=num1-num2
    multi= num1*num2
    div= num1 / num2
    print("Resultados:")
    print(suma)
    print(resta)
    print(multi)
    print(div)

calculadora(30,9)