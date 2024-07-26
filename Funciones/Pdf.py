from fpdf import FPDF
from datetime import datetime

class PDF(FPDF):
        def header(self):
            self.image('logo.png', 10, 5, 30, 17, 'png')
            self.set_font('Arial', 'B', 15)
            self.cell(80)
            self.cell(30, 10, 'REPORTE GENERAL', 0, 0, 'C')
            self.ln(20)

        def footer(self):
            self.set_y(-15)
            self.set_font('Arial', 'I', 8)
            self.cell(0, 10, 'N° Pagina ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

def pdf__repre(datos):
    

    fecha_actual = datetime.now()
    nombre_archivo = fecha_actual.strftime("Representantes_%Y-%m-%d_%H-%M") + ".pdf"

    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Arial', "", 10)

    pdf.cell(w=12, h=15, txt='#', border=1, align='C', fill=0)
    pdf.cell(w=25, h=15, txt='C.I', border=1, align='C', fill=0)
    pdf.cell(w=37, h=15, txt='Nombres', border=1, align='C', fill=0)
    pdf.cell(w=37, h=15, txt='Apellidos', border=1, align='C', fill=0)
    pdf.cell(w=30, h=15, txt='Telefono', border=1, align='C', fill=0)
    pdf.multi_cell(w=0, h=15, txt='Dirección', border=1, align='C', fill=0)

    for i, dato in enumerate(datos, 1):
        ci, nombres, apellidos, telefono, direccion = dato
        pdf.cell(w=12, h=8, txt=str(i), border=1, align='C', fill=0)
        pdf.cell(w=25, h=8, txt=str(ci), border=1, align='C', fill=0)
        pdf.cell(w=37, h=8, txt=nombres, border=1, align='C', fill=0)
        pdf.cell(w=37, h=8, txt=apellidos, border=1, align='C', fill=0)
        pdf.cell(w=30, h=8, txt=telefono, border=1, align='C', fill=0)
        pdf.multi_cell(w=0, h=8, txt=direccion, border=1, align='C', fill=0)

    pdf.output(nombre_archivo, 'F')



def pdf__stud(datos):
    fecha_actual = datetime.now()
    nombre_archivo = fecha_actual.strftime("Estudiantes_%Y-%m-%d_%H-%M") + ".pdf"
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Arial', "", 10)

    pdf.cell(w=14, h=15, txt='#', border=1, align='C', fill=0)
    pdf.cell(w=45, h=15, txt='Nombres', border=1, align='C', fill=0)
    pdf.cell(w=45, h=15, txt='Apellidos', border=1, align='C', fill=0)
    pdf.cell(w=15, h=15, txt='Edad', border=1, align='C', fill=0)
    pdf.cell(w=35, h=15, txt='C.I', border=1, align='C', fill=0)
    pdf.cell(w=36, h=15, txt='C.I Representante', border=1, align='C', fill=0)
    pdf.ln()

    for i, dato in enumerate(datos, 1):
        pdf.cell(w=14, h=8, txt=str(i), border=1, align='C', fill=0)
        pdf.cell(w=45, h=8, txt=f"{dato[1]} {dato[2]}", border=1, align='C', fill=0)
        pdf.cell(w=45, h=8, txt=f"{dato[3]} {dato[4]}", border=1, align='C', fill=0)
        pdf.cell(w=15, h=8, txt=str(dato[5]), border=1, align='C', fill=0)
        pdf.cell(w=35, h=8, txt=dato[6], border=1, align='C', fill=0)
        pdf.multi_cell(w=0, h=8, txt=str(dato[7]), border=1, align='C', fill=0)


    pdf.output(nombre_archivo, 'F')