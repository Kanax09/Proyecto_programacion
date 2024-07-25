from fpdf import FPDF
from datetime import datetime

# Obtiene la fecha y hora actuales
fecha_actual = datetime.now()

# variable para hacer multipdf la fecha y hora como una cadena (por ejemplo, "2024-07-25_09-30-15")
nombre_archivo = fecha_actual.strftime("Estudiantes_%Y-%m-%d_%H-%M") + ".pdf"

class PDF(FPDF):
    def header(self):
        # Logo de kelly
        self.image('logo.png', 10, 5, 30,17,'png')
        # Estilo de texto
        self.set_font('Arial', 'B', 15)
        # Mover para centrarlo
        self.cell(100)
        # Titulo
        self.cell(30, 10, 'REPORTE ESTUDIANTES', 0, 0, 'R')
        # Espaciado
        self.ln(20)

    # Page footer
    def footer(self):
        # Posicion no pegada al margen
        self.set_y(-15)
        # Estilo texto
        self.set_font('Arial', 'I', 8)
        # adquirir el numero de pagina
        self.cell(0, 10, 'N° Pagina ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

datos = [ ]*10

# Ejecutar la clase
pdf = PDF()
pdf.alias_nb_pages()

#funcion para declarar una pagina
pdf.add_page()
pdf.set_font('arial', "",10)
pdf.cell(w=14,h=15,txt= 'ID',border=1,align='C',fill=0,)
pdf.cell(w=45,h=15,txt= 'Nombres',border=1,align='C',fill=0,)
pdf.cell(w=45,h=15,txt= 'Apellidos',border=1,align='C',fill=0,)
pdf.cell(w=15,h=15,txt= 'Edad',border=1,align='C',fill=0,)
pdf.cell(w=35,h=15,txt= 'C.I',border=1,align='C',fill=0,)
pdf.multi_cell(w=0,h=15,txt= 'C.I-Representante',border=1,align='C',fill=0,)

for i,dato in enumerate(datos,1):
    #datos
    pdf.cell(w=14,h=8,txt= str(i),border=1,align='C',fill=0,)
    pdf.cell(w=45,h=8,txt= dato[0],border=1,align='C',fill=0,)
    pdf.cell(w=45,h=8,txt= (f"{dato[1]} {dato[0]}"),border=1,align='C',fill=0,)
    pdf.cell(w=15,h=8,txt= str(dato[2]),border=1,align='C',fill=0,)
    pdf.cell(w=35,h=8,txt= dato[3],border=1,align='C',fill=0,)
    pdf.multi_cell(w=0,h=8,txt= dato[4],border=1,align='C',fill=0,)
print("|=================================|")
print("\nREPORTE EN PDF Generado con Exito\n")
print("|=================================|")

#salida de datos, (ruta)
pdf.output(nombre_archivo, 'F')
