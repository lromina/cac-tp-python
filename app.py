
from flask import Flask, render_template, request, redirect, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuración de la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''  # Asegúrate de que esta contraseña sea correcta
app.config['MYSQL_DB'] = 'bd_recetario'

mysql = MySQL(app)

@app.route('/')
def index():
    try:
        # Crear una conexión
        conn = mysql.connection
        cursor = conn.cursor()

        # Seleccionar la base de datos
        cursor.execute(f"USE {app.config['MYSQL_DB']}")

        # Consulta SQL para obtener datos
        sql = "SELECT * FROM recetas"
        
        # Ejecutar la consulta SQL
        cursor.execute(sql)

        # Traer las recetas
        recetas = cursor.fetchall()
        
        cursor.close()
        
        # Pasar las recetas a la plantilla
        return render_template('recetario/index.html', recetas=recetas)
    except Exception as e:
        return f"Error: {str(e)}"
@app.route('/detalle-receta/<int:id>')
def detalle_receta(id):
    try:
        # Crear una conexión
        conn = mysql.connection
        cursor = conn.cursor()

        # Seleccionar la base de datos
        cursor.execute(f"USE {app.config['MYSQL_DB']}")

        # Consulta SQL para obtener los detalles de la receta
        sql = "SELECT * FROM recetas WHERE id = %s"
        
        # Ejecutar la consulta SQL
        cursor.execute(sql, (id,))

        # Traer los detalles de la receta
        receta = cursor.fetchone()
        
        cursor.close()
        
        # Pasar los detalles de la receta a la plantilla
        return render_template('recetario/detalle-receta.html', receta=receta)
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/quienes_somos')
def quienes_somos():
    return render_template('recetario/quienes_somos.html')

@app.route('/registrate')
def registrate():
    return render_template('recetario/registrate.html')


@app.route('/iniciar_sesion')
def iniciar_sesion():
    return render_template('recetario/iniciar_sesion.html')
    
@app.route('/create')
def create():
    return render_template('recetario/create.html')

@app.route('/store', methods=['POST'])
def storage():
    #RECIBIR LOS VALORES DEL FORMULARIO y los guarda en variables
    _nombre = request.form['nombre']
    _tiempo = request.form['tiempo']
    _ingredientes = request.form['ingredientes']
    _pasos = request.form['pasos']
    _categoria = request.form['categoria']
    _dificultad = request.form['dificultad']
    _imagen = request.files['imagen']
    
    #guardamos los datos en una tupla
    
    datos = (_nombre, _tiempo, _ingredientes, _pasos, _categoria, _dificultad, _imagen.filename)
    
    #Armamos la sentencia SQL para subir los datos. 
    
    sql = "INSERT INTO recetas (id, nombre, tiempo, ingredientes, pasos, categoria, dificultad, imagen)\
        VALUES (NULL, %s, %s, %s, %s, %s, %s, %s)"
 
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    # Confirmar la transacción
    conn.commit()
    
     # Usar flash para mostrar el mensaje de éxito
    # flash('Receta creada satisfactoriamente')

    return redirect('create')


if __name__ == '__main__':
    app.run(debug=True)

