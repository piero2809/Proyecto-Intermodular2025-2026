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
            width: 800px;
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
    