# StockMaster API 📦

API RESTful para la gestión de un inventario de productos, construida con Python, FastAPI y PostgreSQL. Este proyecto está completamente contenerizado con Docker y desplegado en la nube a través de un pipeline de CI/CD.

**🚀 API en vivo disponible en:** [https://stockmaster-api-he73.onrender.com/docs](https://stockmaster-api-he73.onrender.com/docs)

*(Nota: Al ser un plan gratuito, el primer arranque puede tardar unos 30-50 segundos mientras el servicio "despierta")*

## ✨ Características
*   **CRUD completo** para la gestión de productos (Crear, Leer, Actualizar, Borrar).
*   **Documentación de API** interactiva y automática con Swagger UI.
*   **Base de datos relacional** conectada a través de un ORM (SQLAlchemy).
*   **Despliegue Continuo (CI/CD):**
    *   Un pipeline de **GitHub Actions** construye y sube automáticamente la imagen de Docker a Docker Hub en cada `push` a `main`.
    *   El servicio en **Render** se actualiza automáticamente al detectar una nueva imagen.
*   **Diseñado para Orquestación:** La configuración de la base de datos es flexible, permitiendo su despliegue en entornos como **Kubernetes** mediante variables de entorno (ver [stockmaster-k8s-config](https://github.com/AngelNavaDev14/stockmaster-k8s-config)).

## 🛠️ Stack de Tecnologías
*   **Backend:** Python 3.11, FastAPI
*   **Base de Datos:** PostgreSQL
*   **ORM:** SQLAlchemy
*   **Validación de Datos:** Pydantic
*   **Contenerización:** Docker
*   **CI/CD:** GitHub Actions
*   **Plataforma de Despliegue (PaaS):** Render

## 🏁 Cómo ejecutarlo localmente
1.  Clonar el repositorio.
2.  Crear y activar un entorno virtual e instalar dependencias.
3.  Asegurarse de tener una instancia de PostgreSQL corriendo localmente.
4.  Ejecutar el servidor con `uvicorn main:app --reload`.
