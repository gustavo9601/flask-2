# pip3 install Flask
from flask import Flask, render_template, request, url_for, redirect, abort
import mysql.connector

# Seteando en el ambiente el nombre del archivo
# set FLASK_APP=main.py
# Setando a modo desarrollo para que se reinicie al hacer cambios
# set FLASK_ENV=development
# set => windows export  => linux

# Ejecutar y levantar el server de flask
# flask run

app = Flask(__name__)

# Path a ejecutar
@app.route("/")
def index():
    # render_template(file inside folder templates)
    return render_template('index.html')

# Path a ejecutar
@app.route("/test")
def test():
    # render_template(file inside folder templates)
    return render_template('test.html')

# Especificando el tipo de dato a recibir
@app.route('/test/age/<int:age>')
def test_age(age):
    return "The age send is: " + str(age)

@app.route('/test/<name>')
def test_name(name):
    return "The name send is: " + name

# methods=[Verbos HTTP]
@app.route('/test_methods', methods=['POST'])
def test_methods():
    if request.method == 'POST':
        return "TTeh request is way POST :) "
    else:
        return "Not allowed this method :( "


@app.route('/test_methods/post', methods=['POST'])
def test_methods_with_fields():
    # Retornara todos los campos enviados por formulario
    print(request.form)
    # Accedediendo al dato que nos indetersa, ya que se devuelve una tupla
    # request.form['llave1']

@app.route('/404')
def redirect_to_index():
    # url_for(name_function, params)
    print('url de index', url_for('index'))

    # redirect(url to redirect)
    return redirect(url_for('index'))


@app.route('/abort')
def abort_request():
    # abort(Code error 404 | 401 | 500)
    abort(500)

@app.route('/json')
def return_json():
    return {
        "name" : "gus",
        "surname" : "mar"
    }


# Conexion global
midb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='test_py'
)


@app.route('/conexion-bd')
def connnection_bd():
    # dictionary=True
    # Se especifica que el orden de la tupla debe ser por el nombre de la columna y no indice
    cursor = midb.cursor(dictionary=True)

    query = 'select * from users'
    cursor.execute(query)
    usuarios = cursor.fetchall()

    # Renderizando la plantilla connection.html y pasando la variable usuarios
    return render_template('connection.html', usuarios=usuarios)



"""
# Ejecutando el servicio de Flask
# Otra forma es con la siguiente linea
# python filename.py
debug=True # Permite estar en modo desarrollo y refrescar el servidor automaticamente
"""
app.run(
    debug=True
)

