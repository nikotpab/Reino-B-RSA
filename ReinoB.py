import tkinter as tk

from PIL import Image
from PIL import ImageTk, ImageTk
#pip install pycryptodome
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from tkinter import ttk
import base64
##pip install reportlab
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER

root = tk.Tk()

root.title("Reino B RSA")
root.resizable(False, False)
root.minsize(1400, 700)

img = Image.open("main.png")
img = img.resize((1400,800))
img = ImageTk.PhotoImage(img)

canvas = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
canvas.place(x=0, y=0)
canvas.bg = img
canvas.create_image(0, 0, image=img, anchor="nw")

def fistPanel(event=None):
    img = Image.open("first.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")
    btnContinue = canvas2.create_text(1250, 630, text="Continuar...", font=("UnifrakturCook", 40, "bold"), fill="white")
    canvas2.tag_bind(btnContinue, "<Button-1>", secondPanel)

def secondPanel(event=None):
    img = Image.open("second.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")
    btnContinue = canvas2.create_text(1250, 630, text="Continuar...", font=("UnifrakturCook", 40, "bold"), fill="white")
    canvas2.tag_bind(btnContinue, "<Button-1>", thirdPanel)

def thirdPanel(event=None):
    img = Image.open("third.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")
    btnContinue = canvas2.create_text(1250, 630, text="Continuar...", font=("UnifrakturCook", 40, "bold"), fill="white")
    canvas2.tag_bind(btnContinue, "<Button-1>", fourthPanel)

def fourthPanel(event=None):
    img = Image.open("fourth.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")
    btnContinue = canvas2.create_text(1250, 630, text="Continuar...", font=("UnifrakturCook", 40, "bold"), fill="white")
    canvas2.tag_bind(btnContinue, "<Button-1>", fifthPanel)

def fifthPanel(event=None):
    img = Image.open("fifth.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")
    btnContinue = canvas2.create_text(1250, 630, text="Continuar...", font=("UnifrakturCook", 40, "bold"), fill="white")
    canvas2.tag_bind(btnContinue, "<Button-1>", sixthPanel)

def sixthPanel(event=None):
    img = Image.open("sixth.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")
    btnContinue = canvas2.create_text(1250, 630, text="Continuar...", font=("UnifrakturCook", 40, "bold"), fill="white")
    canvas2.tag_bind(btnContinue, "<Button-1>", seventhPanel)

def seventhPanel(event=None):
    img = Image.open("seventh.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")
    btnContinue = canvas2.create_text(1250, 630, text="Continuar...", font=("UnifrakturCook", 40, "bold"), fill="white")
    canvas2.tag_bind(btnContinue, "<Button-1>", eighthPanel)

def eighthPanel(event=None):
    img = Image.open("eighth.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")
    btnContinue = canvas2.create_text(1250, 630, text="Continuar...", font=("UnifrakturCook", 40, "bold"), fill="white")
    canvas2.tag_bind(btnContinue, "<Button-1>",ninthPanel)

def ninthPanel(event=None):
    img = Image.open("ninth.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")
    btnContinue = canvas2.create_text(1250, 630, text="Continuar...", font=("UnifrakturCook", 40, "bold"), fill="white")
    canvas2.tag_bind(btnContinue, "<Button-1>",tenthPanel)

def tenthPanel(event=None):
    img = Image.open("tenth.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")
    btnContinue = canvas2.create_text(1250, 630, text="Continuar...", font=("UnifrakturCook", 40, "bold"), fill="white")
    canvas2.tag_bind(btnContinue, "<Button-1>", eleventhPanel)

def eleventhPanel(event=None):
    img = Image.open("eleventh.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")
    btnContinue = canvas2.create_text(1250, 630, text="Continuar...", font=("UnifrakturCook", 40, "bold"), fill="white")
    canvas2.tag_bind(btnContinue, "<Button-1>", twelfthPanel)

def twelfthPanel(event=None):
    img = Image.open("twelfth.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")
    btnContinue = canvas2.create_text(1250, 630, text="Continuar...", font=("UnifrakturCook", 40, "bold"), fill="white")
    canvas2.tag_bind(btnContinue, "<Button-1>", thirteenthPanel)

def thirteenthPanel(event=None):
    img = Image.open("thirteenth.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")
    btnContinue = canvas2.create_text(1250, 630, text="Continuar...", font=("UnifrakturCook", 40, "bold"), fill="white")
    canvas2.tag_bind(btnContinue, "<Button-1>",fourteenthPanel)

