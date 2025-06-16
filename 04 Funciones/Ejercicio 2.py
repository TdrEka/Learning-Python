# Ejercicio 2
# Crear una funcion que dada una lista de series (cada serie tiene titulo, capitulos, finalizada, capitulos_vistos)
# nos devuelva las serues que han finalizado pero no hemos terminado de ver

series = [
    {
        'titulo': 'Frieren: Beyond Journey\'s End',
        'capitulos': 28,
        'finalizada': False,
        'capitulos_vistos': 20
    },
    {
        'titulo': 'The Apothecary Diaries',
        'capitulos': 24,
        'finalizada': True,
        'capitulos_vistos': 18
    },
    {
        'titulo': 'Hunter x Hunter',
        'capitulos': 148,
        'finalizada': False,
        'capitulos_vistos': 100
    },
    {
        'titulo': 'Fullmetal Alchemist: Brotherhood',
        'capitulos': 64,
        'finalizada': True,
        'capitulos_vistos': 64
    },
    {
        'titulo': 'Wind Breaker',
        'capitulos': 13,
        'finalizada': True,
        'capitulos_vistos': 8
    }
]

def series_finalizadas_sin_acabar(series_lista):
    series_pendientes = []
    for serie in series_lista:
        if serie['finalizada'] and serie['capitulos_vistos'] < serie['capitulos']:
            series_pendientes.append(serie)

    return series_pendientes

print(series_finalizadas_sin_acabar(series))