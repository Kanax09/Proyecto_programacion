import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageOps  # Asegúrate de tener Pillow instalado (pip install pillow)

USUARIO_ADMIN = "admin"
CONTRASENA_ADMIN = "admin1234"

def iniciar_sesion():
    username = username_entry.get()
    password = password_entry.get()

    if username == USUARIO_ADMIN and password == CONTRASENA_ADMIN:
        root.destroy() 
        import Menu_Principal  
    else:
        messagebox.showwarning("Error", "Nombre de usuario o contraseña incorrectos")

# ventana de login
root = tk.Tk()
root.title("Inicio de Sesión")
root.geometry("400x400")

# Cargar imagen (asegúrarse de tener una imagen en el mismo directorio)
try:
    img = Image.open("login_image.png")  
    img = img.resize((270, 146), Image.Resampling.LANCZOS)  
    img = ImageTk.PhotoImage(img)
    img_label = tk.Label(root, image=img)
    img_label.pack(pady=10)
except FileNotFoundError:
    pass

# Título
title_label = tk.Label(root, text="Inicio de Sesión", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Formulario
form_frame = tk.Frame(root)
form_frame.pack(pady=10)

tk.Label(form_frame, text="Nombre de Usuario:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
username_entry = tk.Entry(form_frame)
username_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Contraseña:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
password_entry = tk.Entry(form_frame, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)

# Botón de inicio de sesión
login_button = tk.Button(root, text="Iniciar Sesión", command=iniciar_sesion, bg="#1976D2", fg="white", font=("Helvetica", 12))
login_button.pack(pady=20)

root.mainloop()
