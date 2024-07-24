def Actualizar_representante(cursor,conexion):


    try:
        ci= input("Ingrese la cedula: ")

        #Se pide la consulta y se guarda el valor (%s) como ci en la parte de busqueda
        consulta= "SELECT EXISTS(SELECT * FROM representantes WHERE cedula = %s)"
        busqueda= (ci,)
        cursor.execute(consulta,busqueda)
        
        #Aqui devuelve TRUE si consigue el registro, de lo contrario retorna NONE
        verificacion = cursor.fetchone()[0]

        if verificacion:
                        
            consulta= '''UPDATE representantes 
                       SET representantes.nombres= %s, 
                       representantes.apellidos=%s,
                       representantes.telefono=%s,
                       representantes.direccion=%s Where cedula= %s;'''

            new_nom= input ("Ingrese los nombres: ")
            new_ape= input ("Ingrese los apellidos: ")
            new_tlf= input ("Ingrese los telefono: ")
            new_dir= input ("Ingrese los direccion: ")
            val= (new_nom,new_ape,new_tlf,new_dir,ci)
            cursor.execute(consulta,val)
            conexion.commit()

            print("USUARIO ACTUALIZADO :) ")

        else:
            print("La cedula ingresada no existe :(")

    except Exception as error:
        print(f"Ocurrio un error {error}")


def Actualizar_estudiante(cursor,conexion):
    try:
        #Aqui pedimos por los dos nombres y los dos apellidos
        #DE MOMENTO QUEDARA ASi
        nom1= input("Ingrese El primer nombre: ")
        nom2= input("Ingrese El segundo nombre: ")
        ape1= input("Ingrese el primer apellido:")
        ape2= input("Ingrese el segundo apellido:")


        consulta= '''SELECT EXISTS(SELECT * FROM estudiante 
                    WHERE 1er_nombre = %s and 2do_nombre = %s and 1er_apellido= %s and 2do_apellido= %s)'''
        nombre= (nom1,nom2,ape1,ape2)
        cursor.execute(consulta,nombre)

        verificacion = cursor.fetchone()[0]

        

        if verificacion:
            
            #Aqui buscamos rapidamente el id del estudiante ingresado para que no cambie el id actual
            cursor.execute("SELECT id,1er_nombre,2do_nombre,1er_apellido,2do_apellido FROM estudiante")
            for aux,nombre1,nombre2,apellido1,apellido2 in cursor:
                if nom1==nombre1 and (nom2==nombre2 and ape1==apellido1 and ape2==apellido2 ):
                    x=aux

            #y si esta larga la sentencia sin embargo no parece haber mucha redundancia en los datos
            #ya que no hay nada que determine que no tengas una o mas operaciones en el futuro
            # al igual que nada asegura que no desarrolles otras alergias mas adelante            
            actualizar= '''UPDATE estudiante
                        SET estudiante.id = %s,
                        estudiante.1er_nombre = %s,
                        estudiante.2do_nombre = %s,
                        estudiante.1er_apellido = %s,
                        estudiante.2do_apellido = %s,
                        estudiante.edad = %s,
                        estudiante.cedula = %s,
                        estudiante.cedula_representante = %s
                        WHERE 1er_nombre = %s AND 2do_nombre= %s AND 1er_apellido=%s AND 2do_apellido= %s;'''
            
            #Aqui le pasamos el id que conseguimos recien
            new_id=x
            new_nom1= input ("Ingrese El primer nombre: ")
            new_nom2= input ("Ingrese el segundo nombre: ")
            new_ape1= input ("Ingrese el primer apellido: ")
            new_ape2= input ("Ingrese el segundo apellido: ")
            new_eda= int(input ("Ingrese la edad: "))
            new_ced= input ("Ingrese la cedula(Si no tiene ingrese 0): ")
            new_repre=int(input("Ingrese la cedula del representante:")) 

            if new_ced == "0":
                new_ced="X"

            #tiene que seguir el orden segun la sentencia
            crede= (new_id,new_nom1,new_nom2,new_ape1,new_ape2,new_eda,new_ced,new_repre,nom1,nom2,ape1,ape2)
            cursor.execute(actualizar,crede)
            conexion.commit()

            print("USUARIO ACTUALIZADO :) ")

        else:
            print("La cedula ingresada no existe :(")


    except Exception as e:
        
         print(f"ocurrio un error {e}")

       

    