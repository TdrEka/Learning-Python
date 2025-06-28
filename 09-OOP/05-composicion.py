class Motor:
    def encender(self):
        print("brum brum")

class Coche:
    def __init__(self, motor):
        self.motor = motor

    def arrancar(self):
        self.motor.encender()



motor = Motor()
seat = Coche(motor)
seat.arrancar()


class Curso:
    def __init__(self, id, nombre, num_plazas):
        self.id = id
        self.nombre = nombre
        self.num_plazas = num_plazas
        self.lista_alumnos = []

    def inscribir_alumnos(self, alumno):
        if len(self.lista_alumnos) < self.num_plazas and alumno not in self.lista_alumnos:
            self.lista_alumnos.append(alumno)
            print(f"yay {alumno} made it in")

        else: print(f"Booh... ")


class CursoPresencial(Curso):
    def __init__(self, curso_id, nombre, num_plazas, direccion):
        super().__init__(curso_id, nombre, num_plazas)
        self.direccion = direccion
        self.sesiones = [] # -> Lista de fechas en las que hay clase
        self.asistencias = {} # -> Diccionario con los alumnos como claves, y el valor seria una lista de fechas

    def agregar_sesion(self, fecha):
        self.sesiones.append(fecha)

    def registrar_asistencia(self, alumno, fecha):
        if alumno not in self.lista_alumnos:
            print(f"el alumno {alumno} no esta apuntado en el curso {self.nombre}")
            return
        if fecha not in self.sesiones:
            print(f"la fecha {fecha} no es una sesion valida")
            return

        # if alumno not in self.asistencias:
        #    self.asistencias[alumno] = [fecha]
        # else:
        #    self.asistencias[alumno].append(fecha)

        self.asistencias.setdefault(alumno, []).append(fecha)
        print(f"el alumno {alumno} ha asistido a la clase de {fecha}")

    def porcentaje_asistencia(self, alumno):
        if alumno not in self.lista_alumnos:
            print(f"El alumno {alumno} no está inscrito en el curso.")
            return 0

        total_sesiones = len(self.sesiones)
        if total_sesiones == 0:
            print("No hay sesiones registradas.")
            return 0

        asistencias = self.asistencias.get(alumno, [])
        porcentaje = (len(asistencias) / total_sesiones) * 100
        return porcentaje

class CursoOnline(Curso):
    def __init__(self, curso_id, nombre, num_plazas, plataforma):
        super().__init__(curso_id, nombre, num_plazas)
        self.plataforma = plataforma
        self.sesiones = []  # -> Lista de fechas en las que hay clase
        self.asistencias = {}  # -> Diccionario con los alumnos como claves, y el valor seria una lista de fechas

    def agregar_sesion(self, fecha):
        self.sesiones.append(fecha)

    def registrar_asistencia(self, alumno, fecha):
        if alumno not in self.lista_alumnos:
            print(f"el alumno {alumno} no esta apuntado en el curso {self.nombre}")
            return
        if fecha not in self.sesiones:
            print(f"la fecha {fecha} no es una sesion valida")
            return

        # if alumno not in self.asistencias:
        #    self.asistencias[alumno] = [fecha]
        # else:
        #    self.asistencias[alumno].append(fecha)

        self.asistencias.setdefault(alumno, []).append(fecha)
        print(f"el alumno {alumno} ha asistido a la clase de {fecha}")

    def get_reporte_asistencia(self):
        pass

class CursoEnlatado(Curso):
    def __init__(self, curso_id, nombre, num_plazas, plataforma, fecha_grabacion, duracion):
        super().__init__(curso_id, nombre, num_plazas)
        self.plataforma = plataforma
        self.fecha_grabacion = fecha_grabacion
        self.duracion = duracion

    def esta_obsoleto(self):
        pass


    def ver_curso(self, alumno, minutos_consumidos):
        pass