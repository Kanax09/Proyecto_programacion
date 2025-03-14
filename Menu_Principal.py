import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re
import mysql.connector
from Conexion import Conexionbd
from Funciones.Pdf import *
from Funciones.Listar import *
from Funciones.Agregar import *
from Funciones.Eliminar import *
from Funciones.Actualizar import *

conexion=Conexionbd()
cursor=conexion.cursor()

# Validaciones
def validar_cedula(cedula):
    if not cedula.isdigit():
        return False
    if len(cedula) < 7:
        messagebox.showwarning("Advertencia", "La cédula debe tener mínimo 7 dígitos.")
        return False
    if len(cedula) > 10:
        messagebox.showwarning("Advertencia", "La cédula debe tener máximo 10 dígitos.")
        return False
    return True

def validar_telefono(telefono):
    return bool(re.match(r"^\d{10}$", telefono))  # Asumiendo que el teléfono debe tener 10 dígitos

def validar_nombre_apellido(nombre_apellido):
    # Verifica que solo haya un espacio entre palabras
    return bool(re.match(r"^[a-zA-Z]+(?: [a-zA-Z]+)*$", nombre_apellido))

def validar_edad(edad):
    return edad.isdigit() and 5 <= int(edad) <= 16

def validar_datos_representante(ci, nom, ape, tlf, dir):
    if not validar_cedula(str(ci)):
        return False
    if not validar_telefono(str(tlf)):
        messagebox.showwarning("Advertencia", "El teléfono debe tener 10 dígitos.")
        return False
    if not validar_nombre_apellido(nom) or not validar_nombre_apellido(ape):
        messagebox.showwarning("Advertencia", "Los nombres y apellidos solo deben contener letras y un espacio entre palabras.")
        return False
    if not dir:
        messagebox.showwarning("Advertencia", "La dirección no puede estar vacía.")
        return False
    return True

def validar_datos_estudiante(nom1, nom2, ape1, ape2, eda, ci, ci_repre):
    if not validar_nombre_apellido(nom1) or not validar_nombre_apellido(nom2):
        messagebox.showwarning("Advertencia", "Los nombres solo deben contener letras y un espacio entre palabras.")
        return False
    if not validar_nombre_apellido(ape1) or not validar_nombre_apellido(ape2):
        messagebox.showwarning("Advertencia", "Los apellidos solo deben contener letras y un espacio entre palabras.")
        return False
    if not validar_edad(str(eda)):
        messagebox.showwarning("Advertencia", "La edad debe ser un número entre 5 y 16.")
        return False
    if not validar_cedula(str(ci)) and ci != "X":
        return False
    if not validar_cedula(str(ci_repre)):
        return False
    return True

# Funciones CRUD para Representantes
def agregar_representante():
    ci = ci_entry.get()
    nom = nom_entry.get()
    ape = ape_entry.get()
    tlf = tlf_entry.get()
    dir = dir_entry.get()

    if not (ci and nom and ape and tlf and dir):
        messagebox.showwarning("Advertencia", "Debe ingresar todos los datos.")
        return

    if not validar_datos_representante(ci, nom, ape, tlf, dir):
        return

    try:
        agg__repre(cursor,conexion,ci,nom,ape,tlf,dir)
        messagebox.showinfo("Éxito", "Representante agregado exitosamente.")
        mostrar_representantes()
        mostrar_estudiantes()    
     
        
    except mysql.connector.Error:
        messagebox.showerror("Error", f"Exceso de caracteres en los campos o usuario ya ingresado")
    except Exception as e:
        messagebox.showerror("Error", f"ocurrio un error {e}")



def eliminar_representante():
    ci = ci_entry.get()

    if not validar_cedula(str(ci)):
        messagebox.showwarning("Advertencia", "La cédula debe contener solo números.")
        return

    try:
        
        del__repre(cursor,conexion,ci)
        messagebox.showinfo("Éxito", "Representante y estudiantes asociados eliminados exitosamente.")
        mostrar_representantes()
        mostrar_estudiantes()
          
     
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")
    

def actualizar_representante():
    ci = ci_entry.get()
    nom = nom_entry.get()
    ape = ape_entry.get()
    tlf = tlf_entry.get()
    dir = dir_entry.get()

    if not (ci and nom and ape and tlf and dir):
        messagebox.showwarning("Advertencia", "Debe ingresar todos los datos.")
        return

    if not validar_datos_representante(ci, nom, ape, tlf, dir):
        return
    try:
        act__repre(cursor,conexion,ci,nom,ape,tlf,dir)
        
        messagebox.showinfo("Éxito", "Datos del representante actualizados exitosamente.")
        mostrar_representantes()
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")
    
