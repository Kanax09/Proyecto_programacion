from Conexion import *
from Funciones.Listar import *
from Funciones.Eliminar import *
from Funciones.Actualizar import *
from Funciones.Agregar import *




#Este es un menu de prueba, lo pueden utilizar para probar si todo esta en orden
#si les lanza algun error me avisan

def Menu():

    conexion=Conexionbd()
    
    cursor=conexion.cursor()

    while True:

        print("\nMenu de administrador")
        print("1)Representantes")
        print("2)Estudiantes")
        print("3)Salir")
        op = input("ELIGA UNA OPCION PARA CONTINUAR:")


        if op == "1":
            while True:
                print("\nMenu basico representante")
                print("1)Ingresar")
                print("2)Eliminar")
                print("3)Listar")
                print("4)Actualizar")
                print("5)Volver")
                op=input("Ingrese una tecla para continuar:")

                match op:
                    
                    case "1":
                        Agregar_representante(cursor,conexion)

                    case "2":
                        Eliminar_representante(cursor,conexion)

                    case "3":
                        Mostrar_representante(cursor)

                    case "4":
                        Actualizar_representante(cursor,conexion)

                    case "5":
                        
                        break

        if op == "2":
            while True:
                print("\nMenu basico estudiante")
                print("1)Ingresar")
                print("2)Eliminar")
                print("3)Listar")
                print("4)Actualizar")
                print("5)Volver")
                op=input("Ingrese una tecla para continuar:")

                match op:
                    
                    case "1":
                        Agregar_estudiante(cursor,conexion)

                    case "2":
                        Eliminar_estudiante(cursor,conexion)

                    case "3":
                        Mostrar_estudiante(cursor)

                    case "4":
                        Actualizar_estudiante(cursor,conexion)

                    case "5":
                        
                        break

        if op == "3":
            print("CERRANDO APLICACION")
            cursor.close()
            break

            
Menu()