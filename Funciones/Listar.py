# Funciones para obtener datos de la base de datos
def obtener_datos_representantes(cursor):
   
    cursor.execute("SELECT cedula, nombres, apellidos, telefono, direccion FROM representantes")
    datos = cursor.fetchall()
    
    return datos

def obtener_datos_estudiantes(cursor):
    
    cursor.execute('''
        SELECT e.id, e.1er_nombre, e.2do_nombre, e.1er_apellido, e.2do_apellido, e.edad, e.cedula, e.cedula_representante
        FROM estudiante AS e
    ''')
    datos = cursor.fetchall()
    
    return datos

