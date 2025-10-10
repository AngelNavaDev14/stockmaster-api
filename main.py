from fastapi import FastAPI
from app import models
from app.database import engine

# --- AÑADE ESTA LÍNEA ---
from app.routers import productos # Importamos nuestro nuevo router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="StockMaster API",
    description="API para la gestión de inventario y pedidos.",
    version="0.1.0"
)

# --- Y AÑADE ESTA OTRA LÍNEA ---
app.include_router(productos.router) # Conectamos las rutas de productos a la app principal

@app.get("/")
def read_root():
    """
    Endpoint de bienvenida.
    """
    return {"mensaje": "¡Bienvenido a la StockMaster API, Ángel!"}