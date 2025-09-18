import tkinter as tk
#pip install pycryptodome
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


root = tk.Tk()

root.title("Reino B RSA")
root.resizable(False, False)
root.minsize(1400, 700)

root.mainloop()


def cifrar_texto(mensaje: str) -> str:
    cifrado = cipher_rsa.encrypt(mensaje.encode("utf-8"))
    return base64.b64encode(cifrado).decode("utf-8")  

def descifrar_texto(cifrado_b64: str) -> str:
    cifrado = base64.b64decode(cifrado_b64)
    descifrado = decipher_rsa.decrypt(cifrado)
    return descifrado.decode("utf-8")