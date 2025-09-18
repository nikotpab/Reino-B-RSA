## 📚 Descripción

Aplicación **Tkinter** que explica paso a paso el cifrado RSA mediante pantallas ilustradas. Permite elegir primos \(p\) y \(q\), construir las claves, escribir un mensaje y ver su **cifrado** y **descifrado** en tiempo real. Está pensada con fines **didáctico-educativos** (no para uso criptográfico real).

---

## 👥 Integrantes del grupo

Nicolas Barbosa
Juan Pablo Cuervo
Juan Camilo Beltrán
Miguel Ángel Alza


---

## 📁 Estructura mínima del proyecto

Reino-B-RSA/
├─ ReinoB.py
├─ UnifrakturCook-Bold.ttf
├─ main.png  first.png  second.png … thirtysecond.png
└─ otros .png usados por los paneles y excepciones

---

## 🧰 Requisitos

- **Python 3.10+** (recomendado 3.11 o 3.12)  
- **Tkinter** (viene con Python en Windows/macOS; en Linux puede requerir instalación adicional)  
- Acceso de escritura al directorio de **fuentes** del sistema (el programa instala la fuente *UnifrakturCook* en el primer arranque).  

---

## 📦 Instalación rápida

### 1) Crear y activar entorno virtual

**Windows (PowerShell):**
powershell
python -m venv .venv
.venv\Scripts\Activate.ps1

**MacOS/Linux:**
python3 -m venv .venv
source .venv/bin/activate

# Librerías externas (instalación con pip)

pip install pillow        # Manejo de imágenes (PIL)
pip install pycryptodome  # Algoritmos criptográficos como RSA
pip install reportlab     # Crear y modificar PDFs

# Dependencias adicionales (solo en Linux, si hace falta)
sudo apt-get install -y python3-tk fontconfig



