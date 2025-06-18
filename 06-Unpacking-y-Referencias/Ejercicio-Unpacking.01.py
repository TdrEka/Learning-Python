# Ejercicio 1
# Dada una lista de equipos (pares o impares (en caso de impar que el equipo que sobre pase de fase)
# entrentamientos aleatorios
# Unpacking y */**
# ----
# Barcelona vs Valencia
# Real Madrid vs Sevilla
# ----
# Valencia vs Real Madrid
# Barcelona vs Sevilla
# ----
# Valencia vs Real Madrid
# Barcelona vs Sevilla
# At Bilbao pasa de fase automáticamente

# Enfrentamientos aleatorios
# Unpacking y */**
# Pista: podéis utilizar funciones recursivas
import random

equipos1 = ['Valencia', 'Real Madrid', 'Barcelona', 'Sevilla']
equipos2 = ['Valencia', 'Real Madrid', 'Barcelona', 'Sevilla', 'At Bilbao']


def generador_de_matches(lista_equipos):
    if len(lista_equipos) == 0:
        return
    elif len(lista_equipos) == 1:
        print(f"- El {lista_equipos[0]} pasa directamente.")
    else:
        random.shuffle(lista_equipos)
        equipo1, equipo2, *resto = lista_equipos
        print(f"- {equipo1} vs {equipo2}")
        generador_de_matches(resto)


generador_de_matches(equipos1)
generador_de_matches(equipos2)