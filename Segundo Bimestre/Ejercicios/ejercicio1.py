nombre_equipo = ""
partidos_vistos = 
duracion_partido = 


nombre_equipo = input ("Introduce el nombre del equipo")
partidos_vistos = int(input("Introduce el numero de partidos vistos"))
duracion_partido = int(input("Introduce la duracion promedio de cada partido en minutos"))

print ("Juan ha visto", partidos_vistos, "partidos del equipo", nombre_equipo, "con una duracion promedio de", duracion_partido, "minutos")
print ("Juan ha visto", partidos_vistos * duracion_partido, "minutos en total")

