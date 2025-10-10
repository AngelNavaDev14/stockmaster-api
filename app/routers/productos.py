from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

# Importamos todo lo que hemos creado
from .. import crud, schemas
from ..database import SessionLocal, engine

# Creamos un "router". Es como una mini-aplicación de FastAPI.
router = APIRouter(
    prefix="/productos", # Todas las rutas aquí empezarán con /productos
    tags=["Productos"],    # Así se agruparán en la documentación
)

# --- DEPENDENCIA ---
# Esto es mágico. Cada vez que una ruta necesite la BD, esta función se ejecutará,
# abrirá una conexión, se la dará a la ruta, y se asegurará de cerrarla al final.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- ENDPOINT PARA CREAR UN PRODUCTO ---
@router.post("/", response_model=schemas.Producto)
def create_producto_endpoint(producto: schemas.ProductoCrear, db: Session = Depends(get_db)):
    # Aquí simplemente llamamos a la función que escribimos en crud.py
    return crud.create_producto(db=db, producto=producto)

# --- ENDPOINT PARA LEER UNA LISTA DE PRODUCTOS ---
@router.get("/", response_model=List[schemas.Producto])
def read_productos_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    productos = crud.get_productos(db, skip=skip, limit=limit)
    return productos

# --- ENDPOINT PARA LEER UN SOLO PRODUCTO POR SU ID ---
@router.get("/{producto_id}", response_model=schemas.Producto)
def read_producto_endpoint(producto_id: int, db: Session = Depends(get_db)):
    db_producto = crud.get_producto(db, producto_id=producto_id)
    if db_producto is None:
        # Si el producto no existe, devolvemos un error 404.
        raise HTTPException(status_code=404, detail="Producto no encontrado")
        @router.put("/{producto_id}", response_model=schemas.Producto)
def update_producto_endpoint(producto_id: int, producto: schemas.ProductoCrear, db: Session = Depends(get_db)):
    db_producto = crud.update_producto(db=db, producto_id=producto_id, producto_update=producto)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto

# --- ENDPOINT PARA BORRAR UN PRODUCTO ---
@router.delete("/{producto_id}", response_model=schemas.Producto)
def delete_producto_endpoint(producto_id: int, db: Session = Depends(get_db)):
    db_producto = crud.delete_producto(db=db, producto_id=producto_id)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto