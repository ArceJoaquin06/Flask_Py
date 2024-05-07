from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/contacto')
def contacto():
    return "contactos"

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.2', port=3500)

 