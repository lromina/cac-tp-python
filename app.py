
from flask import Flask, render_template, request, redirect
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

if __name__ == '__main__':
    app.run(debug=True)


# from flask import Flask, render_template
# from flask_mysqldb import MySQL

# #IMPORTAMOS EL ERROR PARA MANEJAR LA CONEXION CON LA BASE DE DATOS

# import MySQLdb

# # Crear una aplicación
# app = Flask(__name__)

# # Configuración de la base de datos
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# app.config['MYSQL_DATABASE_USER'] = 'root'  # Usuario MySQL
# app.config['MYSQL_DATABASE_PASSWORD'] = ''  # Contraseña MySQL
# app.config['MYSQL_DATABASE_DB'] = 'bd_recetario'  # Nombre de la base de datos

# # Inicializamos MySQL
# mysql = MySQL(app)

# # Ruta de la raiz del sitio
# @app.route('/')
# def index():
#     # Creamos una variable que va a contener la consulta sql
#     sql = """
#     INSERT INTO recetas (id, nombre, tiempo, ingredientes, pasos, categoria, dificultad, imagen)
#     VALUES (NULL, 'Pastas con Atun', '16 minutos', 
#             '1 Cucharada de aceite de oliva - 1 Pimiento rojo cortado en bastones - Taza de cebolla picada - 3 Cucharadas de Salsa de Soya - 1 crema de leche - Latas de atún en agua (130 g c/u)', 
#             'En una sartén, calienta el aceite de oliva y fríe los pimientos y la cebolla hasta que doren ligeramente. En un tazón, mezcla la pasta con la Salsa de Soya, la crema, el atún y la mezcla de pimientos y cebolla. Mezcla hasta integrar, sirve en un plato y disfruta.', 
#             'pastas', 'baja', 
#             'https://www.recetasnestle.com.mx/sites/default/files/styles/recipe_detail_desktop/public/srh_recipes/7bbf8946c57d7f04ac3fb68174372128.webp?itok=YAZf8D5v')
#     """
    
#     try:
#         # Conectamos a la base de datos
#         conn = mysql.connection
#         cursor = conn.cursor()
        
#         # Ejecutamos la consulta sql
#         cursor.execute(sql)
        
#         # Commiteamos y cerramos la conexión
#         conn.commit()
#         cursor.close()
#     except MySQLdb.OperationalError as e:
#         print(f"Error de conexión: {e}")
#         return "Error de conexión a la base de datos"
#     except Exception as e:
#         print(f"Error al ejecutar la consulta: {e}")
#         return "Error al acceder a la base de datos"
    
#     return render_template('recetario/index.html') # Me devuelve el index

# # Estas lineas son requeridas por Python para empezar a trabajar con la app
# if __name__ == '__main__':
#     app.run(debug=True)
