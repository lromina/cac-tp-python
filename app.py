
from flask import Flask, render_template, request, redirect, send_from_directory, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuración de la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''  
app.config['MYSQL_DB'] = 'bd_recetario'
app.config['UPLOAD_FOLDER'] = 'uploads'

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
    
@app.route('/listar-recetas')
def listar_receta():
    try:
        # Crear una conexión
        conn = mysql.connection
        cursor = conn.cursor()

        # Seleccionar la base de datos
        cursor.execute(f"USE {app.config['MYSQL_DB']}")

        # Consulta SQL para obtener los detalles de la receta
        sql = "SELECT * FROM recetas"
        
        # Ejecutar la consulta SQL
        cursor.execute(sql)

        # Traer todos los detalles de las recetas
        recetas = cursor.fetchall()
        
        cursor.close()
        
        # Pasar los detalles de la receta a la plantilla
        return render_template('recetario/listar-recetas.html', recetas=recetas)
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


@app.route('/uploads/<nombreFoto>')
def uploads(nombreFoto):
    return send_from_directory(app.config['UPLOAD_FOLDER'], nombreFoto)



## Eliminar

@app.route('/eliminar-receta/<int:id>', methods=['POST'])
def eliminar_receta(id):
    try:
        conn = mysql.connection
        cursor = conn.cursor()

        sql = "DELETE FROM recetas WHERE id = %s"
        cursor.execute(sql, (id,))
        conn.commit()

        cursor.close()
        return redirect(url_for('listar_receta'))
    except Exception as e:
        return f"Error: {str(e)}"
    
# @app.route('/editar-receta/<int:id>')
# def editar_receta(id):
#     try:
#         conn = mysql.connection
#         cursor = conn.cursor()
        
#         # Seleccionar la base de datos
#         cursor.execute(f"USE {app.config['MYSQL_DB']}")

#         sql = "SELECT * FROM recetas WHERE id = %s"
        
#         cursor.execute(sql, (id,))
        
#         receta = cursor.fetchall()
        
#         cursor.close()
        
#         return render_template('recetario/editar-receta.html', receta=receta)
#     except Exception as e:
#         return f"Error: {str(e)}"


# @app.route('/editar-receta/<int:id>', methods=['GET', 'POST'])
# def editar_receta(id):
#     try:
#         conn = mysql.connection
#         cursor = conn.cursor()

#         if request.method == 'POST':
#             nombre = request.form['nombre']
#             tiempo = request.form['tiempo']
#             ingredientes = request.form['ingredientes']
#             pasos = request.form['pasos']
#             categoria = request.form['categoria']
#             dificultad = request.form.getlist['dificultad']
#             imagen = request.files['imagen']

#             sql = """
#                 UPDATE recetas
#                 SET nombre = %s, tiempo = %s, ingredientes = %s, pasos = %s, categoria = %s, dificultad = %s, imagen = %s
#                 WHERE id = %s
#             """
#             cursor.execute(sql, (nombre, tiempo, ingredientes, pasos, categoria, dificultad, imagen, id))
#             conn.commit()

#             return redirect(url_for('detalle_receta', id=id))

#         sql = "SELECT * FROM recetas WHERE id = %s"
#         cursor.execute(sql, (id,))
#         receta = cursor.fetchone()
#         cursor.close()

#         return render_template('recetario/editar-receta.html', receta=receta)
#     except Exception as e:
#         return f"Error: {str(e)}"

@app.route('/editar-receta/<int:id>', methods=['GET', 'POST'])
def editar_receta(id):
    conn = mysql.connection
    cursor = conn.cursor()
    
    if request.method == 'POST':
        # Procesar el formulario de edición
        nombre = request.form['nombre']
        tiempo = request.form['tiempo']
        ingredientes = request.form['ingredientes']
        pasos = request.form['pasos']
        categoria = request.form['categoria']
        dificultad = ','.join(request.form.getlist('dificultad'))  # Concatenar dificultades seleccionadas
        imagen = request.files['imagen']
        
        # Si hay una nueva imagen, guardarla
        # if imagen.filename != '':
        #     filename = secure_filename(imagen.filename)
        #     imagen.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # else:
        #     filename = None

        # Actualizar la receta en la base de datos
        sql = """
            UPDATE recetas
            SET nombre = %s, tiempo = %s, ingredientes = %s, pasos = %s, categoria = %s, dificultad = %s, imagen = %s
            WHERE id = %s
        """
        cursor.execute(sql, (nombre, tiempo, ingredientes, pasos, categoria, dificultad, imagen, id))
        conn.commit()

        return redirect('/listar-recetas')

    # Obtener los datos de la receta para editar
    cursor.execute("SELECT * FROM recetas WHERE id = %s", (id,))
    receta = cursor.fetchone()
    cursor.close()

    return render_template('recetario/editar-receta.html', receta=receta)



if __name__ == '__main__':
    app.run(debug=True)

