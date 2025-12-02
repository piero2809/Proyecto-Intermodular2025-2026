En el desarrollo web moderno, uno de los pilares fundamentales es la interacción entre aplicaciones y bases de datos. ``Flask``, un microframework de Python, permite crear aplicaciones web ligeras y rápidas, ideales para proyectos educativos o de pequeña escala. Por su parte, MySQL es un sistema de gestión de bases de datos relacional ampliamente utilizado para almacenar y gestionar información estructurada.

Primero se importa la librería Flask para desplegar una pagina web desde ``python`` y ``MySQL``.connector para manejar la base de datos. Luego, se establece la conexion a la base de datos utilizando el usuario creado anteriormente. Se crea el cursor para ejecutar las consultar respectivas a ``MySQL`` y se usa la aplicacion flask. Dentro de la definicion se copian partes del HTML que tienen que mostrarse en la pagina web. Se ejecuta la consulta a MySQL para obtener las filas de la tabla creada. Se crea una variable `cadena` para agregar el html, dentro de un bucle se recorre las cadenas obtenidas de la base de datos y se agregan al `article`. Finalmente se ciera el HTML y se retorna la cadena completa para que Flask la muestre en la pagina web.  
## Se realiza el ejercicio
```
from flask import Flask
import mysql.connector

conexion = mysql.connector.connect(
  host="localhost",
  user="portafolioexamen",
  password="1portafolioexamen",
  database="portafolioexamen"
)                                 
cursor = conexion.cursor()               
app = Flask(__name__) 

@app.route("/")                          
def holamundo():                         
    cursor.execute("SELECT * FROM piezas_y_categorias_examen;")
    filas = cursor.fetchall()
    cadena = '''
    <!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <title>Examen</title>
    <style>
        html,
        body {
            background: rgb(92, 88, 148);
            font-family: sans-serif;
        }

        header,
        main,
        footer {
            background: rgb(96, 170, 154);
            padding: 20px;
            width: 900px;
            margin: auto;
            text-align: center;
        }

        main {
            display: grid;
            grid-template-columns: auto auto auto;
            gap: 20px;
        }

        article img {
            width: 200px;
            height: 200px;
        }
    </style>
</head>

<body>
    <header>
        <h1>Portafolio examen</h1>
        <h2>Gestor de proyectos DAM DAW</h2>
        <h3>Piero Funes</h3>
    </header>
    <main>
    ''' 
    for fila in filas:
        cadena += '''
        <article>
            <p>'''+fila[0]+'''</p>
            <h3>'''+fila[1]+'''</h3>
            <p>'''+fila[2]+'''</p>
            <p>'''+fila[3]+'''</p>
            <img
                src="https://tse3.mm.bing.net/th/id/OIP.ZDVq-76UPggSR5zN5WGVrwHaHa?cb=ucfimg2ucfimg=1&rs=1&pid=ImgDetMain&o=7&rm=3">
        </article>
        '''
    cadena += '''
     </main>
    <footer>
        <p>(C) 2025 Piero Funes Larios</p>
    </footer>
</body>

</html>
    '''
    return cadena

if __name__ == "__main__":
    app.run(debug=True)
    
```

Este ejercicio demuestra cómo integrar Python con una base de datos MySQL y generar contenido dinámico en una página web mediante Flask.
Se aplicaron conceptos clave como conexión a bases de datos, consultas SQL, estructuras HTML y rutas web.