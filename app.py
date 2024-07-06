
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

        # Consulta SQL para insertar datos
        # sql = "INSERT INTO recetas (nombre, tiempo, ingredientes, pasos, categoria, dificultad, imagen) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        # values = ('Pastas con Atun', '16 minutos', '1 Cucharada de aceite de oliva...', 'En una sartén, calienta el aceite de oliva...', 'pastas', 'baja', 'https://www.example.com/im...')

        sql = "Select * from recetas"
        
        # Ejecutar la consulta SQL
        # cursor.execute(sql, values)
        cursor.execute(sql)

        # Confirmar la transacción
        conn.commit()

        # Cerrar cursor y conexión
        # cursor.close()
        # conn.close()

        return render_template('recetario/index.html')

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

