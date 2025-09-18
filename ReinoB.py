import tkinter as tk
import os
import shutil
import subprocess
import platform
import ctypes
from PIL import Image
from PIL import ImageTk, ImageTk
#pip install pycryptodome
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from tkinter import ttk
import base64
import math
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

p=0
q=0

module=0

phi=0
e=0
d=0
message=""
messageChiper=0
messageDechiper=0
message_encrypted_b64 = ""
message_decrypted_str = ""
enc_str = ""

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_coprime(a: int, b: int) -> bool:
    return math.gcd(a, b) == 1


CONTROL_NAMES = {
    0: "NUL", 1: "SOH", 2: "STX", 3: "ETX", 4: "EOT", 5: "ENQ", 6: "ACK", 7: "BEL",
    8: "BS", 9: "HT", 10: "LF", 11: "VT", 12: "FF", 13: "CR", 14: "SO", 15: "SI",
    16: "DLE", 17: "DC1", 18: "DC2", 19: "DC3", 20: "DC4", 21: "NAK", 22: "SYN", 23: "ETB",
    24: "CAN", 25: "EM", 26: "SUB", 27: "ESC", 28: "FS", 29: "GS", 30: "RS", 31: "US",
    127: "DEL"
}

def bytes_to_visible(barr: bytes) -> str:
    parts = []
    for b in barr:
        if 0x20 <= b <= 0x7E:
            parts.append(chr(b))
        elif b in CONTROL_NAMES:
            parts.append(f"[{CONTROL_NAMES[b]}]")
        else:
            parts.append(f"[0x{b:02X}]")
    return "".join(parts)


def enc_message(msg: str) -> str:
    global e, module
    if module <= 1 or e <= 0:
        return ""
    data = str(msg).encode("utf-8")
    if module > 255:
        parts = [str(pow(b, e, module)) for b in data]
        return ",".join(parts)
    else:
        digits = []
        for b in data:
            hi = (b >> 6) & 0x3F
            lo = b & 0x3F
            digits.extend([hi, lo])
        enc_digits = [str(pow(dig, e, module)) for dig in digits]
        return ",".join(enc_digits)


def enc_messagae(msg: str) -> str:
    return enc_message(msg)

def deenc_message(cipher_str: str) -> str:
    global d, module
    if module <= 1 or d <= 0:
        return ""
    s = str(cipher_str)
    out = bytearray()
    tokens = [t for t in s.strip().split(",") if t]
    if module <= 255:
        nums = []
        for t in tokens:
            try:
                c = int(t)
                m = pow(c, d, module)
                nums.append(m)
            except Exception:
                continue
        for i in range(0, len(nums), 2):
            if i + 1 < len(nums):
                hi = nums[i] & 0x3F
                lo = nums[i + 1] & 0x3F
                b = (hi << 6) | lo
                out.append(b)
    else:
        for t in tokens:
            try:
                c = int(t)
                m = pow(c, d, module)
                out.append(m & 0xFF)
            except Exception:
                continue
    return bytes_to_visible(out)

def firstPanel(event=None):
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
    canvas2.tag_bind(btnContinue, "<Button-1>", ninthPanel)

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

    inpNumb1 = tk.Entry(root, width=22, font=("UnifrakturCook", 14))
    inpNumb1.focus()
    inpNumb2 = tk.Entry(root, width=22, font=("UnifrakturCook", 14))
    inpNumb2.focus()

    canvas2.create_window(702, 251, window=inpNumb1)
    canvas2.create_window(860, 300, window=inpNumb2)

    btnContinue = canvas2.create_text(
        1250, 630,
        text="Continuar...",
        font=("UnifrakturCook", 40, "bold"),
        fill="white"
    )

    def continuar(event=None):
        global p, q, module
        value1 = inpNumb1.get()
        value2 = inpNumb2.get()

        if value1 == "" or value2 == "":
            whiteException(tenthPanel)
            return

        if not value1.isdigit() or not value2.isdigit():
            notNumber(tenthPanel)
            return

        p = int(value1)
        q = int(value2)
        if not is_prime(p):
            notPrime(tenthPanel)
            return

        if not is_prime(q):
            notPrime(tenthPanel)
            return
        module = p * q
        eleventhPanel()

    canvas2.tag_bind(btnContinue, "<Button-1>", continuar)


