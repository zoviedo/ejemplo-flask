# 🐍 HOSTING Template: Aplicación Web con Flask (Python)

Este repositorio contiene el código base para una aplicación web dinámica construida con el framework **Flask** de Python, optimizada para el despliegue en la plataforma de Hosting.

Este template está configurado para ejecutarse en un contenedor **Python con Gunicorn** y exponer la aplicación a través del **Puerto 80**.

---

## 🚀 Cómo Empezar

Sigue estos pasos para adaptar este template y desplegarlo en la plataforma de Hosting:

1.  **Clonar el Template:** Clona este repositorio a tu cuenta personal de GitHub.
2.  **Modificar el Código:**
    * Trabaja en el archivo **`app.py`** para definir la lógica de tu aplicación y las rutas de API.
    * Modifica el archivo **`static/style.css`** para cambiar el diseño.
    * Modifica los archivos en la carpeta **`templates/`** para cambiar la interfaz de usuario.
3.  **Dependencias:** Si tu proyecto requiere librerías adicionales de Python (más allá de Flask), añádelas al archivo **`requirements.txt`**.
4.  **Registro en la plataforma de Hosting:**
    * Una vez que tu código esté listo en tu repositorio personal, copia la URL de dicho repositorio.
    * Regístrala en la interfaz de la plataforma de Hosting (Selecciona "Flask" como template).
5.  **Despliegue:** La plataforma automáticamente construirá el contenedor Python y te proporcionará una URL local para acceder a tu aplicación.

---

## 📁 Estructura del Template

| Archivo/Directorio | Descripción | **¿Editable por el Usuario?** |
| :--- | :--- | :--- |
| `app.py` | **Punto de entrada de la aplicación.** Contiene la lógica y las rutas de Flask. | ✅ SÍ |
| `requirements.txt` | Lista de dependencias de Python. | ✅ SÍ |
| `templates/` | Contiene los archivos HTML (Jinja2) que son renderizados por Flask. | ✅ SÍ |
| `static/` | **Carpeta estándar de Flask** para archivos estáticos (CSS, JS, imágenes). | ✅ SÍ |
| **`static/style.css`** | **Archivo de estilos CSS.** Utilizado por la plantilla `index.html`. | ✅ SÍ |
| **`Dockerfile`** | **Instrucciones para Docker:** Configura el entorno Python (con Gunicorn) y el Puerto 80. | ❌ **NO** |

---

## ⚠️ NOTA IMPORTANTE PARA EL DESPLIEGUE

**Por favor, no modifiques el archivo `Dockerfile`** en la raíz de este repositorio. Este archivo contiene la configuración crítica necesaria para que el **Project Manager Service** de la plataforma pueda construir y ejecutar tu contenedor correctamente.