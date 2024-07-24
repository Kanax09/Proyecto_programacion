
def Agregar_representante(cursor,conexion):
                #Aqui en caso de que no exista la tabla se crea automaticamente
                #si no existe claro esta
                  
                try:
                    agregar= "INSERT INTO representantes VALUES (%s,%s,%s,%s,%s);"              

                    ci= int(input("Ingrese la cedula:"))
                    nom= input("Ingrese los nombres: ")
                    ape=input("Ingrese los apellidos: ")
                    tlf= int(input("Ingrese la telefono: "))
                    dir= input("Ingrese la direccion:")


                    valores= (ci,nom,ape,tlf,dir)
                    cursor.execute(agregar,valores)
                    conexion.commit()

                    print("USUARIO INGRESADO :) ")

                except Exception as e:
                       print("Ocurrio un error")

def Agregar_estudiante(cursor,conexion):
        
         #Aqui en caso de que no exista la tabla se crea automaticamente
         #si no existe claro esta

        try:

            agregar= "INSERT INTO estudiante VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"              

            #El id queda en None para que siga la secuencia del auto increment
            #Asi ellos no se tendran que precupar por un id

            id=None
            nom1= input("Ingrese El primer nombre: ")
            nom2= input("Ingrese El segundo nombre: ")
            ape1=input("Ingrese El primer apellido: ")
            ape2=input("Ingrese El segundo apellido: ")
            eda= int(input("Ingrese la edad: "))
            ci= input("Ingrese la cedula(ingrese 0 si no tiene):")
            ci_repre=int(input("Ingrese la cedula del representante"))

            #Esto es basicamente por estilo para que guarde una X en la casilla de cedula en caso de no tener
            if ci=="0":
                    ci="X"

            #Aqui se guardan los valores ingresados, recordar que si se guarda asi es por el orden de la tabla
            #los valores se ajustan a los valores en blanco (%s) en la sentencia
            valores= (id,nom1,nom2,ape1,ape2,eda,ci,ci_repre)
            cursor.execute(agregar,valores)
            conexion.commit()

            print("USUARIO INGRESADO :) ")
        except Exception as e:
            print(f"Ocurrio un error {e}")


        

        
