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
  cursor.execute("SELECT * FROM piezas_y_categorias_examen;")  # Pido el contenido de la vista

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
        <img src="https://media.tenor.com/-C5C2LkQPTMAAAAM/sillynubcat-unzips-unzips.gif  ">
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