def eleventhPanel(event=None):
    global module
    img = Image.open("eleventh.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")

    outNumb1 = tk.Entry(root, width=18, font=("UnifrakturCook", 14),justify="center" )
    outNumb1.insert(0, module)
    outNumb1.config(state="readonly")
    outNumb1.focus()
    canvas2.create_window(930, 240, window=outNumb1)


    btnContinue = canvas2.create_text(
        1250, 630,
        text="Continuar...",
        font=("UnifrakturCook", 40, "bold"),
        fill="white"
    )

    def continuar(event=None):

        twelfthPanel()


    canvas2.tag_bind(btnContinue, "<Button-1>", continuar)

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
    global p, q, phi
    img = Image.open("fourteenth.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")

    out1 = tk.Entry(root, width=20, font=("UnifrakturCook", 14),justify="center",bg="black" )
    phi=(p-1)*(q-1)
    value=phi
    out1.insert(0, value)
    out1.config(state="readonly",)
    out1.focus()
    canvas2.create_window(960, 293, window=out1)


    btnContinue = canvas2.create_text(
        1250, 630,
        text="Continuar...",
        font=("UnifrakturCook", 40, "bold"),
        fill="white"
    )

    def continuar(event=None):

        fifteenthPanel()


    canvas2.tag_bind(btnContinue, "<Button-1>", continuar)

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

    inpNumb1 = tk.Entry(root, width=18, font=("UnifrakturCook", 16))
    inpNumb1.focus()
    canvas2.create_window(950, 240, window=inpNumb1)


    btnContinue = canvas2.create_text(
        1250, 630,
        text="Continuar...",
        font=("UnifrakturCook", 40, "bold"),
        fill="white"
    )

    def continuar(event=None):
        global phi, e
        value1 = inpNumb1.get().strip()

        # Validaciones con retornos tempranos
        if value1 == "":
            whiteException(seventeenthPanel)
            return

        if not value1.isdigit():
            notNumber(seventeenthPanel)
            return

        n1 = int(value1)

        # 1) Rango básico RSA: 1 < e < phi(n)
        if n1 <= 1 or n1 >= phi:
            notCoPrime(seventeenthPanel)

            return

        # 2) Única condición requerida: gcd(e, phi) == 1
        if not is_coprime(n1, phi):
            notCoPrime(seventeenthPanel)
            return

        # Si todo ok, asigna e y avanza
        e = n1
        eighteenthPanel()

    canvas2.tag_bind(btnContinue, "<Button-1>", continuar)


def eighteenthPanel(event=None):
    global e,module
    img = Image.open("eighteenth.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")

    outTxt1 = tk.Entry(root, width=21, font=("UnifrakturCook", 14),justify="center")
    canvas2.create_window(960, 193, window=outTxt1)
    value=f"({e}, {module})"
    outTxt1.insert(0, value)
    outTxt1.config(state="readonly",)
    outTxt1.focus()

    btnContinue = canvas2.create_text(
        1250, 630,
        text="Continuar...",
        font=("UnifrakturCook", 40, "bold"),
        fill="white"
    )

    def continuar(event=None):

            nineteenthPanel()

    canvas2.tag_bind(btnContinue, "<Button-1>", continuar)



def nineteenthPanel(event=None):
    global module,phi
    img = Image.open("nineteenth.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")

    outTxt1 = tk.Entry(root, width=21, font=("UnifrakturCook", 10),justify="center")
    outTxt2 = tk.Entry(root, width=21, font=("UnifrakturCook", 10),justify="center")
    canvas2.create_window(870, 315, window=outTxt1)
    canvas2.create_window(916, 350, window=outTxt2)
    value=module
    value2=phi
    outTxt1.insert(0, value)
    outTxt1.config(state="readonly",)
    outTxt1.focus()
    outTxt2.insert(0, value2)
    outTxt2.config(state="readonly",)
    outTxt2.focus()

    btnContinue = canvas2.create_text(
        1250, 630,
        text="Continuar...",
        font=("UnifrakturCook", 40, "bold"),
        fill="white"
    )

    def continuar(event=None):

            twentiethPanel()

    canvas2.tag_bind(btnContinue, "<Button-1>", continuar)

