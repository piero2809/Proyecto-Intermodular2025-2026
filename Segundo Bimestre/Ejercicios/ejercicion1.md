En programación, interactuar con el usuario es clave para crear aplicaciones útiles y dinámicas.
Este ejercicio usa `input()` para pedir datos al usuario y hacer un cálculo simple.

- **`nombre_equipo`**: Guarda el texto tal cual lo escribe el usuario.
- **`partidos_vistos` y `duracion_partido`**: Se convierten a números enteros con `int()` para poder hacer operaciones matemáticas con ellos.

Después, el programa muestra dos resultados:

1. Un resumen con los datos introducidos.
2. El cálculo total de minutos viendo partidos (`partidos_vistos` \* `duracion_partido`).

```python
nombre_equipo = ""
partidos_vistos =
duracion_partido =


nombre_equipo = input ("Introduce el nombre del equipo")
partidos_vistos = int(input("Introduce el numero de partidos vistos"))
duracion_partido = int(input("Introduce la duracion promedio de cada partido en minutos"))

print ("Juan ha visto", partidos_vistos, "partidos del equipo", nombre_equipo, "con una duracion promedio de", duracion_partido, "minutos")
print ("Juan ha visto", partidos_vistos * duracion_partido, "minutos en total")
```

En resumen, este ejercicio sirve para entender cómo fluyen los datos en un programa.
Nos ayuda a practicar cosas básicas pero importantes: capturar datos, convertir tipos y hacer cálculos.
