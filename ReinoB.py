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

def twentiethPanel(event=None):
    img = Image.open("twentieth.png")
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
    value4 = f"φ(n) = {phi}"
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
        value1 = inpTxt1.get()
        message=value1

    #Aqui esta para que ponga la logica para el cifrado
        if value1 == "" :
            print("Campos vacios")
            whiteException(twentythirdPanel)
        else:
            #Mas exactamente aqui
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

    outNumb1 = tk.Entry(root, width=21, font=("UnifrakturCook", 12),justify="center",bg="black" )
    outNumb2 = tk.Entry(root, width=21, font=("UnifrakturCook", 12),justify="center",bg="black" )
    global message, module, e, messageChiper
    try:
        m = int(message)
    except:
        m = int.from_bytes(message.encode("utf-8"), "big") % module
    c = pow(m, e, module)
    messageChiper = c
    value = f"m = {m}"
    value2 = f"c = {c}"
    outNumb1.insert(0, value)
    outNumb1.config(state="readonly")
    outNumb1.focus()
    outNumb2.insert(0, value2)
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

    outNumb1 = tk.Entry(root, width=18, font=("UnifrakturCook", 12),justify="center",bg="black" )
    global d, module, messageChiper, messageDechiper
    m2 = pow(messageChiper, d, module)
    messageDechiper = m2
    value = f"m' = {m2}"
    outNumb1.insert(0, value)
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
    global messageDechiper
    img = Image.open("thirtieth.png")
    img = img.resize((1400, 800))
    img = ImageTk.PhotoImage(img)

    canvas2 = tk.Canvas(root, width=1400, height=800, highlightthickness=0, bd=0)
    canvas2.place(x=0, y=0)
    canvas2.bg = img
    canvas2.create_image(0, 0, image=img, anchor="nw")

    outTxt1 = tk.Entry(root, width=21, font=("UnifrakturCook", 14),justify="center")
    
    canvas2.create_window(650, 193, window=outTxt1)  
     
    value="m"

    outTxt1.insert(0, value)
    outTxt1.config(state="readonly",)

    

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

    outTxt1 = tk.Entry(root, width=25, font=("UnifrakturCook", 14),justify="center")
    outTxt2 = tk.Entry(root, width=25, font=("UnifrakturCook", 14),justify="center")
    outTxt3 = tk.Entry(root, width=25, font=("UnifrakturCook", 14),justify="center")


    canvas2.create_window(800, 320, window=outTxt1)  
    canvas2.create_window(780, 425, window=outTxt2)  
    canvas2.create_window(800, 530, window=outTxt3)  


    value="(4,5)"
    value2=0
    value3=0
 
    outTxt1.insert(0, value)
    outTxt1.config(state="readonly",)

    outTxt2.insert(0, value2)
    outTxt2.config(state="readonly",)

    outTxt2.insert(0, value3)
    outTxt3.config(state="readonly",)

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
 
    value="(4,5)"
    value2=0
    value3=0
 
    outTxt1.insert(0, value)
    outTxt1.config(state="readonly",)

    outTxt2.insert(0, value)
    outTxt2.config(state="readonly",)

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
    btnContinue = canvas2.create_text(1250, 630, text="Finalizar", font=("UnifrakturCook", 40, "bold"), fill="white")
    canvas2.tag_bind(btnContinue, "<Button-1>", firstPanel)

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
canvas.tag_bind(btn, "<Button-1>", fistPanel)



root.mainloop()


def encrypt(msj: str) -> str:
    encryption = cipher_rsa.encrypt(msj.encode("utf-8"))
    return base64.b64encode(encryption).decode("utf-8")

def dechiper(encryption_b64: str) -> str:
    encryption = base64.b64decode(encryption_b64)
    decryptor = decipher_rsa.decrypt(encryption)
    return decryptor.decode("utf-8")
