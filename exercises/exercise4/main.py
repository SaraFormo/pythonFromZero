clase = [
    ["Alberto", 5],
    ["Javier", 2],
    ["Sara", 6],
    ["Bea", 7],
    ["Julia", 3],
    ["Fernando", 2],
]

apro=0
susp=0
sumaNotas=0
numAlumnos=len(clase)
for alumno in clase:
    sumaNotas+=alumno[1]
    if alumno[1]>=5:
        apro += 1
    else:
        susp += 1

media=sumaNotas/numAlumnos

print("el numero de aprobados es:"+str(apro))
print("el numero de suspensos es:"+str(susp))
print("la nota media de la clase es:"+str(media))