#Si no lo tienen instalar: pip install mysql-connector-python
import mysql.connector 

def Conexionbd():

    # Credenciales de la conexion, lo unico que tienen que cambiar es el host, el user y la password a las credenciales que tengan
    # en mariadb u otros gestores, recordar que esta bd es de mysql
    #Las tablas se crean automaticamente a la hora de ingresar la informacion en ambos casos tanto de estudiantes 
    #como representantes, mirar los archivos agregar en la carpeta funciones

    host = "localhost"
    user = "root"
    password = "mortadela"
    database = "escuela_danza"
    charset='utf8mb4'
    collation='utf8mb4_general_ci'

    try:
        # Estableciendo conexion
        Conexion = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset=charset,
            collation=collation
        )

        #este print pueden borrarlo si les apetece
        print("Conexión exitosa a la base de datos")

        return Conexion

        
    # Aqui recoge el error y lo retorna como err y detecta si no se puede establecer una conexion
    # con la bd puesta en la credencial si no existe la crea

    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            aux = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                charset=charset,
                collation=collation
            )

            cur = aux.cursor()
            cur.execute(f"CREATE DATABASE {database}")
            print(f"Base de datos '{database}' creada correctamente.")

            Conexion = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset=charset,
            collation=collation
        )

            return Conexion

        else:
            print("Error al conectar a la base de datos:", err)
