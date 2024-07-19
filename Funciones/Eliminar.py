def Eliminar_representante(cursor,conexion):
                try:
                    ci=  input("Ingrese La cedula: ")

                    #El comando de consulta es para verificar si existe una tabla llamada representantes
                    #y si existe eliga todos los elementos donde la cedula sea == a la ingresada
                    consulta= "SELECT EXISTS(SELECT * FROM representantes WHERE cedula = %s)"
                    cedula= (ci,)

                    #El valor de la cedula lo pasa por la variable cedula y cedula de consulta
                    #toma el valor de cedula por eso es que cedula va al final de el comando
                    cursor.execute(consulta,cedula)

                    #este comando devuelve solo un registro y devuelve TRUE si encuentra algo
                    #caso contrario devolvera un NONE
                    verificacion = cursor.fetchone()[0]

                    if verificacion:


                        #Aqui sucede mas de lo mismo que la explicacion de arriba
                        eliminacion= "DELETE FROM representantes WHERE cedula= %s"
                        val= (ci,)
                        cursor.execute(eliminacion,val)
                        conexion.commit()

                        print("USUARIO Eliminado :) ")

                    else:
                        print("La cedula ingresada no existe :(")

                except Exception as e:
                      
                        print(f"NO SE ENCONTRARON REGISTROS, INGRESE UNO PRIMERO {e}")

                    
                      

def Eliminar_estudiante(cursor,conexion):

       try:
        nom1= input("Ingrese El primer nombre: ")
        nom2= input("Ingrese El segundo nombre: ")
        ape1= input("Ingrese el primer apellido:")
        ape2= input("Ingrese el segundo apellido:")

        #Aqui que hay mas valores recordar que los valores TIENEN que ir en el orden que se establece en la consulta
        consulta= '''SELECT EXISTS(SELECT * FROM estudiante 
                    WHERE 1er_nombre = %s and 2do_nombre = %s and 1er_apellido= %s and 2do_apellido= %s)'''
        nombre= (nom1,nom2,ape1,ape2)
        cursor.execute(consulta,nombre)

        verificacion = cursor.fetchone()[0]



        if verificacion:

            
                    
            eliminacion= "DELETE FROM estudiante WHERE 1er_nombre= %s AND 2do_nombre = %s AND 1er_apellido = %s AND 2do_apellido=%s"
            val= (nom1,nom2,ape1,ape2)
            cursor.execute(eliminacion,val)
            conexion.commit()

            print("USUARIO Eliminado :) ")

        else:
            print("La cedula ingresada no existe :(")

       except Exception as e:
             print(f"ocurrio un error {e}")
                    
                    
          