    
# StockMaster API 📦

API RESTful para la gestión de un inventario de productos, construida con Python, FastAPI y PostgreSQL. Este proyecto está completamente contenerizado con Docker y desplegado en la nube a través de un pipeline de CI/CD.

**🚀 API en vivo disponible en:** [https://stockmaster-api-he73.onrender.com/docs](https://stockmaster-api-he73.onrender.com/docs)

*(Nota: Al ser un plan gratuito, el primer arranque puede tardar unos 30-50 segundos mientras el servicio "despierta")*

## ✨ Características

*   **CRUD completo** para la gestión de productos (Crear, Leer, Actualizar, Borrar).
*   **Documentación de API** interactiva y automática con Swagger UI y ReDoc.
*   **Base de datos relacional** conectada a través de un ORM (SQLAlchemy).
*   **Despliegue continuo**: Cada `git push` a la rama `main` dispara un nuevo despliegue automático en Render.

## 🛠️ Stack de Tecnologías

*   **Backend:** Python 3.11, FastAPI
*   **Base de Datos:** PostgreSQL
*   **ORM:** SQLAlchemy
*   **Validación de Datos:** Pydantic
*   **Contenerización:** Docker
*   **Plataforma de Despliegue (PaaS):** Render

## 🏁 Cómo ejecutarlo localmente

Para correr este proyecto en tu máquina, necesitas tener Git, Python 3.11+, Docker y PostgreSQL instalados.

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/AngelNavaDev14/stockmaster-api.git
    cd stockmaster-api
    ```
2.  **Crear y activar un entorno virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
3.  **Instalar las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configurar la base de datos local:**
    Asegúrate de tener una instancia de PostgreSQL corriendo y modifica la URL de conexión por defecto en el archivo `app/database.py` si es necesario.

5.  **Ejecutar el servidor:**
    ```bash
    uvicorn main:app --reload
    ```
    La API estará disponible en `http://127.0.0.1:8000`.

## 📄 Endpoints de la API

Todas las rutas están bajo el prefijo `/productos`.

| Método HTTP | Ruta                        | Descripción                       |
|-------------|-----------------------------|-----------------------------------|
| `POST`      | `/`                         | Crea un nuevo producto.           |
| `GET`       | `/`                         | Obtiene una lista de productos.   |
| `GET`       | `/{producto_id}`            | Obtiene un producto por su ID.    |
| `PUT`       | `/{producto_id}`            | Actualiza un producto por su ID.  |
| `DELETE`    | `/{producto_id}`            | Elimina un producto por su ID.    |

