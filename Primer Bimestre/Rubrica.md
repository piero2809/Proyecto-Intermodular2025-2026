## 1.-Introducción breve y contextualización - 25% de la nota del ejercicio
En el desarrollo web moderno, uno de los pilares fundamentales es la interacción entre aplicaciones y bases de datos. Flask, un microframework de Python, permite crear aplicaciones web ligeras y rápidas, ideales para proyectos educativos o de pequeña escala. Por su parte, MySQL es un sistema de gestión de bases de datos relacional ampliamente utilizado para almacenar y gestionar información estructurada.

## 2.-Desarrollo detallado y preciso - 25% de la nota del ejercicio
- Incluir definiciones correctas y completas.
- Usar terminología técnica apropiada al temario.
- Explicar el funcionamiento paso a paso si es un proceso.
- Dar ejemplos reales o de código (si procede).

## 3.-Aplicación práctica - 25% de la nota del ejercicio
```
import mysql.connector                    # Importo el conector a base de datos
from flask import Flask                   # Importo la libreria Flask

conexion = mysql.connector.connect(
  host="localhost",
  user="portafolioexamen",
  password="1portafolioexamen",
  database="portafolioexamen"
  )                                       # Me conecto a la base de datos
cursor = conexion.cursor()                # Creo un cursor
app = Flask(__name__)                     # Creo una aplicación Flask (web)

@app.route("/")                           # Atrapo la ruta raiz (/)
def holamundo():                          # Defino una funcion
  cursor.execute("SELECT * FROM piezas_y_categorias;")  # Pido el contenido de la vista

  filas = cursor.fetchall()                 # Lo guardo en una lista
  ########### AQUI PONGO EL INICIO HASTA EL MAIN
  cadena = ''' 
<!doctype html>
<html lang="es">
  <head>
    <title>Examen</title>
    <meta charset="utf-8">
    <style>
      html,body{background:rgb(92, 88, 148);font-family:sans-serif;}
      header,main,footer{
        background:rgb(96, 170, 154);
        padding:20px;
        width:800px;
        margin:auto;
        text-align:center;
      }
      main{
        display:grid;
        grid-template-columns:auto auto auto;
        gap:20px;
      }
    </style>
  </head>
  <body>
    <header>
      <h1>Piero Funes Larios</h1>
      <h2>pierofl2005@gmail.com</h2>
    </header>
    <main>
  '''                               # Creo una cadena vacia
  ########### AQUI PONGO LO QUE SE REPITE
  for fila in filas:                        # Para cada elemento de la lista
    cadena += '''
      <article>
        <p>Categoria</p>
        <h3>Titulo</h3>
        <p>Descripcion</p>
        <img src="https://media.tenor.com/-C5C2LkQPTMAAAAM/sillynubcat-unzips-unzips.gif">
      </article>
    '''
  ########### AQUI PONGO EL FINAL
  cadena += ''' 
 </main>
    <footer>
      (c) 2025 Piero Funes Larios
    </footer>
  </body>
</html>
  '''
  return cadena                             # Devuelvo la cadena como HTML en la web

if __name__ == "__main__":                # Si este es el archivo principal
    app.run(debug=True)                   # Ejecuta la web
```
## 4.-Conclusión breve - 25% de la nota del ejercicio
Este ejercicio demuestra cómo integrar Python con una base de datos MySQL y generar contenido dinámico en una página web mediante Flask.
Se aplicaron conceptos clave como conexión a bases de datos, consultas SQL, estructuras HTML y rutas web.