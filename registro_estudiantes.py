# Crea una lista que contenga varios nombres de estudiantes.
# Crea un diccionario que asocie a cada estudiante con su calificación (puedes inventar las calificaciones).
# Escribe un programa que imprima el nombre de cada estudiante junto con su calificación.

estudiantes=["Luis","Pepe","Carolina","Manolo","Leticia"]

calificaciones= {
    estudiantes[0]:7,
    estudiantes[1]:9,
    estudiantes[2]:9,
    estudiantes[3]:4,
    estudiantes[4]:10    
}

for x in estudiantes:
    print(f"{x}: {calificaciones[x]}")