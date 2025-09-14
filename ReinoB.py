import tkinter as tk

from PIL import Image
from PIL import ImageTk, ImageTk
#pip install pycryptodome
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from tkinter import ttk
import base64


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
    canvas2.tag_bind(btnContinue, "<Button-1>", lambda e: print("Iniciar presionado"))



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