def fourteenthPanel(event=None):
    img = Image.open("fourteenth.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")
    btnContinue = canvas2.create_text(1250, 630, text="Continuar...", font=("UnifrakturCook", 40, "bold"), fill="white")
    canvas2.tag_bind(btnContinue, "<Button-1>", fifteenthPanel)

def fifteenthPanel(event=None):
    img = Image.open("fifteenth.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")
    btnContinue = canvas2.create_text(1250, 630, text="Continuar...", font=("UnifrakturCook", 40, "bold"), fill="white")
    canvas2.tag_bind(btnContinue, "<Button-1>", sixteenthPanel)

def sixteenthPanel(event=None):
    img = Image.open("sixteenth.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")
    btnContinue = canvas2.create_text(1250, 630, text="Continuar...", font=("UnifrakturCook", 40, "bold"), fill="white")
    canvas2.tag_bind(btnContinue, "<Button-1>", seventeenthPanel)

def seventeenthPanel(event=None):
    img = Image.open("seventeenth.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")
    btnContinue = canvas2.create_text(1250, 630, text="Continuar...", font=("UnifrakturCook", 40, "bold"), fill="white")
    canvas2.tag_bind(btnContinue, "<Button-1>", eighteenthPanel)

def eighteenthPanel(event=None):
    img = Image.open("eighteenth.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")
    btnContinue = canvas2.create_text(1250, 630, text="Continuar...", font=("UnifrakturCook", 40, "bold"), fill="white")
    canvas2.tag_bind(btnContinue, "<Button-1>", nineteenthPanel)

def nineteenthPanel(event=None):
    img = Image.open("nineteenth.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")
    btnContinue = canvas2.create_text(1250, 630, text="Continuar...", font=("UnifrakturCook", 40, "bold"), fill="white")
    canvas2.tag_bind(btnContinue, "<Button-1>",twentiethPanel)
def nineteenthPanel(event=None):
    img = Image.open("nineteenth.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")
    btnContinue = canvas2.create_text(1250, 630, text="Continuar...", font=("UnifrakturCook", 40, "bold"), fill="white")
    canvas2.tag_bind(btnContinue, "<Button-1>", twentiethPanel)


def twentiethPanel(event=None):
    img = Image.open("twentieth.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")
    btnContinue = canvas2.create_text(1250, 630, text="Continuar...", font=("UnifrakturCook", 40, "bold"), fill="white")
    canvas2.tag_bind(btnContinue, "<Button-1>", twentyfirstPanel)


def twentyfirstPanel(event=None):
    img = Image.open("twentyfirst.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")
    btnContinue = canvas2.create_text(1250, 630, text="Continuar...", font=("UnifrakturCook", 40, "bold"), fill="white")
    canvas2.tag_bind(btnContinue, "<Button-1>", twentysecondPanel)


def twentysecondPanel(event=None):
    img = Image.open("twentysecond.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")
    btnContinue = canvas2.create_text(1250, 630, text="Continuar...", font=("UnifrakturCook", 40, "bold"), fill="white")
    canvas2.tag_bind(btnContinue, "<Button-1>", twentythirdPanel)


def twentythirdPanel(event=None):
    img = Image.open("twentythird.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")
    btnContinue = canvas2.create_text(1250, 630, text="Continuar...", font=("UnifrakturCook", 40, "bold"), fill="white")
    canvas2.tag_bind(btnContinue, "<Button-1>", twentyfourthPanel)


def twentyfourthPanel(event=None):
    img = Image.open("twentyfourth.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")
    btnContinue = canvas2.create_text(1250, 630, text="Continuar...", font=("UnifrakturCook", 40, "bold"), fill="white")
    canvas2.tag_bind(btnContinue, "<Button-1>", twentyfifthPanel)


def twentyfifthPanel(event=None):
    img = Image.open("twentyfifth.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")
    btnContinue = canvas2.create_text(1250, 630, text="Continuar...", font=("UnifrakturCook", 40, "bold"), fill="white")
    canvas2.tag_bind(btnContinue, "<Button-1>", twentysixthPanel)


def twentysixthPanel(event=None):
    img = Image.open("twentysixth.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")
    btnContinue = canvas2.create_text(1250, 630, text="Continuar...", font=("UnifrakturCook", 40, "bold"), fill="white")
    canvas2.tag_bind(btnContinue, "<Button-1>", twentyseventhPanel)


