from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

@app.route('/')
def principal():
    return "Bienvenidos internautas a la página del mejor jugador de Arena"

@app.route('/contacto')
def contacto():
    return "contactos"
