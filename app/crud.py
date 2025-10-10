from sqlalchemy.orm import Session
from . import models, schemas

# --- FUNCIÓN PARA LEER UN PRODUCTO POR SU ID ---
def get_producto(db: Session, producto_id: int):
    return db.query(models.Producto).filter(models.Producto.id == producto_id).first()

# --- FUNCIÓN PARA LEER UNA LISTA DE PRODUCTOS ---
def get_productos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Producto).offset(skip).limit(limit).all()

# --- FUNCIÓN PARA CREAR UN NUEVO PRODUCTO ---
def create_producto(db: Session, producto: schemas.ProductoCrear):
    # Convertimos el schema de Pydantic a un modelo de SQLAlchemy
    db_producto = models.Producto(**producto.dict())
    db.add(db_producto)  # Lo añadimos a la sesión
    db.commit()          # Confirmamos la transacción (lo guardamos en la BD)
    db.refresh(db_producto) # Refrescamos el objeto para obtener su nuevo ID

def update_producto(db: Session, producto_id: int, producto_update: schemas.ProductoCrear):
    db_producto = db.query(models.Producto).filter(models.Producto.id == producto_id).first()
    if db_producto:
        update_data = producto_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_producto, key, value)
        db.commit()
        db.refresh(db_producto)
    return db_producto

# --- FUNCIÓN PARA BORRAR UN PRODUCTO ---
def delete_producto(db: Session, producto_id: int):
    db_producto = db.query(models.Producto).filter(models.Producto.id == producto_id).first()
    if db_producto:
        db.delete(db_producto)
        db.commit()
    return db_producto
