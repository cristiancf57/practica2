from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Inscripción en curso
@app.route('/curso', methods=['GET', 'POST'])
def curso():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        curso = request.form['curso']
        return render_template('result.html', form="Inscripción en curso", data={'Nombre': nombre, 'Apellido': apellido, 'Curso': curso})
    return render_template('curso.html')

# Registro de usuarios
@app.route('/usuarios', methods=['GET', 'POST'])
def usuarios():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        return render_template('result.html', form="Registro de usuarios", data={'Nombre': nombre, 'Apellido': apellido, 'Correo': correo})
    return render_template('usuarios.html')

# Registro de productos
@app.route('/productos', methods=['GET', 'POST'])
def productos():
    if request.method == 'POST':
        producto = request.form['producto']
        categoria = request.form['categoria']
        existencia = request.form['existencia']
        precio = request.form['precio']
        return render_template('result.html', form="Registro de productos", data={'Producto': producto, 'Categoría': categoria, 'Existencia': existencia, 'Precio': precio})
    return render_template('productos.html')

# Registro de libros
@app.route('/libros', methods=['GET', 'POST'])
def libros():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        resumen = request.form['resumen']
        formato = request.form['formato']
        return render_template('result.html', form="Registro de libros", data={'Título': titulo, 'Autor': autor, 'Resumen': resumen, 'Formato': formato})
    return render_template('libros.html')

if __name__ == '__main__':
    app.run(debug=True)
