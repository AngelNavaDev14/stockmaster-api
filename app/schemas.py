from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Schema base para un producto. Contiene los campos comunes.
class ProductoBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    stock: int = 0

# Schema para crear un producto. Hereda de ProductoBase.
class ProductoCrear(ProductoBase):
    pass # No necesita campos adicionales por ahora

# Schema para leer un producto (cuando lo devolvemos desde la API).
# Incluye los campos que la base de datos genera automáticamente (id, fechas).
class Producto(ProductoBase):
    id: int
    fecha_creacion: datetime
    fecha_actualizacion: Optional[datetime] = None

    # Configuración para que Pydantic pueda leer los datos desde un modelo de SQLAlchemy.
    class Config:
        from_attributes = True