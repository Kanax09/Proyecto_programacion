

def agg__repre(cursor,conexion,ci,nom,ape,tlf,dir):
        cursor.execute("INSERT INTO representantes (cedula, nombres, apellidos, telefono, direccion) VALUES (%s, %s, %s, %s, %s)", (ci, nom, ape, tlf, dir))
        conexion.commit()

def agg_stu(cursor,conexion,nom1, nom2, ape1, ape2, eda, ci, ci_repre):

    cursor.execute("INSERT INTO estudiante (1er_nombre, 2do_nombre, 1er_apellido, 2do_apellido, edad, cedula, cedula_representante) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                       (nom1, nom2, ape1, ape2, eda, ci, ci_repre))
    conexion.commit()
        
        
   


        

        
