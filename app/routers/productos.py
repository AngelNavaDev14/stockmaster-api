# <<< CÓDIGO CORREGIDO PARA app/routers/productos.py >>>

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import crud, schemas
from ..database import SessionLocal

router = APIRouter(
    prefix="/productos",
    tags=["Productos"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Producto)
def create_producto_endpoint(producto: schemas.ProductoCrear, db: Session = Depends(get_db)):
    return crud.create_producto(db=db, producto=producto)

@router.get("/", response_model=List[schemas.Producto])
def read_productos_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    productos = crud.get_productos(db, skip=skip, limit=limit)
    return productos

@router.get("/{producto_id}", response_model=schemas.Producto)
def read_producto_endpoint(producto_id: int, db: Session = Depends(get_db)):
    db_producto = crud.get_producto(db, producto_id=producto_id)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto

# --- ESTAS SON LAS FUNCIONES QUE PROBABLEMENTE ESTABAN MAL INDENTADAS ---
@router.put("/{producto_id}", response_model=schemas.Producto)
def update_producto_endpoint(producto_id: int, producto: schemas.ProductoCrear, db: Session = Depends(get_db)):
    db_producto = crud.update_producto(db=db, producto_id=producto_id, producto_update=producto)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto

@router.delete("/{producto_id}", response_model=schemas.Producto)
def delete_producto_endpoint(producto_id: int, db: Session = Depends(get_db)):
    db_producto = crud.delete_producto(db=db, producto_id=producto_id)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto