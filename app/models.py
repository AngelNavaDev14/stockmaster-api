from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from .database import Base

# Esta clase define la ESTRUCTURA de la tabla 'productos' en nuestra base de datos.
class Producto(Base):
    __tablename__ = "productos"

    # Columnas de la tabla
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), index=True, nullable=False)
    descripcion = Column(String(255), nullable=True)
    precio = Column(Float, nullable=False)
    stock = Column(Integer, default=0)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_actualizacion = Column(DateTime(timezone=True), onupdate=func.now())