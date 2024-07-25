import tkinter as tk
from tkinter import messagebox

USUARIO_ADMIN = "admin"
CONTRASENA_ADMIN = "admin1234"

def iniciar_sesion():
    username = username_entry.get()
    password = password_entry.get()

    if username == USUARIO_ADMIN and password == CONTRASENA_ADMIN:
        root.destroy() 
        import gui  
    else:
        messagebox.showwarning("Error", "Nombre de usuario o contraseña incorrectos")

# ventana de login
root = tk.Tk()
root.title("Inicio de Sesión")

tk.Label(root, text="Nombre de Usuario:").grid(row=0, column=0, padx=5, pady=5)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Contraseña:").grid(row=1, column=0, padx=5, pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)

login_button = tk.Button(root, text="Iniciar Sesión", command=iniciar_sesion)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