def twentiethPanel(event=None):
    global e, phi, d, p, q
    img = Image.open("twentieth.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")

    outTxt1 = tk.Entry(root, width=20, font=("UnifrakturCook", 10),justify="center")
    outTxt2 = tk.Entry(root, width=20, font=("UnifrakturCook", 10),justify="center")
    outTxt3 = tk.Entry(root, width=14, font=("UnifrakturCook", 10),justify="center")
    canvas2.create_window(425, 150, window=outTxt1)
    canvas2.create_window(480, 217, window=outTxt2)
    canvas2.create_window(984, 250, window=outTxt3)
    d = pow(e, -1, phi)
    value3 = d
    outTxt1.insert(0, e)
    outTxt1.config(state="readonly",)
    outTxt1.focus()
    outTxt2.insert(0, phi)
    outTxt2.config(state="readonly",)
    outTxt2.focus()
    outTxt3.insert(0, value3)
    outTxt3.config(state="readonly",)
    outTxt3.focus()

    btnContinue = canvas2.create_text(
        1250, 630,
        text="Continuar...",
        font=("UnifrakturCook", 40, "bold"),
        fill="white"
    )

    def continuar(event=None):
        twentyfirstPanel()

    canvas2.tag_bind(btnContinue, "<Button-1>", continuar)


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

    outNumb1 = tk.Entry(root, width=21, font=("UnifrakturCook", 12),justify="center",bg="black" )
    outNumb2 = tk.Entry(root, width=21, font=("UnifrakturCook", 12),justify="center",bg="black" )
    outNumb3 = tk.Entry(root, width=21, font=("UnifrakturCook", 12),justify="center",bg="black" )
    outNumb4 = tk.Entry(root, width=21, font=("UnifrakturCook", 12),justify="center",bg="black" )
    global e, d, module, phi
    value = f"e = {e}"
    value2 = f"d = {d}"
    value3 = f"n = {module}"
    value4 = f"n = {module}"

    outNumb1.insert(0, value)
    outNumb1.config(state="readonly",)
    outNumb1.focus()
    outNumb2.insert(0, value2)
    outNumb2.config(state="readonly",)
    outNumb2.focus()
    outNumb3.insert(0, value3)
    outNumb3.config(state="readonly",)
    outNumb3.focus()
    outNumb4.insert(0, value4)
    outNumb4.config(state="readonly",)
    outNumb4.focus()
    canvas2.create_window(563, 385, window=outNumb1)
    canvas2.create_window(563, 500, window=outNumb2)
    canvas2.create_window(835, 385, window=outNumb3)
    canvas2.create_window(835, 500, window=outNumb4)

    btnContinue = canvas2.create_text(
        1250, 630,
        text="Continuar...",
        font=("UnifrakturCook", 40, "bold"),
        fill="white"
    )

    def continuar(event=None):

        twentythirdPanel()


    canvas2.tag_bind(btnContinue, "<Button-1>", continuar)

def twentythirdPanel(event=None):
    global message
    img = Image.open("twentythird.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")

    inpTxt1 = tk.Entry(root, width=19, font=("UnifrakturCook", 10))
    inpTxt1.focus()
    canvas2.create_window(1030, 337, window=inpTxt1)

    btnContinue = canvas2.create_text(
        1250, 630,
        text="Continuar...",
        font=("UnifrakturCook", 40, "bold"),
        fill="white"
    )

    def continuar(event=None):
        global message
        value1 = inpTxt1.get()
        if value1 == "":
            whiteException(twentythirdPanel)
            return
        message = value1
        twentyfourthPanel()

    canvas2.tag_bind(btnContinue, "<Button-1>", continuar)

def twentyfourthPanel(event=None):
    img = Image.open("twentyfourth.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")

    outNumb1 = tk.Entry(root, width=21, font=("UnifrakturCook", 12), justify="center", bg="white")
    outNumb2 = tk.Entry(root, width=21, font=("UnifrakturCook", 12), justify="center", bg="white" )

    global e, d, module, phi
    value = e
    value2 = d
    value3 = module
    value4 = phi

    outNumb1.insert(0, "("+str(value)+","+str(value3)+")")
    outNumb1.config(state="readonly")
    outNumb1.focus()
    outNumb2.insert(0, "("+str(value2)+","+str(value3)+")")
    outNumb2.config(state="readonly")
    outNumb2.focus()

    canvas2.create_window(695, 345, window=outNumb1)
    canvas2.create_window(695, 458, window=outNumb2)

    btnContinue = canvas2.create_text(
        1250, 630,
        text="Continuar...",
        font=("UnifrakturCook", 40, "bold"),
        fill="white"
    )

    def continuar(event=None):
        twentyfifthPanel()

    canvas2.tag_bind(btnContinue, "<Button-1>", continuar)

