estudiantes=["Luis","Pepe","Carolina","Manolo","Leticia"]

calificaciones= {
    estudiantes[0]:7,
    estudiantes[1]:9,
    estudiantes[2]:9,
    estudiantes[3]:4,
    estudiantes[4]:10    
}
def mostrarNotas():
    for x in estudiantes:
        archivo.write(f"{x}: {calificaciones[x]}  ")

with open("registro.txt","w") as archivo:
    mostrarNotas()