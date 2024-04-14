from flask import Flask, render_template 
app = Flask(__name__)
# rutas
@app.route('/')
def raiz():
    titulo = "Página inicio"
    return render_template('inicio.html',titulo=titulo)

# ruta para nosotros
@app.route('/nosotros')
def nosotros():
    titulo = "Nosotros"
    return render_template('nosotros.html',titulo=titulo)

# ruta para nosotros
@app.route('/entrenamientos')
def entrenamientos():
    titulo = "Entrenamientos"
    return render_template('entrenamientos.html',titulo=titulo)


# bloque de prueba
if __name__ == "__main__":
    app.run(debug=True)