def twentyfifthPanel(event=None):
    img = Image.open("twentyfifth.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")

    outNumb1 = tk.Entry(root, width=18, font=("UnifrakturCook", 12), justify="center", bg="black")

    global d, e, module, messageChiper, messageDechiper, message_decrypted_str

    value = e
    value2 = module

    outNumb1.insert(0, "("+str(value)+","+str(value2)+")")
    outNumb1.config(state="readonly")
    outNumb1.focus()

    canvas2.create_window(950, 171, window=outNumb1)


    btnContinue = canvas2.create_text(
        1250, 630,
        text="Continuar...",
        font=("UnifrakturCook", 40, "bold"),
        fill="white"
    )

    def continuar(event=None):
        twentysixthPanel()

    canvas2.tag_bind(btnContinue, "<Button-1>", continuar)


def twentysixthPanel(event=None):
    global message_encrypted_b64, message_decrypted_str
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
    canvas2.tag_bind(btnContinue, "<Button-1>", twentyeighthPanel)


def twentyeighthPanel(event=None):
    img = Image.open("twentyeighth.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")
    btnContinue = canvas2.create_text(1250, 630, text="Continuar...", font=("UnifrakturCook", 40, "bold"), fill="white")
    canvas2.tag_bind(btnContinue, "<Button-1>", twentyninthPanel)

def twentyninthPanel(event=None):
    img = Image.open("twentyninth.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")
    btnContinue = canvas2.create_text(1250, 630, text="Continuar...", font=("UnifrakturCook", 40, "bold"), fill="white")
    canvas2.tag_bind(btnContinue, "<Button-1>", thirtiethPanel)

def thirtiethPanel(event=None):
    global message, e, module, d, enc_str
    img = Image.open("thirtieth.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")

    outEnc = tk.Entry(root, width=40, font=("UnifrakturCook", 14), justify="center")


    canvas2.create_window(700, 190, window=outEnc)


    if module <= 1 or e <= 0 or d <= 0:
        enc_str = ""
    else:
        enc_str = enc_message(message)

    outEnc.insert(0, enc_str)
    outEnc.config(state="readonly")
    outEnc.focus()


    btnContinue = canvas2.create_text(
        1250, 630,
        text="Continuar...",
        font=("UnifrakturCook", 40, "bold"),
        fill="white"
    )

    def continuar(event=None):

            thirtyfirstPanel()

    canvas2.tag_bind(btnContinue, "<Button-1>", continuar)

def thirtyfirstPanel(event=None):
    img = Image.open("thirtyfirst.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")

    outTxt1 = tk.Entry(root, width=22, font=("UnifrakturCook", 14),justify="center")
    outTxt2 = tk.Entry(root, width=22, font=("UnifrakturCook", 14),justify="center")


    canvas2.create_window(760, 309, window=outTxt1)
    canvas2.create_window(690, 405, window=outTxt2)

    global e, d, module, phi, enc_str
    value = e
    value2 = d
    value3 = module
    value4 = phi

    outTxt1.insert(0, "("+str(value2)+","+str(value3)+")")
    outTxt2.insert(0, str(enc_str))

    outTxt1.config(state="readonly",)
    outTxt2.config(state="readonly",)
    outTxt1.focus()
    outTxt2.focus()

    btnContinue = canvas2.create_text(
        1250, 630,
        text="Continuar...",
        font=("UnifrakturCook", 40, "bold"),
        fill="white"
    )

    def continuar(event=None):

            thirtysecondPanel()

    canvas2.tag_bind(btnContinue, "<Button-1>", continuar)

def thirtysecondPanel(event=None):
    img = Image.open("thirtysecond.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")

    outTxt1 = tk.Entry(root, width=16, font=("UnifrakturCook", 14),justify="center")
    outTxt2 = tk.Entry(root, width=16, font=("UnifrakturCook", 14),justify="center")

    canvas2.create_window(1016, 328, window=outTxt1)
    canvas2.create_window(1018, 505, window=outTxt2)

    global e, d, module, phi, enc_str
    value = e
    value2 = d
    value3 = module
    value4 = phi

    outTxt1.insert(0, "(" + str(value2) + "," + str(value3) + ")")
    outTxt2.insert(0, str(deenc_message(enc_str)))

    outTxt1.config(state="readonly",)
    outTxt2.config(state="readonly",)
    outTxt1.focus()
    outTxt2.focus()

    btnContinue = canvas2.create_text(
        1250, 630,
        text="Continuar...",
        font=("UnifrakturCook", 40, "bold"),
        fill="white"
    )

    def continuar(event=None):

            thirtythirdPanel()

    canvas2.tag_bind(btnContinue, "<Button-1>", continuar)

