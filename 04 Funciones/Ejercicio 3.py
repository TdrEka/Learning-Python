# Ejercicio 3
# Crear un diccionario de alumnos (la clave es el nombre del alumno) y cada alumno tendrá las notas de mathematics,
# lengua e Inglés.
# Definir una function que devuelva la nota media de la clase de una asignatura concreta (Ej: get_nota_media(mates)
# Crear una function que devuelva el alumno con la mejor media del curso (Ej: get_mejor_alumno)

alumnos = {
    "Ana": {
        "mathematics": 8.5,
        "lengua": 7.2,
        "inglés": 9.0
    },
    "Carlos": {
        "mathematics": 6.8,
        "lengua": 8.5,
        "inglés": 7.5
    },
    "María": {
        "mathematics": 9.2,
        "lengua": 8.8,
        "inglés": 8.5
    },
    "Pedro": {
        "mathematics": 7.5,
        "lengua": 6.9,
        "inglés": 8.2
    },
    "Laura": {
        "mathematics": 8.8,
        "lengua": 9.1,
        "inglés": 7.8
    }
}


def get_nota_media(asignatura):

    asignaturas_validas = ['mathematics', 'lengua', 'inglés']
    if asignatura not in asignaturas_validas:
        print(f"   Error: Asignatura '{asignatura}' no válida.")
        print(f"   Asignaturas disponibles: {asignaturas_validas}")
        return None

    suma_notas = sum(alumno[asignatura] for alumno in alumnos.values())

    media = suma_notas / len(alumnos)
    return round(media, 2)




def get_mejor_alumno():
    mejor_alumno = None
    mejor_media = 0

    for nombre, notas in alumnos.items():
        media = sum(notas.values()) / len(notas)
        if media > mejor_media:
            mejor_media = media
            mejor_alumno = nombre

    return f"El mejor alumno es {mejor_alumno}, con una media de {round(mejor_media, 2)}"
print("\n--------------------------------------------------------------------------------------\n\n")

print("- La media de la clase es: ", get_nota_media("lengua"),"\n")
print("-", get_mejor_alumno(), "\n")
print("\n--------------------------------------------------------------------------------------")