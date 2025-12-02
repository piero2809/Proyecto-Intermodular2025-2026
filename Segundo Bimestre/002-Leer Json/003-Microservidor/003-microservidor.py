##Importo Flask
from flask import Flask, render_template


##Creo una nueva app
app = Flask(__name__)
##Escucho la ruta raiz
@app.route ("/")
def inicio():
    ##Renderizo una plantilla llamada index.html
    return render_template("index.html")
##Si este archivo no es una libreria y es el archivo principal
if __name__ == "__main__":
    ##Pon en marcha la app
    app.run(debug=True)