def twentyseventhPanel(event=None):
    img = Image.open("twentyseventh.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")
    btnContinue = canvas2.create_text(1250, 630, text="Continuar...", font=("UnifrakturCook", 40, "bold"), fill="white")
    canvas2.tag_bind(btnContinue, "<Button-1>", notCoPrime)

def notCoPrime (event = None):
    img = Image.open("notcoprime.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")
    btnContinue = canvas2.create_text(1250, 630, text="Continuar...", font=("UnifrakturCook", 40, "bold"), fill="white")
    canvas2.tag_bind(btnContinue, "<Button-1>", notNumber)

def notNumber (event = None):
    img = Image.open("notnumber.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")
    btnContinue = canvas2.create_text(1250, 630, text="Continuar...", font=("UnifrakturCook", 40, "bold"), fill="white")
    canvas2.tag_bind(btnContinue, "<Button-1>", notPrime)

def notPrime (event = None):
    img = Image.open("notprime.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")
    btnContinue = canvas2.create_text(1250, 630, text="Continuar...", font=("UnifrakturCook", 40, "bold"), fill="white")
    canvas2.tag_bind(btnContinue, "<Button-1>", lambda e: print("No es un numero primo"))

btn = canvas.create_text(700, 300, text="Iniciar", font=("UnifrakturCook", 40, "bold"), fill="white")
canvas.tag_bind(btn, "<Button-1>", fistPanel)



root.mainloop()


def encrypt(msj: str) -> str:
    encryption = cipher_rsa.encrypt(msj.encode("utf-8"))
    return base64.b64encode(encryption).decode("utf-8")

def dechiper(encryption_b64: str) -> str:
    encryption = base64.b64decode(encryption_b64)
    decryptor = decipher_rsa.decrypt(encryption)
    return decryptor.decode("utf-8")





############################################
#Funcion para exportar referencias en pdf
def export_to_pdf():
    doc = SimpleDocTemplate("Referencias.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Define un estilo para texto justificado
    styles.add(ParagraphStyle(name='Justificado', alignment=TA_JUSTIFY))

    # Define un estilo para el título centrado
    styles.add(ParagraphStyle(name='Centrado', alignment=TA_CENTER, fontName='Helvetica-Bold', fontSize=14))

    references_text = """
    ## Referencias

    [1] Stack Overflow, Transparent backgrounds on buttons in Tkinter, 2015. [En línea]. Disponible en: https://stackoverflow.com/questions/29857757/transparent-backgrounds-on-buttons-in-tkinter. [Accedido: 14-sept-2025].

    [2] Shutterstock, Devil cartoon - imágenes y vectores, 2025. [En línea]. Disponible en: https://www.shutterstock.com/es/search/devil-cartoon?dd_referrer=https%3A%2F%2Fwww.google.com%2F. [Accedido: 14-sept-2025].

    [3] Wallpapers.com, Kingdom background wallpapers, 2025. [En línea]. Disponible en: https://wallpapers.com/kingdom-background. [Accedido: 14-sept-2025].

    [4] AskPython, RSA Algorithm in Python (example), 2025. [En línea]. Disponible en: https://www-askpython-com.translate.goog/python/examples/rsa-algorithm-in-python?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc. [Accedido: 14-sept-2025].

    [5] Python GUIs, Create GUI with Tkinter (tutorial), 2025. [En línea]. Disponible en: https://www-pythonguis-com.translate.goog/tutorials/create-gui-tkinter/?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc. [Accedido: 14-sept-2025].

    [6] Google Fonts, UnifrakturCook, 2025. [En línea]. Disponible en: https://fonts.google.com/specimen/UnifrakturCook. [Accedido: 14-sept-2025].

    [7] Real Python, Create and Modify PDF Files in Python, 19-ene-2025. [En línea]. Disponible en: https://realpython.com/creating-modifying-pdf/ [Accedido: 14-sept-2025].
    """

    # Procesa cada línea del texto
    for line in references_text.strip().split('\n'):
        if line.strip():  # Ignora líneas en blanco
            if "##" in line:
                # Usa el estilo centrado para el título
                story.append(Paragraph(line.replace("##", "").strip(), styles['Centrado']))
            else:
                # Usa el estilo justificado para el resto del texto
                story.append(Paragraph(line.strip(), styles['Justificado']))

    try:
        doc.build(story)
        print("PDF exportado exitosamente con formato mejorado!")
    except Exception as e:
        print(f"Error al exportar el PDF: {e}")


# Llama a la función para ejecutarla
export_to_pdf()
