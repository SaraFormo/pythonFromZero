# Crea una lista de alumnos cada uno con una nota y calcula la nota media de esos alumnos
# Muestra un listado con aquellos alumnos que han aprobado
# Muestra el alumno con la mejor nota de la clase

clase = [
    ["Pepe", 7],
    ["Laura", 5],
    ["Juan", 7],
    ["Mariano", 3],
    ["Borja", 4],
]

aprobados = 0
for alumno in clase:
    if alumno[1] >= 5:
        aprobados += 1

print(aprobados)
media = 0
nombreAprobados = ""
for alumno in clase:
    if alumno[1] >= 5:
       nombreAprobados += alumno[0]+","


print(nombreAprobados)
