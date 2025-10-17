
'''
Zona 1	50% – 60%	Muy suave / recuperación
Zona 2	60% – 70%	Aeróbico básico
Zona 3	70% – 80%	Aeróbico moderado
Zona 4	80% – 90%	Umbral anaeróbico
Zona 5	90% – 100%	Esfuerzo máximo '''

zonas = [0, 0, 0, 0, 0, 0]
def clasificar_zona(bps, edad):


    fcm = 220 - edad
    porcentaje = (bps / fcm) * 100
    dist = 0

    if 50 <= porcentaje < 60:
        dist = 0
    elif 60 <= porcentaje < 70:
        dist = 1
    elif 70 <= porcentaje < 80:
        dist = 2
    elif 80 <= porcentaje < 90:
        dist = 3
    elif 90 <= porcentaje <= 100:
        dist = 4
    else:
        dist = 5

    zonas[dist] += 1
    return zonas