def act__repre (cursor,conexion,ci,nom,ape,tlf,dir):
    
    cursor.execute("UPDATE representantes SET nombres = %s, apellidos = %s, telefono = %s, direccion = %s WHERE cedula = %s",
                       (nom, ape, tlf, dir, ci))
    conexion.commit()


def act__stud(cursor,conexion,nom1, nom2, ape1, ape2, eda, ci, ci_repre, id):
    cursor.execute("UPDATE estudiante SET 1er_nombre = %s, 2do_nombre = %s, 1er_apellido = %s, 2do_apellido = %s, edad = %s, cedula = %s, cedula_representante = %s WHERE id = %s",
                       (nom1, nom2, ape1, ape2, eda, ci, ci_repre, id))
    conexion.commit()
       

    