# Funciones CRUD para Estudiantes
def agregar_estudiante():
    nom1 = nom1_entry.get()
    nom2 = nom2_entry.get()
    ape1 = ape1_entry.get()
    ape2 = ape2_entry.get()
    eda = eda_entry.get()
    ci = ci_entry_est.get()
    ci_repre = ci_repre_entry.get()

    if not (nom1 and nom2 and ape1 and ape2 and eda and ci and ci_repre):
        messagebox.showwarning("Advertencia", "Debe ingresar todos los datos.")
        return

    if ci == "0":
        ci = "X"

    if not validar_datos_estudiante(nom1, nom2, ape1, ape2, eda, ci, ci_repre):
        return

    try:
       
        agg_stu(cursor,conexion,nom1, nom2, ape1, ape2, eda, ci, ci_repre)
        messagebox.showinfo("Éxito", "Estudiante agregado exitosamente.")
        mostrar_estudiantes()
        
    except mysql.connector.Error:
        messagebox.showerror("Error", f"Representantes no encontrado")

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")


def eliminar_estudiante():
    id = id_entry_est.get()

  
    try:
        
        del__stu(cursor,conexion,id)
        messagebox.showinfo("Éxito", "Estudiante eliminado exitosamente.")
        mostrar_estudiantes()

    except mysql.connector.Error:
        messagebox.showerror("Error", f"Id no enconrado")

    
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")
    

def actualizar_estudiante():
    id = id_entry_est.get()
    nom1 = nom1_entry.get()
    nom2 = nom2_entry.get()
    ape1 = ape1_entry.get()
    ape2 = ape2_entry.get()
    eda = eda_entry.get()
    ci = ci_entry_est.get()
    ci_repre = ci_repre_entry.get()

    if not (id and nom1 and nom2 and ape1 and ape2 and eda and ci and ci_repre):
        messagebox.showwarning("Advertencia", "Debe ingresar todos los datos.")
        return

    if ci == "0":
        ci = "X"

    if not validar_datos_estudiante(nom1, nom2, ape1, ape2, eda, ci, ci_repre):
        return

    
    try:

        act__stud(cursor,conexion,nom1, nom2, ape1, ape2, eda, ci, ci_repre, id)
        messagebox.showinfo("Éxito", "Datos del estudiante actualizados exitosamente.")
        mostrar_estudiantes()
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")


def mostrar_representantes():
    for widget in tabla_representantes_frame.winfo_children():
        widget.destroy()

    datos = obtener_datos_representantes(cursor)
    columns = ["Cédula", "Nombres", "Apellidos", "Teléfono", "Dirección"]
    tree = ttk.Treeview(tabla_representantes_frame, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150)

    for row in datos:
        tree.insert("", tk.END, values=row)

    tree.pack(fill=tk.BOTH, expand=True)