def thirtythirdPanel(event=None):
    img = Image.open("thirtythird.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")
    btnContinue = canvas2.create_text(700, 630, text="Bibliografia", font=("UnifrakturCook", 40, "bold"), fill="white")
    def continuar(event=None):

        export_to_pdf()

    canvas2.tag_bind(btnContinue, "<Button-1>", continuar)





    #Excepciones

def notCoPrime (panel):
    img = Image.open("notcoprime.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")
    btnContinue = canvas2.create_text(1250, 630, text="Continuar...", font=("UnifrakturCook", 40, "bold"), fill="white")
    canvas2.tag_bind(btnContinue, "<Button-1>", panel)

def notNumber (panel):
    img = Image.open("notnumber.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")
    btnContinue = canvas2.create_text(1250, 630, text="Continuar...", font=("UnifrakturCook", 40, "bold"), fill="white")
    canvas2.tag_bind(btnContinue, "<Button-1>", panel)

def notPrime (panel):
    img = Image.open("notprime.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")
    btnContinue = canvas2.create_text(1250, 630, text="Continuar...", font=("UnifrakturCook", 40, "bold"), fill="white")
    canvas2.tag_bind(btnContinue, "<Button-1>", panel)

def whiteException(panel):
    img = Image.open("notwritten.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")
    btnContinue = canvas2.create_text(1250, 630, text="Continuar...", font=("UnifrakturCook", 40, "bold"), fill="white")
    canvas2.tag_bind(btnContinue, "<Button-1>", panel)

btn = canvas.create_text(700, 300, text="Iniciar", font=("UnifrakturCook", 40, "bold"), fill="white")
canvas.tag_bind(btn, "<Button-1>", firstPanel)

btn = canvas.create_text(700, 500, text="Salir", font=("UnifrakturCook", 40, "bold"), fill="white")
canvas.tag_bind(btn, "<Button-1>", exit)



root.mainloop()

def exit():
    root.destroy()

def encrypt(msj: str) -> str:
    encryption = cipher_rsa.encrypt(msj.encode("utf-8"))
    return base64.b64encode(encryption).decode("utf-8")

def dechiper(encryption_b64: str) -> str:
    encryption = base64.b64decode(encryption_b64)
    decryptor = decipher_rsa.decrypt(encryption)
    return decryptor.decode("utf-8")

def export_to_pdf():
    doc = SimpleDocTemplate("Referencias.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    story = []


    styles.add(ParagraphStyle(name='Justificado', alignment=TA_JUSTIFY))


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


    for line in references_text.strip().split('\n'):
        if line.strip():
            if "##" in line:

                story.append(Paragraph(line.replace("##", "").strip(), styles['Centrado']))
            else:

                story.append(Paragraph(line.strip(), styles['Justificado']))

    try:
        doc.build(story)
    except Exception as e:
        print(f"Error al exportar el PDF: {e}")


def install_font(font_path):
    font_path = os.path.abspath(os.path.expanduser(font_path))
    system = platform.system()
    if system == "Windows":
        fonts_dir = os.path.join(os.environ["WINDIR"], "Fonts")
        dest = os.path.join(fonts_dir, os.path.basename(font_path))
        shutil.copy(font_path, dest)
        FR_PRIVATE = 0x10
        ctypes.windll.gdi32.AddFontResourceExW(dest, FR_PRIVATE, 0)
        ctypes.windll.user32.SendMessageW(0xFFFF, 0x001D, 0, 0)
    elif system == "Darwin":
        fonts_dir = os.path.expanduser("~/Library/Fonts")
        os.makedirs(fonts_dir, exist_ok=True)
        dest = os.path.join(fonts_dir, os.path.basename(font_path))
        shutil.copy(font_path, dest)
    else:
        fonts_dir = os.path.expanduser("~/.local/share/fonts")
        os.makedirs(fonts_dir, exist_ok=True)
        dest = os.path.join(fonts_dir, os.path.basename(font_path))
        shutil.copy(font_path, dest)
        fc = shutil.which("fc-cache")
        if fc:
            subprocess.run([fc, "-f", "-v"], check=False)

install_font("UnifrakturCook-Bold.ttf")