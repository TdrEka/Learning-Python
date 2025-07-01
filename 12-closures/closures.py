# Crear la closure motor y devolver el metodo arrancar
# crear la closure coche y pasar como argumento el motor
# Devolver un diccionario que devuelva la clave arrancar y que esta ejecute la funcion del motor

def motor():
    def arrancar():
        print("coche arrancado")
    return arrancar

def coche(motor_func):
    return {"arrancar": motor_func}

mi_motor = motor()
mi_coche = coche(mi_motor)
mi_coche["arrancar"]()