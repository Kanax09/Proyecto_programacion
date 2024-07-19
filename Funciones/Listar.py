
def Mostrar_representante(cursor):

    try:
        
        #la variable cursor devuelve todos los datos que encuentre en los registros
        #si quisieramos hacer una busqueda tendriamos que hacer una variable donde el usuario pase la cedula
        #y printe todo cuando la cedula sea == que la cedula que le pasamos
        cursor.execute("SELECT * FROM representantes")
        print("\n============================")
        for cedula,nombre,apellido,telefono,direccion in cursor:
            print ("Cedula: ", cedula)
            print ("Nombres: ", nombre)
            print ("Apellidos: ", apellido)
            print ("Telefono: ", telefono)
            print ("Direccion: ", direccion)
            print ("=====================")

    except Exception as error:
        print("Ocurrio un error",error)


def Mostrar_estudiante(cursor):

    try:
        
        #INNER indica la conexion que hay entre una tabla y otra
        #Los estudiantes se les tiene que pasar si o si una cedula de representante si no, no pueden ingresar
        #Aqui los que se hace es que se les pasa un seudonimo (estudiantes = e y representantes = r)
        #y funcionaria aqui como un objeto siendo e.id referente al id del estudiante
        
        inner= '''
                SELECT e.id,e.1er_nombre,e.2do_nombre,e.1er_apellido,e.2do_apellido,r.cedula,r.nombres
                FROM estudiante AS e 
                INNER JOIN representantes AS r ON e.cedula_representante = r.cedula
                
            '''
    
        cursor.execute(inner)
        print("\n============================")
        for id,nom1,nom2,ape1,ape2,ci_repre,r_nom in cursor:
            print ("id: ", id)
            print (f"Nombres: {nom1} {nom2}")
            print (f"Apellidos: {ape1} {ape2}")
            print ("Cedula del representante: ", ci_repre)
            print ("Nombre del representante: ", r_nom)
            print ("=====================")

    except Exception as error:
        print("Ocurrio un error",error)

