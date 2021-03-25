from flask import Flask, render_template


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

# Ejecutando el servicio de Flask


"""
debug=True # Permite estar en modo desarrollo y refrescar el servidor automaticamente
"""
app.run(
    debug=True
)

