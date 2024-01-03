# Importar Flask y random
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import random


# Crear la aplicación Flask
app = Flask(__name__)
Bootstrap(app)

# Definir la lista de restaurantes
restaurantes = ['El desembarco',
            'Palacio de las milanesas',
            'Birra brava',
            'Felini pocitos',
            'Vintage pool',
            'Costa azul',
            'Restaurante Hong kong',
            'Erevan',
            'La carbonada',
            'Don aurelio',
            'Valerio',
            'Bigga',
            'Britanico',
            'Parrillada Trouville',
            'Parrillada las leñas',
            'Tapa Tapita',
            'Central Friends',
            'Hugo Soca',
            'Francis',
            'HDP',
            'Rudy',
            'Burguer Time!',
            'Bruta']

# Definir la ruta principal
@app.route("/")
def index():
    # Mostrar la plantilla index.html con la introducción
    return render_template("index.html")

# Definir la ruta para elegir el restaurante
@app.route("/elegir")
def elegir():
    # Elegir un restaurante al azar de la lista
    restaurante = random.choice(restaurantes)
    # Mostrar la plantilla elegir.html con el nombre del restaurante
    return render_template("elegir.html", restaurante=restaurante)

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run(debug=True)
