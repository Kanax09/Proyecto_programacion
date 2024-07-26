
def del__repre(cursor,conexion,ci):
        cursor.execute("DELETE FROM estudiante WHERE cedula_representante = %s", (ci,))
        cursor.execute("DELETE FROM representantes WHERE cedula = %s", (ci,))
        conexion.commit()

def del__stu(cursor,conexion,id):
        cursor.execute("DELETE FROM estudiante WHERE id = %s", (id,))
        conexion.commit()
    
       
           
          