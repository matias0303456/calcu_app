import os
from flask import (
    Flask, render_template, request
)

def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        resultado=''
        if request.method == 'POST':
            while True:
                try:
                    cantidad = request.form['cantidad']
                    cifra = request.form['cifra']
                    resultado = (float(cantidad)*float(cifra))/100
                    if resultado == int(resultado):
                        return render_template('index.html', 
                        cantidad=cantidad, cifra=cifra, 
                        resultado=str(int(resultado)))
                    else:
                        return render_template('index.html', 
                        cantidad=cantidad, cifra=cifra, 
                        resultado=str(resultado))
                    break
                except ValueError:
                    return render_template('index.html', 
                    error='''Error: debe ingresar números enteros 
                    o decimales con puntos. Por ejemplo: 1.2''')
        return render_template('index.html')
    return app