def mostrar_estudiantes():
    for widget in tabla_estudiantes_frame.winfo_children():
        widget.destroy()

    datos = obtener_datos_estudiantes(cursor)
    columns = ["ID", "1er Nombre", "2do Nombre", "1er Apellido", "2do Apellido", "Edad", "Cédula", "Cédula Repre"]
    tree = ttk.Treeview(tabla_estudiantes_frame, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    for row in datos:
        tree.insert("", tk.END, values=row)

    tree.pack(fill=tk.BOTH, expand=True)

def generar_reporte_representantes():
    datos = obtener_datos_representantes(cursor)

    pdf__repre(datos)
    
    messagebox.showinfo("Éxito", f"Reporte de representantes generado exitosamente")

def generar_reporte_estudiantes():
    datos = obtener_datos_estudiantes(cursor)

    pdf__stud(datos)
    
    messagebox.showinfo("Éxito", f"Reporte de estudiantes generado exitosamente:")

# ventana principal
root = tk.Tk()
root.title("Sistema de Registro Kellyart")

# Crear pestañas
notebook = ttk.Notebook(root)
notebook.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Ventana para Representantes
representantes_tab = ttk.Frame(notebook)
notebook.add(representantes_tab, text="Representantes")

# Formulario para Representantes
form_representantes = ttk.Frame(representantes_tab)
form_representantes.pack(pady=10, padx=10, fill=tk.X)

tk.Label(form_representantes, text="Cédula:").grid(row=0, column=0, padx=5, pady=5)
ci_entry = tk.Entry(form_representantes)
ci_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(form_representantes, text="Nombres:").grid(row=1, column=0, padx=5, pady=5)
nom_entry = tk.Entry(form_representantes)
nom_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(form_representantes, text="Apellidos:").grid(row=2, column=0, padx=5, pady=5)
ape_entry = tk.Entry(form_representantes)
ape_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(form_representantes, text="Teléfono:").grid(row=3, column=0, padx=5, pady=5)
tlf_entry = tk.Entry(form_representantes)
tlf_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(form_representantes, text="Dirección:").grid(row=4, column=0, padx=5, pady=5)
dir_entry = tk.Entry(form_representantes)
dir_entry.grid(row=4, column=1, padx=5, pady=5)

# Botones para Representantes
btn_frame_representantes = ttk.Frame(representantes_tab)
btn_frame_representantes.pack(pady=10, fill=tk.X)

tk.Button(btn_frame_representantes, text="Agregar Representante", command=agregar_representante, bg="#45a049", fg="white", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame_representantes, text="Eliminar Representante", command=eliminar_representante, bg="#d32f2f", fg="white", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame_representantes, text="Actualizar Representante", command=actualizar_representante, bg="#1976D2", fg="white", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame_representantes, text="Generar Reporte PDF", command=generar_reporte_representantes, bg="#FFC107", fg="black", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)

# Tabla de Representantes
tabla_representantes_frame = ttk.Frame(representantes_tab)
tabla_representantes_frame.pack(pady=10, fill=tk.BOTH, expand=True)

columns_representantes = ("Cédula", "Nombres", "Apellidos", "Teléfono", "Dirección")
tree_representantes = ttk.Treeview(tabla_representantes_frame, columns=columns_representantes, show='headings')
tree_representantes.pack(fill=tk.BOTH, expand=True)

for col in columns_representantes:
    tree_representantes.heading(col, text=col)
    tree_representantes.column(col, width=150)

# Ventana para Estudiantes
estudiantes_tab = ttk.Frame(notebook)
notebook.add(estudiantes_tab, text="Estudiantes")

# Formulario para Estudiantes
form_estudiantes = ttk.Frame(estudiantes_tab)
form_estudiantes.pack(pady=10, padx=10, fill=tk.X)

tk.Label(form_estudiantes, text="ID (para actualizar/eliminar):").grid(row=0, column=0, padx=5, pady=5)
id_entry_est = tk.Entry(form_estudiantes)
id_entry_est.grid(row=0, column=1, padx=5, pady=5)

tk.Label(form_estudiantes, text="1er Nombre:").grid(row=1, column=0, padx=5, pady=5)
nom1_entry = tk.Entry(form_estudiantes)
nom1_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(form_estudiantes, text="2do Nombre:").grid(row=2, column=0, padx=5, pady=5)
nom2_entry = tk.Entry(form_estudiantes)
nom2_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(form_estudiantes, text="1er Apellido:").grid(row=3, column=0, padx=5, pady=5)
ape1_entry = tk.Entry(form_estudiantes)
ape1_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(form_estudiantes, text="2do Apellido:").grid(row=4, column=0, padx=5, pady=5)
ape2_entry = tk.Entry(form_estudiantes)
ape2_entry.grid(row=4, column=1, padx=5, pady=5)

tk.Label(form_estudiantes, text="Edad:").grid(row=5, column=0, padx=5, pady=5)
eda_entry = tk.Entry(form_estudiantes)
eda_entry.grid(row=5, column=1, padx=5, pady=5)

tk.Label(form_estudiantes, text="Cédula (0 si no posee):").grid(row=6, column=0, padx=5, pady=5)
ci_entry_est = tk.Entry(form_estudiantes)
ci_entry_est.grid(row=6, column=1, padx=5, pady=5)

tk.Label(form_estudiantes, text="Cédula Representante:").grid(row=7, column=0, padx=5, pady=5)
ci_repre_entry = tk.Entry(form_estudiantes)
ci_repre_entry.grid(row=7, column=1, padx=5, pady=5)

# Botones para Estudiantes
btn_frame_estudiantes = ttk.Frame(estudiantes_tab)
btn_frame_estudiantes.pack(pady=10, fill=tk.X)

tk.Button(btn_frame_estudiantes, text="Agregar Estudiante", command=agregar_estudiante, bg="#45a049", fg="white", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame_estudiantes, text="Eliminar Estudiante", command=eliminar_estudiante, bg="#d32f2f", fg="white", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame_estudiantes, text="Actualizar Estudiante", command=actualizar_estudiante, bg="#1976D2", fg="white", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame_estudiantes, text="Generar Reporte PDF", command=generar_reporte_estudiantes, bg="#FFC107", fg="black", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)

# Tabla de Estudiantes
tabla_estudiantes_frame = ttk.Frame(estudiantes_tab)
tabla_estudiantes_frame.pack(pady=10, fill=tk.BOTH, expand=True)

columns_estudiantes = ("ID", "1er Nombre", "2do Nombre", "1er Apellido", "2do Apellido", "Edad", "Cédula", "Cédula Representante")
tree_estudiantes = ttk.Treeview(tabla_estudiantes_frame, columns=columns_estudiantes, show='headings')
tree_estudiantes.pack(fill=tk.BOTH, expand=True)

for col in columns_estudiantes:
    tree_estudiantes.heading(col, text=col)
    tree_estudiantes.column(col, width=100)

# datos iniciales
mostrar_representantes()
mostrar_estudiantes()

# Iniciar la aplicación
root.mainloop()